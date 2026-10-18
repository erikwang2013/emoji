#!/usr/bin/env python3
"""Commit the visual-assets licence + generated pet forms and push each repo."""
from __future__ import annotations
import importlib.util, os, subprocess, sys
from pathlib import Path

ROOT = Path('/home/wwwroot')
EMOJI = ROOT / 'emoji'
spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)

MSG = ('docs: reserve commercial rights for visual assets\n\n'
       'Project pets, images, icons and emoji are proprietary and require a\n'
       'commercial license. Code licenses are unchanged.')

def run(args, cwd, timeout=120):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0',
               GIT_SSH_COMMAND='ssh -o BatchMode=yes -o ConnectTimeout=10')
    return subprocess.run(args, cwd=str(cwd), env=env, capture_output=True, text=True, timeout=timeout)

def process(project: Path, paths, label):
    if not (project / '.git').is_dir():
        return f'{label}: no git'
    existing = [p for p in paths if (project / p).exists()]
    if not existing:
        return f'{label}: nothing to add'
    r = run(['git', 'add', '--'] + existing, project)
    if r.returncode:
        return f'{label}: add failed: {r.stderr.strip()[:160]}'
    r = run(['git', 'diff', '--cached', '--quiet', '--'] + existing, project)
    committed = False
    if r.returncode != 0:
        r = run(['git', 'commit', '-m', MSG, '--'] + existing, project)
        if r.returncode:
            return f'{label}: commit failed: {r.stderr.strip()[:160]}'
        committed = True
    remote = run(['git', 'remote', 'get-url', 'origin'], project)
    if remote.returncode or not remote.stdout.strip():
        return f'{label}: {"committed" if committed else "unchanged"}, no remote'
    up = run(['git', 'rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}'], project)
    if up.returncode == 0:
        push = run(['git', 'push'], project, timeout=180)
    else:
        push = run(['git', 'push', '-u', 'origin', 'HEAD'], project, timeout=180)
    if push.returncode:
        return f'{label}: {"committed" if committed else "unchanged"}, PUSH FAILED: {push.stderr.strip()[:180]}'
    return f'{label}: {"committed" if committed else "unchanged"}, pushed'

def main():
    for cfg in gp.PETS:
        label = cfg['key']
        project = ROOT / label
        paths = ['ASSETS-LICENSE.md', 'README.md']
        if not cfg['skip']:
            paths.append(cfg['out'])
        try:
            print(process(project, paths, label), flush=True)
        except subprocess.TimeoutExpired:
            print(f'{label}: TIMEOUT', flush=True)
        except Exception as exc:
            print(f'{label}: ERROR {exc}', flush=True)
    # emoji project: everything generated this session
    try:
        print(process(EMOJI, ['ASSETS-LICENSE.md', 'README.md', 'emoji.json', 'shortcodes.json',
                              'demo.html', 'preview.png', 'pets', 'png', 'font', 'tools', '.gitignore'],
                      'emoji'), flush=True)
    except subprocess.TimeoutExpired:
        print('emoji: TIMEOUT', flush=True)
    except Exception as exc:
        print(f'emoji: ERROR {exc}', flush=True)

if __name__ == '__main__':
    main()
