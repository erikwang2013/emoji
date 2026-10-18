#!/usr/bin/env python3
"""Add the visual-assets commercial licence notice to every pet project."""
from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT = Path('/home/wwwroot')
EMOJI = ROOT / 'emoji'
spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)

NOTICE = '''# 视觉资产商业授权 / Visual Assets Commercial License

Copyright (c) 2026 erik <erik@erik.xyz> — https://erik.xyz
All rights reserved.

本项目中的**项目宠物（project pets）、图片（images）、图标（icons）、表情（emoji /
expression forms）及其源文件**（包括但不限于 SVG、PNG、ICO、字体中的图形字形）均为
**非开源资产**。未经作者书面许可，任何人不得复制、修改、再分发、公开传播或将其用于
商业目的。商业使用必须取得商业授权。

The project pets, images, icons, emoji/expression forms and their source files in this
repository are **NOT open-source assets**. All rights are reserved. No copying,
modification, redistribution, public transmission, or commercial use is permitted
without prior written permission. A commercial license is required for commercial use.

**商业授权 / Commercial licensing:** erik@erik.xyz

## 例外 / Exceptions

- 第三方素材仍遵循其原许可证；例如项目内明确标注的 Go Gopher（© Go Authors /
  Renee French, CC BY 4.0）等，不因本文件而改变其授权。
- 代码部分仍遵循仓库根目录的 `LICENSE`（如有）；本文件仅覆盖视觉资产。
- `emoji` 项目中字体文件内用于短码连字的 ASCII 字形派生自 DejaVu Sans，遵循
  `font/LICENSE-DejaVu.txt`。
'''

README_NOTICE = '''
<!-- assets-license:start -->
## 视觉资产授权 / Visual Assets License

本项目的项目宠物、图片、图标、表情（包括 `docs/pet-expressions/` 等目录下的
SVG / PNG）**不是开源资产**，版权归作者所有。未经书面许可不得复制、修改、再分发或
用于商业用途；商业使用需取得商业授权，联系 **erik@erik.xyz**。详见
[ASSETS-LICENSE.md](ASSETS-LICENSE.md)。

> 代码部分仍遵循仓库原有 `LICENSE`；第三方素材（如明确标注的 Go Gopher 等）仍遵循其原许可证。
<!-- assets-license:end -->
'''

def add_notice(project: Path):
    lic = project / 'ASSETS-LICENSE.md'
    if not lic.exists():
        lic.write_text(NOTICE, encoding='utf-8')
    readme = project / 'README.md'
    if not readme.exists():
        return False, 'no README'
    text = readme.read_text(encoding='utf-8', errors='replace')
    if '<!-- assets-license:start -->' in text:
        return False, 'already present'
    block = README_NOTICE
    if '<!-- pet-expressions:end -->' in text:
        text = text.replace('<!-- pet-expressions:end -->', '<!-- pet-expressions:end -->\n' + block, 1)
    else:
        text = text.rstrip() + '\n' + block
    readme.write_text(text, encoding='utf-8')
    return True, 'added'

def main():
    done = 0
    for cfg in gp.PETS:
        project = ROOT / cfg['key']
        if not project.is_dir():
            print('skip missing', cfg['key'])
            continue
        changed, status = add_notice(project)
        print(('ok ' if changed else 'skip '), cfg['key'], status)
        done += int(changed)
    # the emoji project gets the file too; its README is regenerated later
    lic = EMOJI / 'ASSETS-LICENSE.md'
    if not lic.exists():
        lic.write_text(NOTICE, encoding='utf-8')
    print('done', done, 'README updates; licence file ensured for emoji')

if __name__ == '__main__':
    main()
