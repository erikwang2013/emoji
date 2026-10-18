#!/usr/bin/env python3
"""Final commit/push pass: handles SSH-over-443, HTTPS remotes and stale locks."""
from __future__ import annotations
import importlib.util, os, signal, subprocess, time
from pathlib import Path

ROOT = Path('/home/wwwroot')
EMOJI = ROOT / 'emoji'
spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)
MSG = ('docs: reserve commercial rights for visual assets\n\n'
       'Project pets, images, icons and emoji are proprietary and require a\n'
       'commercial license. Code licenses are unchanged.')
ENV = dict(os.environ, GIT_TERMINAL_PROMPT='0')

def run(args, cwd, timeout=45):
    p = subprocess.Popen(args, cwd=str(cwd), env=ENV, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        out, err = p.communicate(timeout=timeout)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        try: os.killpg(p.pid, signal.SIGKILL)
        except ProcessLookupError: pass
        out, err = p.communicate()
        return 124, out, err

def push_project(project: Path, timeout=45):
    # stale lock cleanup
    lock = project / '.git' / 'index.lock'
    if lock.exists():
        age = time.time() - lock.stat().st_mtime
        if age > 60:
            lock.unlink()
    remote = subprocess.run(['git', '-C', str(project), 'remote', 'get-url', 'origin'],
                            capture_output=True, text=True).stdout.strip()
    if not remote:
        return 'no remote (commit kept locally)'
    branch = subprocess.run(['git', '-C', str(project), 'branch', '--show-current'],
                            capture_output=True, text=True).stdout.strip() or 'main'
    up = subprocess.run(['git', '-C', str(project), 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'],
                        capture_output=True, text=True)
    if remote.startswith('https://github.com/'):
        # port 443 is blocked here; use the equivalent SSH remote one-off
        slug = remote[len('https://github.com/'):].removesuffix('.git')
        args = ['git', 'push', f'git@github.com:{slug}.git', f'HEAD:{branch}']
    elif up.returncode == 0:
        args = ['git', 'push']
    else:
        args = ['git', 'push', '-u', 'origin', 'HEAD']
    last = ''
    for i in range(3):
        rc, out, err = run(args, project, timeout=timeout)
        if rc == 0:
            return 'pushed' if i == 0 else f'pushed (retry {i})'
        text = (err or out).strip()
        last = text.splitlines()[-1] if text else f'exit {rc}'
        if 'non-fast-forward' in text or 'fetch first' in text or '被拒绝' in text:
            # try a rebase once, abort on conflict
            f = run(['git', 'fetch', 'origin', branch], project, timeout=45)
            r = run(['git', 'rebase', f'origin/{branch}'], project, timeout=60)
            if r[0] != 0:
                run(['git', 'rebase', '--abort'], project, timeout=30)
                return f'PUSH FAILED (non-fast-forward; conflict): {last}'
            continue
        time.sleep(2)
    return f'PUSH FAILED: {last}'

def process(project: Path, paths, label, timeout=45):
    if not (project / '.git').is_dir():
        return f'{label}: no git'
    existing = [p for p in paths if (project / p).exists()]
    if not existing:
        return f'{label}: nothing'
    rc, out, err = run(['git', 'add', '--'] + existing, project, timeout=45)
    if rc:
        return f'{label}: add failed: {(err or out).strip()[:140]}'
    rc, out, err = run(['git', 'diff', '--cached', '--quiet', '--'] + existing, project, timeout=30)
    committed = False
    if rc != 0:
        rc, out, err = run(['git', 'commit', '-m', MSG, '--'] + existing, project, timeout=60)
        if rc:
            return f'{label}: commit failed: {(err or out).strip()[:140]}'
        committed = True
    status = push_project(project, timeout=timeout)
    return f'{label}: {"committed" if committed else "unchanged"}, {status}'

def main():
    for cfg in gp.PETS:
        paths = ['ASSETS-LICENSE.md', 'README.md']
        if not cfg['skip']:
            paths.append(cfg['out'])
        try:
            print(process(ROOT / cfg['key'], paths, cfg['key']), flush=True)
        except Exception as exc:
            print(f'{cfg["key"]}: ERROR {exc}', flush=True)
    try:
        print(process(EMOJI, ['ASSETS-LICENSE.md', 'README.md', 'emoji.json', 'shortcodes.json',
                              'demo.html', 'preview.png', 'pets', 'png', 'font', 'tools', '.gitignore'],
                      'emoji', timeout=300), flush=True)
    except Exception as exc:
        print(f'emoji: ERROR {exc}', flush=True)

if __name__ == '__main__':
    main()
