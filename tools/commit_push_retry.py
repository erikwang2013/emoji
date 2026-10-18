#!/usr/bin/env python3
"""Retry commits/pushes with short timeouts; safe to re-run."""
from __future__ import annotations
import importlib.util, os, subprocess, time
from pathlib import Path

ROOT = Path('/home/wwwroot')
EMOJI = ROOT / 'emoji'
spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)

MSG = ('docs: reserve commercial rights for visual assets\n\n'
       'Project pets, images, icons and emoji are proprietary and require a\n'
       'commercial license. Code licenses are unchanged.')
ENV = dict(os.environ, GIT_TERMINAL_PROMPT='0',
           GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=10')

def sh(args, cwd, timeout=60):
    return subprocess.run(args, cwd=str(cwd), env=ENV, capture_output=True, text=True, timeout=timeout)

def push(project, timeout=45, attempts=3):
    remote = sh(['git', 'remote', 'get-url', 'origin'], project)
    if remote.returncode or not remote.stdout.strip():
        return 'no remote'
    up = sh(['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'], project)
    args = ['git', 'push'] if up.returncode == 0 else ['git', 'push', '-u', 'origin', 'HEAD']
    last = ''
    for i in range(attempts):
        try:
            r = sh(args, project, timeout=timeout)
        except subprocess.TimeoutExpired:
            last = f'timeout #{i+1}'
            time.sleep(2)
            continue
        if r.returncode == 0:
            return 'pushed' if i == 0 else f'pushed (retry {i})'
        last = (r.stderr or r.stdout).strip().splitlines()[-1][:160] if (r.stderr or r.stdout).strip() else f'exit {r.returncode}'
        time.sleep(2)
    return f'PUSH FAILED: {last}'

def process(project: Path, paths, label, push_timeout=45):
    if not (project / '.git').is_dir():
        return f'{label}: no git'
    lock = project / '.git' / 'index.lock'
    if lock.exists():
        return f'{label}: index.lock exists'
    existing = [p for p in paths if (project / p).exists()]
    if not existing:
        return f'{label}: nothing'
    r = sh(['git', 'add', '--'] + existing, project)
    if r.returncode:
        return f'{label}: add failed: {r.stderr.strip()[:140]}'
    r = sh(['git', 'diff', '--cached', '--quiet', '--'] + existing, project)
    committed = False
    if r.returncode != 0:
        r = sh(['git', 'commit', '-m', MSG, '--'] + existing, project)
        if r.returncode:
            return f'{label}: commit failed: {r.stderr.strip()[:140]}'
        committed = True
    status = push(project, timeout=push_timeout)
    return f'{label}: {"committed" if committed else "unchanged"}, {status}'

def main():
    for cfg in gp.PETS:
        paths = ['ASSETS-LICENSE.md', 'README.md']
        if not cfg['skip']:
            paths.append(cfg['out'])
        try:
            print(process(ROOT / cfg['key'], paths, cfg['key']), flush=True)
        except subprocess.TimeoutExpired:
            print(f'{cfg["key"]}: TIMEOUT', flush=True)
        except Exception as exc:
            print(f'{cfg["key"]}: ERROR {exc}', flush=True)
    try:
        print(process(EMOJI, ['ASSETS-LICENSE.md', 'README.md', 'emoji.json', 'shortcodes.json',
                              'demo.html', 'preview.png', 'pets', 'png', 'font', 'tools', '.gitignore'],
                      'emoji', push_timeout=300), flush=True)
    except subprocess.TimeoutExpired:
        print('emoji: TIMEOUT', flush=True)
    except Exception as exc:
        print(f'emoji: ERROR {exc}', flush=True)

if __name__ == '__main__':
    main()
