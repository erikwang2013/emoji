#!/usr/bin/env python3
"""Extract the 12 OPI keycap panels from the design sheet into standalone SVGs."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path
import xml.etree.ElementTree as ET

EMOJI = Path('/home/wwwroot/emoji')
SRC = Path('/home/wwwroot/bag/opi/docs/opi-pet-forms.svg')
OUT = EMOJI / 'sources' / 'opi'
SVG = 'http://www.w3.org/2000/svg'
XLINK = 'http://www.w3.org/1999/xlink'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', XLINK)

# Whole-body motion per mood; OPI's art has no per-part ids to target.
MOTION = {
    'smile':      ('bob',    3.0, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); }'),
    'joy':        ('bounce', 1.7, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); }'),
    'cry':        ('droop',  4.0, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(4px); }'),
    'depressed':  ('droop',  4.5, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(5px); }'),
    'terrified':  ('shiver', 0.18, '0%, 100% { transform: translateX(0); } 25% { transform: translateX(-1.5px); } 75% { transform: translateX(1.5px); }'),
    'angry':      ('shake',  0.3,  '0%, 100% { transform: translateX(0); } 25% { transform: translateX(-2px); } 75% { transform: translateX(2px); }'),
    'coquettish': ('sway',   3.0, '0%, 100% { transform: rotate(-2deg); } 50% { transform: rotate(2deg); }'),
    'cute':       ('bounce', 1.5, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); }'),
    'pleasing':   ('bob',    2.1, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); }'),
    'knocking':   ('tap',    0.9,  '0%, 100% { transform: translateX(0); } 30% { transform: translateX(6px); } 55% { transform: translateX(-1px); }'),
    'facepalm':   ('sway',   3.2, '0%, 100% { transform: rotate(-2deg); } 50% { transform: rotate(2deg); }'),
    'tongue':     ('bob',    2.6, '0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); }'),
}

spec = importlib.util.spec_from_file_location('gp', EMOJI / 'tools/generate_pets.py')
gp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gp)

def local(tag):
    return tag.split('}')[-1]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    root = ET.parse(SRC).getroot()
    defs = root.find(f'{{{SVG}}}defs')
    if defs is None:
        raise SystemExit('defs not found')
    panels = []
    for g in root.iter(f'{{{SVG}}}g'):
        direct = [c for c in list(g) if local(c.tag) == 'use']
        if any((c.get('href') or c.get(f'{{{XLINK}}}href')) == '#forms-back' for c in direct):
            panels.append(g)
    if len(panels) != 12:
        raise SystemExit(f'expected 12 panels, got {len(panels)}')
    for (slug, zh, en, _), panel in zip(gp.MOODS, panels):
        svg = ET.Element(f'{{{SVG}}}svg', {
            'viewBox': '0 0 240 250', 'width': '240', 'height': '250',
            'role': 'img', 'aria-label': f'OPI 小欧 · {zh}'})
        name, dur, frames = MOTION[slug]
        style = ET.Element(f'{{{SVG}}}style')
        style.text = (
            f'.opi-motion {{ animation: opi-{name} {dur}s ease-in-out infinite; '
            'transform-origin: 120px 125px; }\n'
            f'@keyframes opi-{name} {{ {frames} }}\n'
            '@media (prefers-reduced-motion: reduce) { .opi-motion { animation: none !important; } }')
        svg.append(style)
        svg.append(copy.deepcopy(defs))
        holder = ET.SubElement(svg, f'{{{SVG}}}g', {'class': 'opi-motion'})
        for child in list(panel):
            holder.append(copy.deepcopy(child))
        tree = ET.ElementTree(svg)
        tree.write(OUT / f'{slug}.svg', encoding='utf-8', xml_declaration=False)
    print('wrote', len(panels), 'panels to', OUT)

if __name__ == '__main__':
    main()
