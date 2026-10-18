#!/usr/bin/env python3
"""Build the pet-emoji atlas: images, PNGs, manifest, shortcodes, README, demo."""
from __future__ import annotations
import html, importlib.util, json, shutil, subprocess
from pathlib import Path
from PIL import Image, ImageDraw

EMOJI = Path('/home/wwwroot/emoji')
ROOT = Path('/home/wwwroot')
THUMB_SIZE = 64
spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)

CATALOG_EXTRA = [dict(
    key='polypack', pet='Pax', out='docs/assets', skip=False,
    file_map={'smile': 'pax-smile.svg', 'joy': 'pax-joy.svg', 'cry': 'pax-cry.svg',
              'depressed': 'pax-dejected.svg', 'terrified': 'pax-shock.svg',
              'angry': 'pax-angry.svg', 'coquettish': 'pax-coquettish.svg',
              'cute': 'pax-cute.svg', 'pleasing': 'pax-ingratiating.svg',
              'knocking': 'pax-knock.svg', 'facepalm': 'pax-facepalm.svg',
              'tongue': 'pax-tongue.svg'},
), dict(
    key='opi', pet='小欧', src_dir=str(EMOJI / 'sources' / 'opi'), skip=False,
)]

MOOD_ZH = {m[0]: m[1] for m in gp.MOODS}
MOOD_EN = {m[0]: m[2] for m in gp.MOODS}

def project_slug(key: str) -> str:
    for p in ('bag/', 'erikwang2013/'):
        if key.startswith(p):
            key = key[len(p):]
    return key.replace('/', '-')

def make_entries():
    entries, projects = [], []
    idx = 0
    for cfg in (gp.PETS + CATALOG_EXTRA):
        if cfg.get('skip') or cfg.get('catalog_skip'):
            continue
        slug = project_slug(cfg['key'])
        src_dir = Path(cfg['src_dir']) if cfg.get('src_dir') else ROOT / cfg['key'] / cfg['out']
        out_img = EMOJI / 'pets' / slug
        out_png = EMOJI / 'png' / slug
        out_img.mkdir(parents=True, exist_ok=True)
        out_png.mkdir(parents=True, exist_ok=True)
        forms = []
        for mood, zh, en, _ in gp.MOODS:
            src = src_dir / cfg.get('file_map', {}).get(mood, f'{mood}.svg')
            if not src.exists():
                raise FileNotFoundError(src)
            dst = out_img / f'{mood}.svg'
            if not dst.exists():
                shutil.copyfile(src, dst)
            png = out_png / f'{mood}.png'
            need_render = True
            if png.exists():
                try:
                    if Image.open(png).size == (128, 128):
                        need_render = False
                except Exception:
                    pass
            if need_render:
                subprocess.run(['rsvg-convert', '-w', '128', '-h', '128', str(dst), '-o', str(png)],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                im = Image.open(png).convert('RGBA')
                if im.size != (128, 128):
                    canvas = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
                    canvas.alpha_composite(im, ((128 - im.width) // 2, (128 - im.height) // 2))
                    canvas.save(png, optimize=True)
            thumb = EMOJI / 'thumbs' / slug / f'{mood}.png'
            thumb.parent.mkdir(parents=True, exist_ok=True)
            Image.open(png).convert('RGBA').resize((THUMB_SIZE, THUMB_SIZE), Image.LANCZOS).save(
                thumb, optimize=True)
            cp = 0xE000 + idx
            e = {
                'project': cfg['key'],
                'project_slug': slug,
                'pet': cfg['pet'],
                'mood': mood,
                'mood_zh': zh,
                'mood_en': en,
                'shortcode': f':{slug}-{mood}:',
                'alias': f':emoji-{slug}-{mood}:',
                'codepoint': f'U+{cp:04X}',
                'image': f'pets/{slug}/{mood}.svg',
                'png': f'png/{slug}/{mood}.png',
            }
            entries.append(e)
            forms.append(e)
            idx += 1
        projects.append({
            'project': cfg['key'],
            'project_slug': slug,
            'pet': cfg['pet'],
            'count': len(forms),
            'forms': forms,
        })
    return projects, entries

def write_manifest(projects, entries):
    manifest = {
        'name': 'Pet Emoji Atlas',
        'version': '2.0.0',
        'description': 'Project-pet expression emoji: image + colour bitmap font + shortcode.',
        'format': 'image + font + shortcode',
        'counts': {'projects': len(projects), 'forms': len(entries), 'moods_per_pet': 12},
        'font': 'font/emoji.ttf',
        'css': 'font/emoji.css',
        'codepoint_range': f"U+{0xE000:04X}..U+{0xE000 + len(entries) - 1:04X}",
        'projects': projects,
        'emojis': entries,
    }
    (EMOJI / 'emoji.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    sc = {}
    for e in entries:
        info = {'slug': f"{e['project_slug']}-{e['mood']}", 'codepoint': e['codepoint'],
                'image': e['image'], 'png': e['png'], 'pet': e['pet'], 'project': e['project']}
        sc[e['shortcode']] = info
        sc[e['alias']] = info
    (EMOJI / 'shortcodes.json').write_text(json.dumps(sc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return manifest

def write_readme(projects, entries, manifest):
    def grid(forms):
        head = '| ' + ' | '.join(e['mood_zh'] for e in forms) + ' |'
        rule = '|' + ':--:|' * len(forms)
        imgs = '| ' + ' | '.join(
            f'![{e["mood_zh"]}](thumbs/{e["project_slug"]}/{e["mood"]}.png)' for e in forms) + ' |'
        return '\n'.join((head, rule, imgs))
    summary = '\n'.join(
        f'| {i+1} | {p["pet"]} | `{p["project"]}` | `:{p["project_slug"]}-*:` | {p["count"]} |'
        for i, p in enumerate(projects))
    details = []
    for p in projects:
        grids = [grid(p['forms'][i:i + 6]) for i in range(0, len(p['forms']), 6)]
        codes = ' · '.join(f'`{e["shortcode"]}`' for e in p['forms'])
        details.append(
            f'### {p["pet"]} · `{p["project"]}` · `:{p["project_slug"]}-*:`\n\n'
            + '\n\n'.join(grids) + '\n\n' + codes)
    first = entries[0]
    readme = f'''# 项目宠物 Emoji 图鉴 · Pet Emoji Atlas

**{manifest["counts"]["projects"]} 个项目 × 12 种形态 = {manifest["counts"]["forms"]} 枚宠物表情 emoji。**
每一枚同时提供 **图片（SVG / PNG）+ 彩色字体（CBDT/CBLC TTF）+ 短码（shortcode）**。

> **授权 / License**：本项目中的项目宠物、图片、图标、表情及字体中的图形字形均为
> **非开源资产**，商业使用需取得商业授权。详见 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。

## 12 种形态

笑 / 欢乐 / 哭 / 沮丧 / 惊恐 / 愤怒 / 撒娇 / 卖萌 / 讨好 / 敲打 / 捂脸 / 吐舌头

## 用法

### 1. 图片

```markdown
![{first["mood_zh"]}]({first["image"]})
![{first["mood_zh"]}]({first["png"]})
```

### 2. 字体

引入 `font/emoji.css` 后，使用字体族 `Pet Emoji Atlas` 与码位 `{first["codepoint"]}` 显示对应字形；支持 `liga` 连字的编辑器也可直接输入短码。

```css
@import url("font/emoji.css");
```

字体为 CBDT/CBLC 彩色位图字体；支持彩色位图字体的环境会显示对应宠物表情，否则请使用图片。

### 3. 短码

```text
{first["shortcode"]}
{first["alias"]}
```

- 主短码：`:<项目>-<形态>:`
- 别名：`:emoji-<项目>-<形态>:`
- 字体码位：`{manifest["codepoint_range"]}`
- 全量映射见 [shortcodes.json](shortcodes.json)；字体内置主短码 `:<项目>-<形态>:` 的 `liga` 连字。
- `:emoji-<项目>-<形态>:` 别名可用 `shortcodes.json` 映射为图片或对应码位；需要把短码渲染成图片时，查 `image` 字段。

## 项目总览

| # | 宠物 | 项目 | 短码前缀 | 形态 |
|---|---|---|---|---|
{summary}

## 逐项目预览

{(chr(10) * 2).join(details)}

## 说明

- 图片源文件在 `pets/<项目>/<形态>.svg`，PNG 在 `png/<项目>/<形态>.png`，README 预览使用 `thumbs/<项目>/<形态>.png`（{THUMB_SIZE}×{THUMB_SIZE}）。
- `preview.png` 是所有项目「笑」形态的总览。
- 已去除与其他项目重复的 7 个宠物入口：`aetherupload-rust`、`apidoc-go`、`apidoc-rust`、`apidoc-ui`、`encryptable-rust`、`hashids-rust`、`snowflake-rust`；保留对应的 PHP / Webman 版本。`jwt-rust` 已改为独立橘猫形象，重新纳入。
- 本项目代码与生成脚本仍遵循其原有许可；视觉资产适用 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。
'''
    (EMOJI / 'README.md').write_text(readme, encoding='utf-8')

def write_demo(projects, entries):
    sections = []
    for p in projects:
        cards = '\n'.join(
            f'''      <div class="card" data-text="{html.escape((p["pet"]+' '+p["project"]+' '+e["mood_zh"]+' '+e["shortcode"]).lower())}">
        <img src="{e["image"]}" alt="{html.escape(e["mood_zh"])}">
        <h4>{e["mood_zh"]}</h4>
        <code>{e["shortcode"]}</code>
      </div>''' for e in p['forms'])
        sections.append(
            f'''<section class="project" data-project="{p["project_slug"]}">
  <h2>{html.escape(p["pet"])} <small>{p["project"]} · <code>:{p["project_slug"]}-*:</code></small></h2>
  <div class="grid">
{cards}
  </div>
</section>''')
    first = entries[0]
    font_strip = ' '.join(
        f'<span class="mood-emoji" title="{html.escape(e["mood_zh"])}">&#x{int(e["codepoint"][2:],16):X};</span>'
        for e in projects[0]['forms'])
    short_strip = ' · '.join(
        f'<span class="mood-emoji">{e["shortcode"]}</span>' for e in projects[0]['forms'])
    demo = f'''<!doctype html>
<html lang="zh-CN">
<meta charset="utf-8">
<title>Pet Emoji Atlas · 图片 + 字体 + 短码</title>
<link rel="stylesheet" href="font/emoji.css">
<style>
  body {{ margin:0; padding:32px; background:#fff9ea; color:#3b2a14;
         font-family: system-ui,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif; }}
  h1 {{ margin:0 0 6px; }} p.lead {{ color:#8a6a3a; margin:0 0 18px; }}
  input {{ width:100%; box-sizing:border-box; padding:10px 14px; border-radius:10px;
           border:1px solid #e7d3a6; font:inherit; margin-bottom:24px; }}
  section.project {{ background:#fff; border:1px solid #f0dfb8; border-radius:18px;
                     padding:16px 18px; margin:0 0 18px; }}
  section.project h2 {{ font-size:18px; margin:0 0 12px; }}
  section.project h2 small {{ font-weight:400; color:#8a6a3a; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(104px,1fr)); gap:10px; }}
  .card {{ text-align:center; padding:8px; border-radius:12px; background:#fffaf0; }}
  .card img {{ width:72px; height:72px; }}
  .card h4 {{ margin:2px 0; font-size:13px; }}
  .card code {{ font-size:10px; color:#8a6a3a; word-break:break-all; }}
  .fontbox {{ background:#fff; border:1px solid #f0dfb8; border-radius:18px; padding:18px; margin:0 0 18px; }}
  .mood-emoji {{ font-size:40px; line-height:1.4; }}
  #out img {{ width:36px; vertical-align:middle; }}
</style>
<h1>Pet Emoji Atlas</h1>
<p class="lead">{len(projects)} 个项目 × 12 形态 = {len(entries)} 枚宠物表情。图片 / 彩色字体 / 短码三种用法。</p>
<input id="q" placeholder="搜索宠物、项目、形态或短码…">
<div class="fontbox">
  <h2>字体字形与短码连字（{html.escape(projects[0]["pet"])}）</h2>
  <div class="mood-emoji">{font_strip}</div>
  <div class="mood-emoji">{short_strip}</div>
</div>
<div id="projects">
{chr(10).join(sections)}
</div>
<div class="fontbox">
  <h2>短码 → 图片</h2>
  <p><code>{first["shortcode"]}</code> → <span id="out"></span></p>
</div>
<script>
const firstMap = {{"{first["shortcode"]}": "{first["image"]}"}};
document.getElementById('out').innerHTML = `<img src="${{firstMap["{first["shortcode"]}"]}}" alt="">`;
document.getElementById('q').addEventListener('input', e => {{
  const q = e.target.value.toLowerCase();
  document.querySelectorAll('.card').forEach(c => {{
    c.style.display = c.dataset.text.includes(q) ? '' : 'none';
  }});
  document.querySelectorAll('section.project').forEach(s => {{
    const any = [...s.querySelectorAll('.card')].some(c => c.style.display !== 'none');
    s.style.display = any ? '' : 'none';
  }});
}});
</script>
</html>
'''
    (EMOJI / 'demo.html').write_text(demo, encoding='utf-8')

def write_preview(projects):
    cell = 96
    cols = 11
    rows = (len(projects) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cell, rows * cell), '#FFF9EA')
    for i, p in enumerate(projects):
        png = EMOJI / 'png' / p['project_slug'] / 'smile.png'
        im = Image.open(png).convert('RGBA').resize((cell, cell))
        bg = Image.new('RGBA', (cell, cell), (255, 249, 234, 255))
        bg.alpha_composite(im, (0, 0))
        sheet.paste(bg.convert('RGB'), ((i % cols) * cell, (i // cols) * cell))
    sheet.save(EMOJI / 'preview.png')

def main():
    projects, entries = make_entries()
    manifest = write_manifest(projects, entries)
    write_readme(projects, entries, manifest)
    write_demo(projects, entries)
    write_preview(projects)
    print(f'projects={len(projects)} forms={len(entries)} codepoints={manifest["codepoint_range"]}')

if __name__ == '__main__':
    main()
