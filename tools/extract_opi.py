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
        svg.append(copy.deepcopy(defs))
        holder = ET.SubElement(svg, f'{{{SVG}}}g')
        for child in list(panel):
            holder.append(copy.deepcopy(child))
        tree = ET.ElementTree(svg)
        tree.write(OUT / f'{slug}.svg', encoding='utf-8', xml_declaration=False)
    print('wrote', len(panels), 'panels to', OUT)

if __name__ == '__main__':
    main()
