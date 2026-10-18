#!/usr/bin/env python3
"""Generate 12 animated expression variants for every project pet.

Each variant keeps the original pet artwork, removes its own animations, and
adds a colour-matched expression face plus mood effects.  Existing files are
never overwritten.
"""
from __future__ import annotations
import argparse, math, os, re, shutil
from pathlib import Path

ROOT = Path('/home/wwwroot')
EMOJI = ROOT / 'emoji'

MOODS = [
    ('smile',      '笑',     'Smile',       'emoji-smile'),
    ('joy',        '欢乐',   'Joy',         'emoji-joy'),
    ('cry',        '哭',     'Cry',         'emoji-cry'),
    ('depressed',  '沮丧',   'Depressed',   'emoji-depressed'),
    ('terrified',  '惊恐',   'Terrified',   'emoji-terrified'),
    ('angry',      '愤怒',   'Angry',       'emoji-angry'),
    ('coquettish', '撒娇',   'Coquettish',  'emoji-coquettish'),
    ('cute',       '卖萌',   'Cute',        'emoji-cute'),
    ('pleasing',   '讨好',   'Pleasing',    'emoji-pleasing'),
    ('knocking',   '敲打',   'Knocking',    'emoji-knocking'),
    ('facepalm',   '捂脸',   'Facepalm',    'emoji-facepalm'),
    ('tongue',     '吐舌头', 'Tongue Out',  'emoji-tongue'),
]
MOOD = {m[0]: m for m in MOODS}

ACCENT = {
    'smile': '#FFD166', 'joy': '#FF6B9D', 'cry': '#4FA3FF',
    'depressed': '#8A9BB0', 'terrified': '#9B7BFF', 'angry': '#EF4444',
    'coquettish': '#FF7AA2', 'cute': '#FFC93C', 'pleasing': '#5FBF9F',
    'knocking': '#F59E0B', 'facepalm': '#FB7185', 'tongue': '#FF5C8A',
}

# ---------------------------------------------------------------------------
# SVG helpers
# ---------------------------------------------------------------------------

def esc(s: str) -> str:
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))

def n(v: float) -> str:
    return f'{v:.2f}'.rstrip('0').rstrip('.')

def E(cx, cy, rx, ry, fill, rot=None):
    t = f' transform="rotate({rot} {n(cx)} {n(cy)})"' if rot else ''
    return (f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" '
            f'fill="{fill}"{t}/>')

def CIR(cx, cy, r, fill):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{fill}"/>'

def R(x, y, w, h, rx, fill):
    return (f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" '
            f'rx="{n(rx)}" fill="{fill}"/>')

def POLY(points, fill):
    return f'<polygon points="{points}" fill="{fill}"/>'

# ---------------------------------------------------------------------------
# Pet registry
# ---------------------------------------------------------------------------

def P(key, src, pet, eyes, r, patches, ink, **kw):
    """Compact pet configuration.

    eyes: (x1, x2, y) or ((x1, y1), (x2, y2))
    """
    if len(eyes) == 3 and not isinstance(eyes[0], (tuple, list)):
        x1, x2, y = eyes
        e1, e2 = (x1, y), (x2, y)
    else:
        e1, e2 = eyes
    d = dict(key=key, src=str(ROOT / src) if not str(src).startswith('/') else str(src),
             pet=pet, e1=e1, e2=e2, r=r, patches=patches, ink=ink,
             line=kw.pop('line', ink), pupil=kw.pop('pupil', ink),
             sclera=kw.pop('sclera', '#FFFFFF'),
             blush=kw.pop('blush', '#FF8FB3'),
             mouth_y=kw.pop('mouth_y', None),
             mouth_color=kw.pop('mouth_color', ink),
             mouth_fill=kw.pop('mouth_fill', '#4A1D2E'),
             paw=kw.pop('paw', None), paw_line=kw.pop('paw_line', None),
             out=kw.pop('out', 'docs/pet-expressions'),
             readme=kw.pop('readme', 'README.md'),
             badge=kw.pop('badge', False),
             badge_cx=kw.pop('badge_cx', None), badge_cy=kw.pop('badge_cy', None),
             badge_r=kw.pop('badge_r', None),
             decor=kw.pop('decor', ''), scale=kw.pop('scale', 1.0),
             viewbox=kw.pop('viewbox', None),
             skip=kw.pop('skip', False), note=kw.pop('note', ''))
    if d['paw'] is None:
        hexes = [p for p in patches if re.search(r'#[0-9A-Fa-f]{6}', p)]
        m = re.search(r'#[0-9A-Fa-f]{6}', hexes[-1]) if hexes else None
        d['paw'] = m.group(0) if m else '#FFFFFF'
    if d['paw_line'] is None:
        d['paw_line'] = d['line']
    return d

PETS = [
    # ---- top level -------------------------------------------------------
    P('ads-php', 'ads-php/docs/diagrams/svg/pet.svg', '阿章',
      (96, 144, 100), 22,
      [E(120, 112, 46, 38, '#2A4A76')],
      '#EAF4FF', line='#0B1A33', pupil='#16213E', paw='#2E5C92', paw_line='#0B1A33'),
    P('appointment-php', 'appointment-php/docs/diagrams/mascot.svg', '小约',
      (202, 278, 250), 14,
      [E(240, 266, 56, 42, '#FFFFFF')],
      '#2B2348', paw='#FFFFFF', paw_line='#2B2348'),
    P('bee-rust', 'bee-rust/docs/rusty.svg', 'Rusty',
      (205, 307, 162), 30,
      [E(256, 202, 80, 72, '#FFC12B')],
      '#2A1E16', paw='#F5B81C', paw_line='#2A1E16'),
    P('bee-rust-admin', 'bee-rust-admin/docs/pet/keeper-onduty.svg', '阿守',
      (224, 288, 170), 20,
      [E(256, 196, 70, 62, 'url(#headGrad)')],
      '#3A2A1A', paw='#FFC12B', paw_line='#3A2A1A',
      out='docs/pet/expressions'),
    P('cloud-php', 'cloud-php/docs/diagrams/c.svg', '云团',
      (212, 268, 170), 13,
      [E(240, 192, 62, 46, '#E8F1FD')],
      '#1E3A8A', paw='#FFFFFF', paw_line='#1E3A8A'),
    P('e-cat', 'e-cat/docs/e-cat.svg', 'E-Cat',
      (0, 0, 0), 20, [], '#0F172A',
      badge=True, badge_cx=360, badge_cy=120, badge_r=64,
      paw='#F1E5D0', paw_line='#5C4A3A',
      note='photo mascot: mood badge + effects'),
    P('erik-talk', 'erik-talk/docs/mascot.svg', 'Loupi',
      (109, 123, 84), 5.2,
      [POLY('131.7,92.5 122.5,100.4 109.5,100.4 100.3,92.5 100.3,79.5 109.5,71.6 122.5,71.6 131.7,79.5', '#1F2338')],
      '#E7F5F0', line='#E7F5F0', pupil='#008060', mouth_color='#E7F5F0',
      blush='#7FD8C8', paw='#C8912F', paw_line='#7A5318'),
    P('erp-php', 'erp-php/docs/mascot.svg', '小八爪',
      (178, 222, 122), 13,
      [E(200, 139, 48, 41, 'url(#bodyGrad)')],
      '#FFFFFF', line='#0D1B3E', pupil='#0D1B3E', paw='#2C62D1', paw_line='#0D1B3E'),
    P('game-platform-php', 'game-platform-php/docs/mascot.svg', 'Dicey',
      ((85.3, 90), (113, 86.1)), 10.5,
      [E(100, 98, 34, 27, '#6B4FE8')],
      '#FFFFFF', line='#2B1A5E', pupil='#2B1A5E', paw='#6B4FE8', paw_line='#2B1A5E'),
    P('insurance-service', 'insurance-service/docs/mascot.svg', '霜霜',
      (164, 236, 188), 13.5,
      [E(200, 206, 62, 50, 'url(#fur)')],
      '#2B3A55', paw='#FFFFFF', paw_line='#A9C6EE'),
    P('integrated-global-logistics', 'integrated-global-logistics/docs/diagrams/mascot.svg', 'E-Cat',
      (220, 292, 196), 11,
      [E(256, 214, 60, 48, '#FF8A3D')],
      '#26324B', paw='#FF8A3D', paw_line='#26324B'),
    P('iot-platform', 'iot-platform/docs/mascot.svg', 'IoT Bot',
      (155, 245, 184), 15,
      [R(115, 140, 170, 112, 36, '#EFF6FF')],
      '#0F172A', paw='#EFF6FF', paw_line='#0F172A'),
    P('item-rental', 'item-rental/docs/mascot.svg', '租租鼠',
      (71.4, 145.5, 129.3), 11.4,
      [E(108, 146, 58, 44, '#8CC5E7'), E(108, 160, 22, 13, '#B8937F'), E(108, 169, 14, 7, '#E0DEDC')],
      '#111212', paw='#8CC5E7', paw_line='#3C89BF'),
    P('omb', 'omb/docs/omb-pet.svg', '小音机',
      (56, 136, 111), 20,
      [CIR(56, 111, 20, 'url(#cream)'), CIR(136, 111, 20, 'url(#cream)'),
       E(96, 118, 15, 9, 'url(#body)')],
      '#0B6E82', mouth_y=122, paw='#F4633A', paw_line='#B33A18'),
    P('open-admin', 'open-admin/public/img/pet.svg', '小安',
      (101, 139, 144), 12,
      [R(73, 109, 94, 70, 20, 'url(#ptScreen)')],
      '#7CD4FF', line='#7CD4FF', pupil='#0B1F45', sclera='#7CD4FF',
      mouth_color='#7CD4FF', paw='#1677FF', paw_line='#7CD4FF'),
    P('open-novel', 'open-novel/docs/pet.svg', 'Novi',
      (224, 288, 220), 21,
      [E(256, 234, 62, 44, 'url(#ink)')],
      '#DCE6F2', line='#DCE6F2', pupil='#1F2C3D', sclera='#F4F8FF',
      mouth_color='#DCE6F2', blush='#E8927C', paw='#2E4057', paw_line='#DCE6F2'),
    P('open-travel', 'open-travel/docs/mascot.svg', '南南',
      (218, 294, 256), 20,
      [CIR(256, 262, 138, '#F6FCFF')],
      '#1F2328', paw='#2F6FED', paw_line='#1F2328'),
    P('property-management-platform', 'property-management-platform/docs/images/pet_xiaozhu.svg', '小筑',
      (118, 162, 178), 10.5,
      [R(100, 156, 80, 60, 14, 'url(#xzBody)')],
      '#FFFFFF', line='#C7D2FE', pupil='#1E1B4B', sclera='#FFFFFF',
      mouth_color='#FFFFFF', paw='#FFFFFF', paw_line='#3730A3'),
    P('quantitative-trading', 'quantitative-trading/docs/images/pet.svg', '算子',
      (0, 0, 0), 20, [], '#1E2A33',
      badge=True, badge_cx=256, badge_cy=70, badge_r=52,
      paw='#D9A441', paw_line='#1E2A33',
      note='abacus pet intentionally has no face: mood badge + bead colour'),
    P('shop-php', 'shop-php/docs/pet.svg', '雪球 Snowy',
      (107, 149, 140), 8.5,
      [CIR(128, 150, 68, 'url(#globe)')],
      '#0B2E52', paw='#2D8CF0', paw_line='#0B2E52',
      decor='<g clip-path="url(#globeClip)" fill="none" stroke="#FFFFFF" stroke-opacity=".28" stroke-width="3"><ellipse cx="128" cy="150" rx="72" ry="26"/><ellipse cx="128" cy="150" rx="30" ry="72"/></g>'),
    P('social', 'social/docs/diagrams/mascot.svg', 'Bub',
      (97, 145, 104), 17,
      [E(120, 120, 55, 42, '#2563EB')],
      '#0F172A', paw='#2563EB', paw_line='#0F172A'),
    P('ssd', 'ssd/docs/assets/ssd-mascot.svg', 'ssd',
      (204, 308, 230), 25,
      [E(256, 250, 78, 50, '#EAF2FE')],
      '#14294F', mouth_y=285, paw='#FFFFFF', paw_line='#14294F'),
    P('super-ops', 'super-ops/docs/images/pet-icon.svg', '超猫 SuperCat',
      (25, 39, 33), 4.8,
      [E(32, 38, 16, 14, '#F1F5F9')],
      '#0F172A', mouth_y=45, paw='#F1F5F9', paw_line='#0F172A'),
    # ---- bag -------------------------------------------------------------
    P('bag/aetherupload-rust', 'bag/aetherupload-rust/docs/pet.svg', '以太兽',
      (100, 140, 136), 7.5,
      [E(120, 148, 42, 32, '#62A7FF')],
      '#0D1B34', paw='#62A7FF', paw_line='#0D1B34'),
    P('bag/apidoc-go', 'bag/apidoc-go/docs/svg/apidoc-pet.svg', 'Apidoc',
      (112, 148, 114), 10,
      [E(130, 126, 34, 26, '#FFFFFF')],
      '#3B3663', paw='#FFFFFF', paw_line='#3B3663'),
    P('bag/apidoc-rust', 'bag/apidoc-rust/docs/images/apidoc-pet.svg', 'Apidoc',
      (112, 148, 114), 10,
      [E(130, 126, 34, 26, '#FFFFFF')],
      '#3B3663', paw='#FFFFFF', paw_line='#3B3663'),
    P('bag/canal', 'bag/canal/docs/assets/canal-pet.svg', '小运',
      (322, 398, 102), 26,
      [E(360, 120, 68, 46, '#E85D2A')],
      '#22202B', mouth_y=158, paw='#E85D2A', paw_line='#22202B'),
    P('bag/druid-rust', 'bag/druid-rust/docs/assets/mascot.svg', '小德',
      (70, 90, 80), 5.5,
      [E(80, 87, 22, 18, '#F3CD92')],
      '#12263A', paw='#F3CD92', paw_line='#12263A'),
    P('bag/encryptable-rust', 'bag/encryptable-rust/docs/pet.svg', 'Locky',
      (132, 188, 184), 11.5,
      [E(160, 199, 42, 34, '#E8EDFF')],
      '#1E1B4B', paw='#E8EDFF', paw_line='#1E1B4B'),
    P('bag/encryption-rust', 'bag/encryption-rust/docs/pet.svg', 'Locky',
      (96, 144, 158), 13,
      [E(120, 172, 46, 36, '#3B4EDB')],
      '#FFFFFF', line='#312E81', pupil='#0F172A', paw='#3B4EDB', paw_line='#312E81'),
    P('bag/go-scout', 'bag/go-scout/docs/mascot.svg', '小侦 Scouty',
      (114, 146, 132), 7,
      [E(130, 144, 32, 24, '#DBE8E5')],
      '#3A3A3A', paw='#DBE8E5', paw_line='#3A3A3A'),
    P('bag/hashids-rust', 'bag/hashids-rust/docs/mascot.svg', '哈希迪 Hashy',
      (91, 129, 110), 14,
      [E(110, 122, 36, 28, '#FFFFFF')],
      '#0F172A', paw='#FFFFFF', paw_line='#0F172A'),
    P('bag/jwt-rust', 'bag/jwt-rust/docs/pet.svg', '钥匙小卫 Kee',
      (102, 138, 86), 6.8,
      [E(120, 95, 28, 22, '#F7AC15')],
      '#1F2937', paw='#F7AC15', paw_line='#1F2937'),
    P('bag/poster-rust', 'bag/poster-rust/assets/pet.svg', 'Posty',
      (126, 174, 128), 10,
      [E(150, 141, 37, 30, '#FFFDF8')],
      '#2D3436', paw='#FFFDF8', paw_line='#2D3436'),
    P('bag/rust-scout', 'bag/rust-scout/docs/svg/pet.svg', 'Scout',
      (226, 274, 159), 7.5,
      [R(200, 142, 100, 34, 17, '#0F172A'), E(250, 189, 20, 9, '#FFFFFF')],
      '#60A5FA', line='#0F172A', pupil='#0F172A', sclera='#60A5FA',
      mouth_color='#64748B', paw='#CBD5E1', paw_line='#64748B',
      viewbox=(150, 80, 220, 300)),
    P('bag/security-go', 'bag/security-go/pet/pet.svg', '哨兵鼠',
      (141, 185, 190), 8.5,
      [E(163, 202, 44, 34, 'url(#p-body)'), E(160, 235, 40, 26, '#7FD8EE')],
      '#0B1220', mouth_y=235, paw='#00A3CC', paw_line='#0B1220',
      out='pet/expressions'),
    P('bag/security-rust', 'bag/security-rust/docs/pet.svg', '甲哨 Sentri',
      (196, 288, 128), 8,
      [E(240, 142, 66, 46, '#CE422B')],
      '#1F1B18', paw='#CE422B', paw_line='#1F1B18'),
    P('bag/snowflake-rust', 'bag/snowflake-rust/docs/pet.svg', '雪花精灵',
      (145, 175, 145), 5,
      [E(160, 152, 26, 20, '#FFFFFF')],
      '#0F1E33', paw='#FFFFFF', paw_line='#0F1E33'),
    # ---- erikwang2013 ---------------------------------------------------
    P('erikwang2013/aetherupload-webman', 'erikwang2013/aetherupload-webman/docs/js/aetherupload-pet.svg', '以太兽',
      (100, 140, 136), 7.5,
      [E(120, 148, 42, 32, '#62A7FF')],
      '#0D1B34', paw='#62A7FF', paw_line='#0D1B34'),
    P('erikwang2013/apidoc-php', 'erikwang2013/apidoc-php/assets/apidoc-pet.svg', 'Apidoc',
      (112, 148, 114), 10,
      [E(130, 126, 34, 26, '#FFFFFF')],
      '#3B3663', paw='#FFFFFF', paw_line='#3B3663'),
    P('erikwang2013/apidoc-ui', 'erikwang2013/apidoc-ui/assets/apidoc-pet.svg', 'Apidoc UI',
      (112, 148, 114), 10,
      [E(130, 126, 34, 26, '#FFFFFF')],
      '#3B3663', paw='#FFFFFF', paw_line='#3B3663'),
    P('erikwang2013/clickhouse-php', 'erikwang2013/clickhouse-php/docs/pet.svg', 'ClickHouse 小象',
      (0, 0, 0), 8, [], '#1E2233',
      badge=True, badge_cx=32, badge_cy=38, badge_r=30,
      paw='#777BB4', paw_line='#1E2233',
      note='side-profile house elephant: mood badge + effects'),
    P('erikwang2013/consul-php', 'erikwang2013/consul-php/docs/images/pet.svg', 'Consu',
      (138, 182, 176), 8.5,
      [R(102, 150, 116, 52, 24, '#10131F')],
      '#9DF0C0', line='#9DF0C0', pupil='#10131F', sclera='#FFFFFF',
      mouth_y=190, paw='#4C508F', paw_line='#9DF0C0'),
    P('erikwang2013/encryptable', 'erikwang2013/encryptable/docs/pet.svg', 'Locky',
      (132, 188, 184), 10.5,
      [E(160, 199, 42, 34, '#E8EDFF')],
      '#1E1B4B', paw='#E8EDFF', paw_line='#1E1B4B'),
    P('erikwang2013/encryption', 'erikwang2013/encryption/docs/mascot.svg', 'Locky',
      (96, 144, 158), 13,
      [E(120, 172, 46, 36, '#3B4EDB')],
      '#FFFFFF', line='#312E81', pupil='#0F172A',
      paw='#3B4EDB', paw_line='#312E81'),
    P('erikwang2013/etcd', 'erikwang2013/etcd/docs/pet.svg', 'Etchy',
      (208, 304, 290), 32,
      [E(256, 316, 80, 50, 'url(#body)')],
      '#10243A', mouth_y=338, blush='#FF8FA3',
      paw='#3B82F6', paw_line='#10243A'),
    P('erikwang2013/hashids', 'erikwang2013/hashids/docs/mascot.svg', '哈希迪 Hashy',
      (91, 129, 110), 14,
      [E(110, 122, 36, 28, '#FFFFFF')],
      '#0F172A', paw='#FFFFFF', paw_line='#0F172A'),
    P('erikwang2013/jwt-webman', 'erikwang2013/jwt-webman/docs/pet.svg', '钥匙小卫 Kee',
      (102, 138, 86), 6.5,
      [E(120, 95, 28, 22, '#F7AC15')],
      '#1F2937', paw='#F7AC15', paw_line='#1F2937'),
    P('erikwang2013/poster-php', 'erikwang2013/poster-php/assets/pet.svg', 'Posty',
      (126, 174, 128), 10,
      [E(150, 141, 37, 30, '#FFFDF8')],
      '#2D3436', paw='#FFFDF8', paw_line='#2D3436'),
    P('erikwang2013/season', 'erikwang2013/season/docs/mascot.svg', 'Seasony 季灵',
      (126, 174, 124), 7,
      [E(150, 135, 50, 40, 'url(#g-spring)')],
      '#22313A', blush='#FF7A90', paw='#8CC5A0', paw_line='#22313A'),
    P('erikwang2013/security-php', 'erikwang2013/security-php/docs/mascot.svg', '小盾',
      (76, 124, 84), 11,
      [E(100, 100, 40, 32, '#3B82F6')],
      '#12305F', paw='#3B82F6', paw_line='#12305F'),
    P('erikwang2013/snowflake-php', 'erikwang2013/snowflake-php/docs/i18n/img/en/pet.svg', '雪花精灵',
      (145, 175, 145), 5,
      [E(160, 152, 26, 20, '#FFFFFF')],
      '#0F1E33', paw='#FFFFFF', paw_line='#0F1E33'),
    P('erikwang2013/webman-scout', 'erikwang2013/webman-scout/docs/images/pet.svg', 'Sniffy',
      (126, 194, 138), 11.5,
      [E(160, 150, 58, 44, '#F0B37E')],
      '#2B3038', blush='#EF8F6B', paw='#F0B37E', paw_line='#2B3038'),
    P('erikwang2013/xhprof', 'erikwang2013/xhprof/resource/xhpy.svg', 'Xhpy',
      (216, 296, 300), 15,
      [E(256, 310, 62, 48, 'url(#body)')],
      '#4A1D0D', blush='#F693A6', paw='#FF9438', paw_line='#4A1D0D'),
    P('erikwang2013/xhprof-webman', 'erikwang2013/xhprof-webman/docs/images/pet.svg', '焰焰',
      (103, 135, 159), 9,
      [E(120, 168, 32, 26, 'url(#core)')],
      '#24292F', blush='#FF9B9B', paw='#EF5350', paw_line='#24292F'),
    # ---- pre-existing expression systems: do not touch ------------------
    P('bag/opi', 'bag/opi/docs/opi-pet.svg', '小欧', (0, 0, 0), 10, [], '#000',
      skip=True, note='all 12 forms already exist (docs/opi-pet-forms.svg)'),
    P('oss', 'oss/docs/assets/mascot.svg', '吞吞', (0, 0, 0), 10, [], '#000',
      skip=True, note='existing expression sheet (docs/assets/mascot-expressions.svg)'),
    P('package-tools', 'package-tools/docs/assets/pax.svg', 'Pax', (0, 0, 0), 10, [], '#000',
      skip=True, note='existing mood generator (tools/build-pax.mjs)'),
]

# ---------------------------------------------------------------------------
# Base SVG cleanup
# ---------------------------------------------------------------------------

def _drop_braced(css: str, head_re: str) -> str:
    out, i = [], 0
    while True:
        m = re.search(head_re, css[i:], re.I)
        if not m:
            out.append(css[i:]); break
        s = i + m.start(); out.append(css[i:s])
        j = i + m.end(); depth = 1
        while j < len(css) and depth:
            if css[j] == '{': depth += 1
            elif css[j] == '}': depth -= 1
            j += 1
        i = j
    return ''.join(out)

def clean_css(css: str) -> str:
    css = _drop_braced(css, r'@(?:-webkit-)?keyframes\s+[\w-]+\s*\{')
    css = _drop_braced(css, r'@media\s*\([^)]*prefers-reduced-motion[^)]*\)\s*\{')
    css = re.sub(r'(?m)(?:-webkit-)?animation(?:-[a-z-]+)?\s*:[^;}]*;?', '', css)
    css = re.sub(r'(?m)transition(?:-[a-z-]+)?\s*:[^;}]*;?', '', css)
    css = re.sub(r'(?m)will-change\s*:[^;}]*;?', '', css)
    return css

def sanitize(inner: str) -> str:
    inner = re.sub(r'<!--.*?-->', '', inner, flags=re.S)
    inner = re.sub(r'<\?.*?\?>', '', inner, flags=re.S)
    inner = re.sub(r'<!DOCTYPE.*?>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'<title\b[^>]*>.*?</title>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'<desc\b[^>]*>.*?</desc>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'<metadata\b[^>]*>.*?</metadata>', '', inner, flags=re.S | re.I)
    # strip SMIL
    for tag in ('animateTransform', 'animateMotion', 'animate', 'set'):
        inner = re.sub(rf'<{tag}\b[^>]*/>', '', inner, flags=re.S)
        inner = re.sub(rf'<{tag}\b[^>]*>.*?</{tag}>', '', inner, flags=re.S)
    # clean style blocks, keep visual rules
    def style_repl(m):
        css = clean_css(m.group(1)).strip()
        return f'<style>{css}</style>' if css else ''
    inner = re.sub(r'<style\b[^>]*>(.*?)</style>', style_repl, inner, flags=re.S | re.I)
    return inner.strip()

def parse_base(path: str):
    txt = Path(path).read_text(encoding='utf-8', errors='replace')
    m = re.search(r'<svg\b[^>]*>(.*)</svg>', txt, re.S | re.I)
    if not m:
        raise ValueError(f'not an svg: {path}')
    inner = m.group(1)
    head = re.search(r'<svg\b[^>]*>', txt, re.S | re.I).group(0)
    vm = re.search(r'viewBox\s*=\s*"([^"]+)"', head) or re.search(r"viewBox\s*=\s*'([^']+)'", head)
    if not vm:
        raise ValueError(f'no viewBox: {path}')
    vb = [float(x) for x in re.findall(r'-?\d*\.?\d+', vm.group(1))[:4]]
    return vb, sanitize(inner)

# ---------------------------------------------------------------------------
# Expression drawing
# ---------------------------------------------------------------------------

def heart(cx, cy, r, color, cls=None, delay=0):
    d = (f'M {n(cx)},{n(cy+0.38*r)} '
         f'C {n(cx-1.02*r)},{n(cy-0.40*r)} {n(cx-0.58*r)},{n(cy-1.12*r)} {n(cx)},{n(cy-0.48*r)} '
         f'C {n(cx+0.58*r)},{n(cy-1.12*r)} {n(cx+1.02*r)},{n(cy-0.40*r)} {n(cx)},{n(cy+0.38*r)} Z')
    a = f' class="{cls}" style="animation-delay:{delay}s"' if cls else ''
    return f'<path{a} d="{d}" fill="{color}"/>'

def star(cx, cy, r, color, cls=None, delay=0):
    d = (f'M {n(cx)},{n(cy-r)} L {n(cx+0.28*r)},{n(cy-0.28*r)} L {n(cx+r)},{n(cy)} '
         f'L {n(cx+0.28*r)},{n(cy+0.28*r)} L {n(cx)},{n(cy+r)} L {n(cx-0.28*r)},{n(cy+0.28*r)} '
         f'L {n(cx-r)},{n(cy)} L {n(cx-0.28*r)},{n(cy-0.28*r)} Z')
    a = f' class="{cls}" style="animation-delay:{delay}s"' if cls else ''
    return f'<path{a} d="{d}" fill="{color}"/>'

def tear(cx, cy, r, color='#7CC4F8', cls='ex-anim-tear', delay=0):
    d = (f'M {n(cx)},{n(cy-r*1.5)} C {n(cx+r*0.75)},{n(cy-r*0.3)} {n(cx+r*0.75)},{n(cy+r*0.8)} '
         f'{n(cx)},{n(cy+r*0.8)} C {n(cx-r*0.75)},{n(cy+r*0.8)} {n(cx-r*0.75)},{n(cy-r*0.3)} '
         f'{n(cx)},{n(cy-r*1.5)} Z')
    return (f'<g transform="translate(0 0)"><path class="{cls}" '
            f'style="animation-delay:{delay}s" d="{d}" fill="{color}"/>'
            f'<circle cx="{n(cx)}" cy="{n(cy-r*0.35)}" r="{n(r*0.22)}" fill="#FFFFFF" opacity=".8"/></g>')

def cloud(cx, cy, w, color='#93A3B8'):
    h = w * 0.38
    return (f'<g class="ex-anim-drift">'
            f'{CIR(cx-w*0.32, cy+h*0.12, w*0.22, color)}'
            f'{CIR(cx-w*0.05, cy-h*0.10, w*0.30, color)}'
            f'{CIR(cx+w*0.28, cy+h*0.10, w*0.20, color)}'
            f'{R(cx-w*0.45, cy+h*0.02, w*0.90, h*0.42, h*0.21, color)}'
            f'</g>')

def rain(cx, cy, w, color='#7CC4F8'):
    out = []
    for i, dx in enumerate((-0.30, -0.10, 0.10, 0.30)):
        x = cx + dx * w
        y = cy + w * 0.05
        out.append(f'<g transform="translate({n(x)} {n(y)})"><path class="ex-anim-rain" '
                   f'style="animation-delay:{i*0.22}s" d="M 0 0 L -2 12" stroke="{color}" '
                   f'stroke-width="{n(max(1.2,w*0.035))}" stroke-linecap="round"/></g>')
    return ''.join(out)

def sweat(cx, cy, r, color='#6FB2F0'):
    return tear(cx, cy, r*0.8, color, 'ex-anim-sweat', 0.2)

def steam(cx, cy, r, color='#D7DEE8'):
    out = []
    for i, (dx, dy, rr) in enumerate(((-0.5, 0.0, 0.55), (0.0, -0.35, 0.7), (0.5, 0.05, 0.5))):
        out.append(f'<g transform="translate({n(cx+dx*r)} {n(cy+dy*r)})">'
                   f'<circle class="ex-anim-steam" style="animation-delay:{i*0.28}s" '
                   f'r="{n(rr*r)}" fill="{color}" opacity=".72"/></g>')
    return ''.join(out)

def vein(cx, cy, r, color='#EF4444'):
    d = (f'M {n(cx)},{n(cy-r)} L {n(cx+0.24*r)},{n(cy-0.24*r)} L {n(cx+r)},{n(cy)} '
         f'L {n(cx+0.24*r)},{n(cy+0.24*r)} L {n(cx)},{n(cy+r)} '
         f'L {n(cx-0.24*r)},{n(cy+0.24*r)} L {n(cx-r)},{n(cy)} '
         f'L {n(cx-0.24*r)},{n(cy-0.24*r)} Z')
    return f'<g class="ex-anim-pulse"><path d="{d}" fill="{color}"/></g>'

def confetti(cx, cy, w):
    cols = ['#FF6B9D', '#FFD166', '#4FA3FF', '#5FBF9F', '#9B7BFF', '#F97316']
    out = []
    for i in range(10):
        a = (i * 2 * math.pi / 10) + 0.3
        x = cx + math.cos(a) * w * (0.55 + (i % 3) * 0.10)
        y = cy + math.sin(a) * w * 0.45
        c = cols[i % len(cols)]
        if i % 2:
            out.append(f'<g transform="translate({n(x)} {n(y)})"><rect class="ex-anim-confetti" '
                       f'style="animation-delay:{i*0.16}s" x="{n(-w*0.025)}" y="{n(-w*0.05)}" '
                       f'width="{n(w*0.05)}" height="{n(w*0.10)}" rx="{n(w*0.015)}" fill="{c}"/></g>')
        else:
            out.append(f'<g transform="translate({n(x)} {n(y)})"><circle class="ex-anim-confetti" '
                       f'style="animation-delay:{i*0.16}s" r="{n(w*0.035)}" fill="{c}"/></g>')
    return ''.join(out)

def knock_fx(cx, cy, r, paw, line):
    x = cx + r * 1.9
    out = [f'<g transform="translate({n(x)} {n(cy)})"><g class="ex-anim-knock">'
           f'<rect x="{n(-r*0.55)}" y="{n(-r*0.45)}" width="{n(r*0.9)}" height="{n(r*0.9)}" '
           f'rx="{n(r*0.3)}" fill="{paw}" stroke="{line}" stroke-width="{n(max(1.3,r*0.10))}"/>'
           f'<path d="M {n(-r*0.25)},{n(-r*0.12)} L {n(-r*0.25)},{n(r*0.15)} M 0,{n(-r*0.18)} L 0,{n(r*0.15)} M {n(r*0.25)},{n(-r*0.12)} L {n(r*0.25)},{n(r*0.15)}" '
           f'stroke="{line}" stroke-width="{n(max(1,r*0.06))}" stroke-linecap="round"/>'
           f'</g></g>']
    for i, dy in enumerate((-0.55, 0.0, 0.55)):
        out.append(f'<g transform="translate({n(x-r*0.85)} {n(cy+dy*r)})">'
                   f'<path class="ex-anim-knockline" style="animation-delay:{i*0.12}s" '
                   f'd="M 0 0 L {n(-r*0.55)} 0" stroke="{ACCENT["knocking"]}" '
                   f'stroke-width="{n(max(1.2,r*0.09))}" stroke-linecap="round"/></g>')
    return ''.join(out)

def palm(cx, cy, r, paw, line):
    out = [f'<g transform="translate({n(cx)} {n(cy)}) rotate(12)">'
           f'<rect class="ex-anim-palm" x="{n(-r*0.75)}" y="{n(-r*1.05)}" width="{n(r*1.5)}" '
           f'height="{n(r*2.0)}" rx="{n(r*0.55)}" fill="{paw}" stroke="{line}" '
           f'stroke-width="{n(max(1.4,r*0.09))}"/>']
    for dx in (-0.36, 0.0, 0.36):
        out.append(f'<path class="ex-anim-palm" d="M {n(dx*r)},{n(-r*0.75)} L {n(dx*r)},{n(-r*0.10)}" '
                   f'stroke="{line}" stroke-width="{n(max(1,r*0.055))}" stroke-linecap="round" opacity=".55"/>')
    out.append('</g>')
    return ''.join(out)

def hands(cx, cy, r, paw, line):
    out = []
    for s in (-1, 1):
        x = cx + s * r * 0.55
        out.append(f'<g transform="translate({n(x)} {n(cy)}) rotate({-s*18})">'
                   f'<g class="ex-anim-please">'
                   f'<ellipse rx="{n(r*0.42)}" ry="{n(r*0.62)}" fill="{paw}" stroke="{line}" '
                   f'stroke-width="{n(max(1.1,r*0.07))}"/>'
                   f'<path d="M 0,{n(-r*0.35)} L 0,{n(r*0.30)}" stroke="{line}" '
                   f'stroke-width="{n(max(1,r*0.05))}" stroke-linecap="round" opacity=".5"/>'
                   f'</g></g>')
    return ''.join(out)

def aura(cx, cy, r, color):
    return (f'<circle class="ex-anim-pulse" cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" '
            f'fill="none" stroke="{color}" stroke-width="{n(max(2,r*0.09))}" '
            f'opacity=".35"/>')

def draw_eye(cfg, i, mode='open', pupil_shift=(0, 0), big=False):
    ex, ey = (cfg['e1'] if i == 0 else cfg['e2'])
    r = cfg['r']
    rx, ry = r, r * 1.14
    if mode == 'wide':
        rx, ry = r * 1.12, r * 1.38
    elif mode == 'narrow':
        ry = r * 0.66
    elif mode == 'droop':
        ry = r * 0.92
    sw = max(1.3, r * 0.16)
    if mode in ('happy', 'sad'):
        w = r * 0.95
        if mode == 'happy':
            d = (f'M {n(ex-w)},{n(ey+r*0.28)} Q {n(ex)},{n(ey-r*1.15)} '
                 f'{n(ex+w)},{n(ey+r*0.28)}')
        else:
            d = (f'M {n(ex-w)},{n(ey-r*0.20)} Q {n(ex)},{n(ey+r*1.10)} '
                 f'{n(ex+w)},{n(ey-r*0.20)}')
        return (f'<path d="{d}" fill="none" stroke="{cfg["ink"]}" '
                f'stroke-width="{n(max(1.8, r*0.20))}" stroke-linecap="round"/>')
    if mode == 'heart':
        return heart(ex, ey, r*1.05, ACCENT['coquettish'], 'ex-anim-pulse')
    if mode == 'star':
        return star(ex, ey, r*1.18, ACCENT['cute'], 'ex-anim-spark')
    if mode == 'spiral':
        return (f'<circle cx="{n(ex)}" cy="{n(ey)}" r="{n(rx)}" fill="{cfg["sclera"]}" '
                f'stroke="{cfg["line"]}" stroke-width="{n(sw)}"/>'
                f'<circle cx="{n(ex)}" cy="{n(ey)}" r="{n(rx*0.55)}" fill="none" '
                f'stroke="{cfg["pupil"]}" stroke-width="{n(sw*0.8)}"/>'
                f'<circle cx="{n(ex)}" cy="{n(ey)}" r="{n(rx*0.20)}" fill="{cfg["pupil"]}"/>')
    # sclera eye
    px = ex + pupil_shift[0] * r
    py = ey + pupil_shift[1] * r
    prx, pry = rx * (0.48 if not big else 0.58), ry * (0.55 if not big else 0.64)
    out = [f'<ellipse cx="{n(ex)}" cy="{n(ey)}" rx="{n(rx)}" ry="{n(ry)}" '
           f'fill="{cfg["sclera"]}" stroke="{cfg["line"]}" stroke-width="{n(sw)}"/>',
           f'<ellipse cx="{n(px)}" cy="{n(py)}" rx="{n(prx)}" ry="{n(pry)}" '
           f'fill="{cfg["pupil"]}"/>',
           f'<circle cx="{n(px-rx*0.22)}" cy="{n(py-ry*0.28)}" r="{n(rx*0.20)}" fill="#FFFFFF"/>']
    if big:
        out.append(f'<circle cx="{n(px+rx*0.24)}" cy="{n(py+ry*0.30)}" r="{n(rx*0.10)}" fill="#FFFFFF" opacity=".9"/>')
    if mode == 'droop':
        out.append(f'<path d="M {n(ex-rx)},{n(ey-ry*0.35)} Q {n(ex)},{n(ey-ry*1.0)} '
                   f'{n(ex+rx)},{n(ey-ry*0.35)}" fill="none" stroke="{cfg["ink"]}" '
                   f'stroke-width="{n(sw*1.15)}" stroke-linecap="round"/>')
    return ''.join(out)

def draw_brows(cfg, kind):
    r = cfg['r']
    x1, y1 = cfg['e1']; x2, y2 = cfg['e2']
    sw = max(1.6, r * 0.14)
    if kind == 'angry':
        return (f'<path d="M {n(x1-r*0.95)},{n(y1-r*1.55)} L {n(x1+r*0.55)},{n(y1-r*0.95)}" '
                f'stroke="{cfg["ink"]}" stroke-width="{n(sw*1.25)}" stroke-linecap="round"/>'
                f'<path d="M {n(x2+r*0.95)},{n(y2-r*1.55)} L {n(x2-r*0.55)},{n(y2-r*0.95)}" '
                f'stroke="{cfg["ink"]}" stroke-width="{n(sw*1.25)}" stroke-linecap="round"/>')
    if kind == 'sad':
        return (f'<path d="M {n(x1-r*0.95)},{n(y1-r*1.0)} L {n(x1+r*0.55)},{n(y1-r*1.6)}" '
                f'stroke="{cfg["ink"]}" stroke-width="{n(sw)}" stroke-linecap="round"/>'
                f'<path d="M {n(x2+r*0.95)},{n(y2-r*1.0)} L {n(x2-r*0.55)},{n(y2-r*1.6)}" '
                f'stroke="{cfg["ink"]}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'raised':
        return (f'<path d="M {n(x1-r*0.85)},{n(y1-r*1.55)} Q {n(x1)},{n(y1-r*1.95)} {n(x1+r*0.85)},{n(y1-r*1.55)}" '
                f'fill="none" stroke="{cfg["ink"]}" stroke-width="{n(sw)}" stroke-linecap="round"/>'
                f'<path d="M {n(x2-r*0.85)},{n(y2-r*1.55)} Q {n(x2)},{n(y2-r*1.95)} {n(x2+r*0.85)},{n(y2-r*1.55)}" '
                f'fill="none" stroke="{cfg["ink"]}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    return ''

def draw_mouth(cfg, kind):
    r = cfg['r']
    mx = (cfg['e1'][0] + cfg['e2'][0]) / 2
    my = cfg['mouth_y'] if cfg['mouth_y'] is not None else (cfg['e1'][1] + cfg['e2'][1]) / 2 + r * 2.2
    dx = abs(cfg['e2'][0] - cfg['e1'][0])
    w = max(r * 2.3, dx * 0.44)
    h = max(r * 0.72, w * 0.22)
    sw = max(1.7, r * 0.16)
    col = cfg['mouth_color']
    fill = cfg['mouth_fill']
    if kind == 'smile':
        return (f'<path d="M {n(mx-w/2)},{n(my)} Q {n(mx)},{n(my+h*1.5)} {n(mx+w/2)},{n(my)}" '
                f'fill="none" stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'smile_small':
        return (f'<path d="M {n(mx-w*0.30)},{n(my)} Q {n(mx)},{n(my+h*1.1)} {n(mx+w*0.30)},{n(my)}" '
                f'fill="none" stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'grin':
        d = (f'M {n(mx-w/2)},{n(my-h*0.25)} Q {n(mx)},{n(my+h*2.3)} {n(mx+w/2)},{n(my-h*0.25)} Z')
        return (f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{n(sw*0.8)}"/>'
                f'<ellipse cx="{n(mx)}" cy="{n(my+h*0.55)}" rx="{n(w*0.22)}" ry="{n(h*0.55)}" fill="#FF6B8A"/>')
    if kind == 'frown':
        return (f'<path d="M {n(mx-w/2)},{n(my)} Q {n(mx)},{n(my-h*1.5)} {n(mx+w/2)},{n(my)}" '
                f'fill="none" stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'wavy':
        pts = [(-0.5, 0), (-0.25, -1), (0.0, 0), (0.25, 1), (0.5, 0)]
        d = f'M {n(mx+w*pts[0][0])},{n(my+h*pts[0][1])}'
        for i in range(1, len(pts)):
            x0, y0 = pts[i-1]; x1, y1 = pts[i]
            d += f' Q {n(mx+w*(x0+x1)/2)},{n(my+h*(y0+y1)*1.4)} {n(mx+w*x1)},{n(my+h*y1)}'
        return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'scream':
        return (f'<ellipse cx="{n(mx)}" cy="{n(my)}" rx="{n(w*0.34)}" ry="{n(h*1.45)}" '
                f'fill="{fill}" stroke="{col}" stroke-width="{n(sw*0.8)}"/>'
                f'<ellipse cx="{n(mx)}" cy="{n(my+h*0.55)}" rx="{n(w*0.18)}" ry="{n(h*0.6)}" fill="#FF6B8A"/>')
    if kind == 'pout':
        return (f'<ellipse cx="{n(mx)}" cy="{n(my)}" rx="{n(w*0.18)}" ry="{n(h*0.55)}" '
                f'fill="none" stroke="{col}" stroke-width="{n(sw)}"/>')
    if kind == 'flat':
        return (f'<path d="M {n(mx-w*0.35)},{n(my)} L {n(mx+w*0.35)},{n(my)}" '
                f'stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    if kind == 'gritted':
        out = [f'<rect x="{n(mx-w/2)}" y="{n(my-h*0.7)}" width="{n(w)}" height="{n(h*1.35)}" '
               f'rx="{n(h*0.28)}" fill="#FFFFFF" stroke="{col}" stroke-width="{n(sw*0.8)}"/>']
        for i in range(1, 5):
            x = mx - w/2 + w*i/5
            out.append(f'<path d="M {n(x)},{n(my-h*0.7)} L {n(x)},{n(my+h*0.65)}" stroke="{col}" '
                       f'stroke-width="{n(max(1,sw*0.45))}" opacity=".55"/>')
        out.append(f'<path d="M {n(mx-w/2)},{n(my)} L {n(mx+w/2)},{n(my)}" stroke="{col}" '
                   f'stroke-width="{n(max(1,sw*0.5))}" opacity=".55"/>')
        return ''.join(out)
    if kind == 'tongue':
        d = (f'M {n(mx-w/2)},{n(my-h*0.25)} Q {n(mx)},{n(my+h*2.1)} {n(mx+w/2)},{n(my-h*0.25)} Z')
        return (f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{n(sw*0.8)}"/>'
                f'<path d="M {n(mx-w*0.17)},{n(my+h*0.55)} Q {n(mx)},{n(my+h*2.4)} {n(mx+w*0.17)},{n(my+h*0.55)} Z" '
                f'fill="#FF5C8A" stroke="{col}" stroke-width="{n(max(1,sw*0.45))}"/>'
                f'<path d="M {n(mx)},{n(my+h*0.7)} L {n(mx)},{n(my+h*1.6)}" stroke="{col}" '
                f'stroke-width="{n(max(1,sw*0.35))}" opacity=".55"/>')
    if kind == 'smirk':
        return (f'<path d="M {n(mx-w*0.42)},{n(my)} Q {n(mx+w*0.05)},{n(my+h*1.2)} {n(mx+w*0.46)},{n(my-h*0.35)}" '
                f'fill="none" stroke="{col}" stroke-width="{n(sw)}" stroke-linecap="round"/>')
    return ''

def draw_blush(cfg, opacity=0.45, cls=None):
    r = cfg['r']
    (x1, y1), (x2, y2) = cfg['e1'], cfg['e2']
    a = f' class="{cls}"' if cls else ''
    return (f'<ellipse{a} cx="{n(x1-r*0.75)}" cy="{n(y1+r*1.35)}" rx="{n(r*0.78)}" ry="{n(r*0.42)}" '
            f'fill="{cfg["blush"]}" opacity="{opacity}"/>'
            f'<ellipse{a} cx="{n(x2+r*0.75)}" cy="{n(y2+r*1.35)}" rx="{n(r*0.78)}" ry="{n(r*0.42)}" '
            f'fill="{cfg["blush"]}" opacity="{opacity}"/>')

def face_svg(cfg, mood):
    """Patch + expression + effects in absolute user coordinates."""
    r = cfg['r']
    x1, y1 = cfg['e1']; x2, y2 = cfg['e2']
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    fw = abs(x2 - x1) + r * 2.6
    my = cfg['mouth_y'] if cfg['mouth_y'] is not None else cy + r * 2.2
    out = [f'<g class="ex-face">']
    out += cfg['patches']
    if cfg.get('decor'):
        out.append(cfg['decor'])
    mood = mood
    # eyes / brows / mouth
    if mood in ('smile',):
        out += [draw_eye(cfg, 0, 'happy'), draw_eye(cfg, 1, 'happy')]
        out += [draw_mouth(cfg, 'smile'), draw_blush(cfg, .5)]
        out += [star(cx-fw*.62, cy-fw*.35, r*.55, ACCENT[mood], 'ex-anim-spark', 0.0),
                star(cx+fw*.58, cy-fw*.48, r*.42, ACCENT[mood], 'ex-anim-spark', 0.5)]
    elif mood == 'joy':
        out += [draw_eye(cfg, 0, 'happy'), draw_eye(cfg, 1, 'happy')]
        out += [draw_mouth(cfg, 'grin'), draw_blush(cfg, .6, 'ex-anim-pulse')]
        out += [confetti(cx, cy-fw*.10, fw*.85)]
    elif mood == 'cry':
        out += [draw_brows(cfg, 'sad'), draw_eye(cfg, 0, 'sad'), draw_eye(cfg, 1, 'sad')]
        out += [draw_mouth(cfg, 'wavy'), draw_blush(cfg, .25)]
        out += [tear(x1, y1+r*1.1, r*.55, '#7CC4F8', 'ex-anim-tear', 0.0),
                tear(x2, y2+r*1.1, r*.55, '#7CC4F8', 'ex-anim-tear', 0.55)]
        out += [tear(x1-r*.1, y1+r*1.5, r*.35, '#A8D8FB', 'ex-anim-tear', 0.9),
                tear(x2+r*.1, y2+r*1.5, r*.35, '#A8D8FB', 'ex-anim-tear', 1.35)]
    elif mood == 'depressed':
        out += [draw_brows(cfg, 'sad'), draw_eye(cfg, 0, 'droop'), draw_eye(cfg, 1, 'droop')]
        out += [draw_mouth(cfg, 'frown'), draw_blush(cfg, .18)]
        out += [cloud(cx, cy-fw*.62, fw*.55), rain(cx, cy-fw*.34, fw*.55)]
    elif mood == 'terrified':
        out += [draw_brows(cfg, 'raised'), draw_eye(cfg, 0, 'wide'), draw_eye(cfg, 1, 'wide')]
        out += [draw_mouth(cfg, 'scream')]
        out += [sweat(x2+r*1.35, y2-r*.75, r*.7),
                sweat(x2+r*1.8, y2+r*.1, r*.5)]
        out += [aura(cx, cy, fw*.62, ACCENT[mood])]
        for i, (dx, dy, a) in enumerate(((-.62,-.45,-25),(.62,-.45,25),(-.66,.25,-12),(.66,.25,12))):
            x, y = cx+dx*fw, cy+dy*fw
            out.append(f'<g transform="translate({n(x)} {n(y)}) rotate({a})">'
                       f'<path class="ex-anim-shock" style="animation-delay:{i*.08}s" d="M 0 0 L {n(r*.55)} 0" '
                       f'stroke="{ACCENT[mood]}" stroke-width="{n(max(1.5,r*.14))}" stroke-linecap="round"/></g>')
    elif mood == 'angry':
        out += [draw_brows(cfg, 'angry'), draw_eye(cfg, 0, 'narrow'), draw_eye(cfg, 1, 'narrow')]
        out += [draw_mouth(cfg, 'gritted')]
        out += [vein(cx+fw*.46, cy-fw*.34, r*.8),
                steam(cx, cy-fw*.55, r*.65)]
        out += [aura(cx, cy, fw*.60, ACCENT[mood])]
    elif mood == 'coquettish':
        out += [draw_eye(cfg, 0, 'happy'), draw_eye(cfg, 1, 'heart')]
        out += [draw_mouth(cfg, 'pout'), draw_blush(cfg, .7, 'ex-anim-pulse')]
        out += [heart(cx-fw*.48, cy-fw*.42, r*.7, ACCENT[mood], 'ex-anim-heart', 0.0),
                heart(cx+fw*.52, cy-fw*.52, r*.55, ACCENT[mood], 'ex-anim-heart', 0.7),
                heart(cx+fw*.36, cy-fw*.22, r*.38, ACCENT[mood], 'ex-anim-heart', 1.3)]
    elif mood == 'cute':
        out += [draw_eye(cfg, 0, 'open', big=True), draw_eye(cfg, 1, 'open', big=True)]
        out += [draw_mouth(cfg, 'smile_small'), draw_blush(cfg, .65, 'ex-anim-pulse')]
        out += [star(cx-fw*.56, cy-fw*.40, r*.6, ACCENT[mood], 'ex-anim-spark', 0.0),
                star(cx+fw*.54, cy-fw*.52, r*.5, ACCENT[mood], 'ex-anim-spark', 0.4),
                star(cx+fw*.60, cy-fw*.12, r*.34, ACCENT[mood], 'ex-anim-spark', 0.8)]
    elif mood == 'pleasing':
        out += [draw_brows(cfg, 'sad'),
                draw_eye(cfg, 0, 'open', pupil_shift=(0, -.22), big=True),
                draw_eye(cfg, 1, 'open', pupil_shift=(0, -.22), big=True)]
        out += [draw_mouth(cfg, 'smile_small'), draw_blush(cfg, .55)]
        out += [sweat(x2+r*1.4, y2-r*.9, r*.55),
                star(cx-fw*.50, cy-fw*.38, r*.35, ACCENT[mood], 'ex-anim-spark', 0.3),
                star(cx+fw*.52, cy-fw*.30, r*.30, ACCENT[mood], 'ex-anim-spark', 0.8),
                hands(cx, my+r*1.05, r*.75, cfg['paw'], cfg['paw_line'])]
    elif mood == 'knocking':
        out += [draw_brows(cfg, 'angry'),
                draw_eye(cfg, 0, 'narrow'), draw_eye(cfg, 1, 'happy')]
        out += [draw_mouth(cfg, 'flat')]
        out += [knock_fx(cx, cy, r, cfg['paw'], cfg['paw_line']),
                steam(cx-fw*.38, cy-fw*.45, r*.45)]
    elif mood == 'facepalm':
        out += [draw_eye(cfg, 0, 'sad')]
        out += [draw_mouth(cfg, 'wavy'), draw_blush(cfg, .7)]
        out += [palm(x2+r*.15, y2+r*.15, r*1.15, cfg['paw'], cfg['paw_line'])]
        out += [steam(cx-fw*.40, cy-fw*.48, r*.6),
                sweat(x2+r*1.45, y2-r*.9, r*.5)]
    elif mood == 'tongue':
        out += [draw_eye(cfg, 0, 'open'), draw_eye(cfg, 1, 'happy')]
        out += [draw_mouth(cfg, 'tongue'), draw_blush(cfg, .55)]
        out += [star(cx-fw*.52, cy-fw*.40, r*.40, ACCENT[mood], 'ex-anim-spark', 0.2)]
    out.append('</g>')
    return ''.join(out)

# ---------------------------------------------------------------------------
# Whole-file composition
# ---------------------------------------------------------------------------

MOTION = {
    'smile': ('bob', 3.2, 'translateY(0)', 'translateY(-{a}px)'),
    'joy': ('bounce', 1.15, 'translateY(0)', 'translateY(-{a2}px)'),
    'cry': ('sob', 0.9, 'translateY(0)', 'translateY({a}px)'),
    'depressed': ('slump', 4.2, 'translateY(0)', 'translateY({a}px)'),
    'terrified': ('tremble', 0.18, 'translate(0,0)', 'translate(-{a}px,{ah}px)'),
    'angry': ('shake', 0.24, 'translateX(0)', 'translateX(-{a2}px)'),
    'coquettish': ('sway', 2.4, 'rotate(0deg)', 'rotate(-2.5deg)'),
    'cute': ('hop', 1.5, 'translateY(0) rotate(0)', 'translateY(-{a}px) rotate(2deg)'),
    'pleasing': ('nod', 1.7, 'translateY(0)', 'translateY({a}px)'),
    'knocking': ('tap', 0.55, 'translateY(0)', 'translateY({ah}px)'),
    'facepalm': ('headshake', 0.9, 'rotate(0deg)', 'rotate(-2deg)'),
    'tongue': ('sway', 2.0, 'rotate(0deg)', 'rotate(3deg)'),
}

def css_for(mood, r):
    a = max(1.6, r * 0.32)
    a2 = a * 1.7
    ah = a * 0.55
    name, dur, start, mid = MOTION[mood]
    mid = mid.format(a=n(a), a2=n(a2), ah=n(ah))
    if mood == 'joy':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'35% {{ transform: {mid}; }} 55% {{ transform: translateY(-{n(a*0.5)}px); }} '
              f'75% {{ transform: translateY(0); }} }}')
    elif mood == 'angry':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'20% {{ transform: {mid}; }} 40% {{ transform: translateX({n(a2)}px); }} '
              f'60% {{ transform: translateX(-{n(a*1.1)}px); }} 80% {{ transform: translateX({n(a*.7)}px); }} }}')
    elif mood == 'terrified':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'25% {{ transform: {mid}; }} 50% {{ transform: translate({n(a)}px,{n(-ah)}px); }} '
              f'75% {{ transform: translate(-{n(a*.8)}px,{n(ah)}px); }} }}')
    elif mood == 'cry':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'50% {{ transform: {mid}; }} }}')
    elif mood == 'facepalm':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'25% {{ transform: {mid}; }} 75% {{ transform: rotate(2deg); }} }}')
    elif mood == 'knocking':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'25% {{ transform: {mid}; }} 32% {{ transform: translateY(0); }} }}')
    elif mood == 'pleasing':
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'50% {{ transform: {mid}; }} }}')
    elif mood in ('coquettish', 'tongue'):
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'50% {{ transform: {mid}; }} }}')
    else:
        kf = (f'@keyframes ex-{name} {{ 0%,100% {{ transform: {start}; }} '
              f'50% {{ transform: {mid}; }} }}')
    return f'''<style>
.ex-motion {{ animation: ex-{name} {dur}s ease-in-out infinite; transform-box: fill-box; transform-origin: 50% 50%; }}
.ex-anim-tear {{ animation: ex-tear 1.8s ease-in infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-sweat {{ animation: ex-tear 1.5s ease-in infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-heart {{ animation: ex-heart 2.2s ease-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-spark {{ animation: ex-spark 1.9s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-rain {{ animation: ex-rain 1.4s linear infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-confetti {{ animation: ex-confetti 2.4s linear infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-pulse {{ animation: ex-pulse 1.6s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-knock {{ animation: ex-knock 0.55s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-knockline {{ animation: ex-knockline 0.55s ease-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-palm {{ animation: ex-palm 0.9s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-steam {{ animation: ex-steam 1.8s ease-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-shock {{ animation: ex-shock 0.5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-please {{ animation: ex-please 1.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
.ex-anim-drift {{ animation: ex-drift 4.5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
{kf}
@keyframes ex-tear {{ 0% {{ transform: translateY(0); opacity: 0; }} 18% {{ opacity: 1; }} 100% {{ transform: translateY({n(max(8,r*1.1))}px); opacity: 0; }} }}
@keyframes ex-heart {{ 0% {{ transform: translateY(0) scale(.65); opacity: 0; }} 20% {{ opacity: 1; }} 100% {{ transform: translateY(-{n(max(10,r*1.8))}px) scale(1.15); opacity: 0; }} }}
@keyframes ex-spark {{ 0%,100% {{ transform: scale(.6) rotate(0deg); opacity: .3; }} 50% {{ transform: scale(1.15) rotate(25deg); opacity: 1; }} }}
@keyframes ex-rain {{ 0% {{ transform: translateY(0); opacity: 0; }} 20% {{ opacity: 1; }} 100% {{ transform: translateY({n(max(8,r*1.2))}px); opacity: 0; }} }}
@keyframes ex-confetti {{ 0% {{ transform: translateY(-{n(max(4,r*.35))}px) rotate(0deg); opacity: 1; }} 100% {{ transform: translateY({n(max(14,r*1.6))}px) rotate(200deg); opacity: 0; }} }}
@keyframes ex-pulse {{ 0%,100% {{ transform: scale(1); opacity: .35; }} 50% {{ transform: scale(1.18); opacity: .7; }} }}
@keyframes ex-knock {{ 0%,100% {{ transform: translateX({n(max(3,r*.45))}px); }} 35% {{ transform: translateX(0); }} }}
@keyframes ex-knockline {{ 0%,100% {{ transform: scaleX(.6); opacity: .35; }} 35% {{ transform: scaleX(1); opacity: 1; }} }}
@keyframes ex-palm {{ 0%,100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-{n(max(1,r*.12))}px) rotate(-4deg); }} }}
@keyframes ex-steam {{ 0% {{ transform: translateY(0); opacity: .7; }} 100% {{ transform: translateY(-{n(max(7,r*.9))}px); opacity: 0; }} }}
@keyframes ex-shock {{ 0%,100% {{ transform: scaleX(.7); opacity: .4; }} 50% {{ transform: scaleX(1.25); opacity: 1; }} }}
@keyframes ex-please {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-{n(max(1.5,r*.18))}px); }} }}
@keyframes ex-drift {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-{n(max(1.5,r*.2))}px); }} }}
@media (prefers-reduced-motion: reduce) {{
  .ex-motion, [class*="ex-anim-"] {{ animation: none !important; }}
}}
</style>'''

def build_svg(cfg, mood):
    vb, inner = parse_base(cfg['src'])
    if cfg.get('viewbox'):
        vb = list(cfg['viewbox'])
    w, h = vb[2], vb[3]
    r = cfg['r']
    label = f'{cfg["pet"]} · {MOOD[mood][1]} {MOOD[mood][2]}'
    if cfg['badge']:
        b_r = cfg['badge_r']
        b_cx, b_cy = cfg['badge_cx'], cfg['badge_cy']
        bcfg = dict(cfg)
        bcfg['e1'] = (b_cx - b_r*0.34, b_cy - b_r*0.06)
        bcfg['e2'] = (b_cx + b_r*0.34, b_cy - b_r*0.06)
        bcfg['r'] = b_r * 0.26
        bcfg['patches'] = [CIR(b_cx, b_cy, b_r, '#FFCC4D')]
        bcfg['ink'] = '#5C3A21'; bcfg['line'] = '#5C3A21'; bcfg['pupil'] = '#5C3A21'
        bcfg['sclera'] = '#FFFFFF'; bcfg['mouth_color'] = '#5C3A21'
        bcfg['blush'] = '#FF8FB3'; bcfg['mouth_y'] = b_cy + b_r*0.34
        bcfg['paw'] = '#FFCC4D'; bcfg['paw_line'] = '#5C3A21'
        face = face_svg(bcfg, mood)
        face = (f'<g transform="translate({n(b_cx-b_r*0.5)} {n(b_cy-b_r*0.5)}) scale({n(b_r/100)})">'
                f'<g transform="translate({n(-b_cx+b_r*0.5)} {n(-b_cy+b_r*0.5)})">{face}</g></g>')
        # simpler: badge face drawn directly in user coords, plus a soft ring
        face = (f'<g>{CIR(b_cx,b_cy,b_r+max(2,b_r*.06),"#FFFFFF")}{CIR(b_cx,b_cy,b_r+max(1,b_r*.03),cfg["ink"])}'
                f'{face_svg(bcfg, mood)}</g>')
    else:
        face = face_svg(cfg, mood)
    extra = ''
    if cfg['badge']:
        # a few mood effects around the badge
        bx, by = cfg['badge_cx'], cfg['badge_cy']
        if mood in ('smile', 'cute', 'tongue'):
            extra = (star(bx+cfg['badge_r']*1.15, by-cfg['badge_r']*.9, cfg['badge_r']*.28, ACCENT[mood], 'ex-anim-spark', 0) +
                     star(bx-cfg['badge_r']*1.15, by-cfg['badge_r']*.6, cfg['badge_r']*.22, ACCENT[mood], 'ex-anim-spark', .5))
        elif mood == 'joy':
            extra = confetti(bx, by, cfg['badge_r']*1.5)
        elif mood == 'cry':
            extra = (tear(bx-cfg['badge_r']*.3, by+cfg['badge_r']*.7, cfg['badge_r']*.18, '#7CC4F8', 'ex-anim-tear', 0) +
                     tear(bx+cfg['badge_r']*.3, by+cfg['badge_r']*.7, cfg['badge_r']*.18, '#7CC4F8', 'ex-anim-tear', .5))
        elif mood == 'depressed':
            extra = cloud(bx, by-cfg['badge_r']*1.35, cfg['badge_r']*.9) + rain(bx, by-cfg['badge_r']*.95, cfg['badge_r']*.9)
        elif mood == 'terrified':
            extra = sweat(bx+cfg['badge_r']*1.15, by-cfg['badge_r']*.6, cfg['badge_r']*.22)
        elif mood == 'angry':
            extra = vein(bx+cfg['badge_r']*1.15, by-cfg['badge_r']*.75, cfg['badge_r']*.25)
        elif mood == 'coquettish':
            extra = heart(bx+cfg['badge_r']*1.2, by-cfg['badge_r']*.8, cfg['badge_r']*.22, ACCENT[mood], 'ex-anim-heart', 0)
        elif mood == 'pleasing':
            extra = sweat(bx+cfg['badge_r']*1.1, by-cfg['badge_r']*.5, cfg['badge_r']*.2)
        elif mood == 'knocking':
            extra = knock_fx(bx+cfg['badge_r']*.3, by, cfg['badge_r']*.18, cfg['paw'], cfg['paw_line'])
        elif mood == 'facepalm':
            extra = steam(bx-cfg['badge_r']*.9, by-cfg['badge_r']*.8, cfg['badge_r']*.25)
    css = css_for(mood, r if not cfg['badge'] else cfg['badge_r']*.26)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
           f'viewBox="{n(vb[0])} {n(vb[1])} {n(w)} {n(h)}" width="{n(w)}" height="{n(h)}" '
           f'role="img" aria-label="{esc(label)}">'
           f'<title>{esc(label)}</title>'
           f'<desc>{esc(cfg["pet"])} 的 {MOOD[mood][1]} 表情形态 · animated expression form</desc>'
           f'{css}'
           f'<g class="ex-motion ex-{mood}">'
           f'<g class="ex-base">{inner}</g>'
           f'{face}{extra}'
           f'</g></svg>')
    return svg

# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------

def update_readme(project: Path, pet: str, out_rel: str, moods=MOODS):
    readme = project / 'README.md'
    if not readme.exists():
        return False
    text = readme.read_text(encoding='utf-8', errors='replace')
    if '<!-- pet-expressions:start -->' in text:
        return False
    cells = []
    for slug, zh, en, code in moods:
        rel = f'{out_rel}/{slug}.svg'
        cells.append(f'<td align="center"><img src="{rel}" width="88" alt="{esc(zh)}"><br>'
                     f'<b>{zh}</b><br><code>:{code}:</code></td>')
    rows = ['<tr>' + ''.join(cells[i:i+6]) + '</tr>' for i in range(0, len(cells), 6)]
    block = ('<!-- pet-expressions:start -->\n'
             f'## 项目宠物表情形态 · {pet}\n\n'
             '<table align="center">\n' + '\n'.join(rows) + '\n</table>\n\n'
             '> 12 种彩色动态形态：笑 / 欢乐 / 哭 / 沮丧 / 惊恐 / 愤怒 / 撒娇 / 卖萌 / 讨好 / 敲打 / 捂脸 / 吐舌头。'
             '每个 SVG 自带表情、情绪特效与整体动效，并遵循 `prefers-reduced-motion`。\n'
             '<!-- pet-expressions:end -->\n')
    # insert after the pet section if there is one
    lines = text.splitlines()
    insert_at = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^##\s+', line) and re.search(r'宠物|吉祥物|mascot', line, re.I):
            for j in range(i + 1, len(lines)):
                if re.match(r'^##\s+', lines[j]):
                    insert_at = j
                    break
            break
    new_lines = lines[:insert_at] + ['', block] + lines[insert_at:]
    readme.write_text('\n'.join(new_lines).rstrip() + '\n', encoding='utf-8')
    return True

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*', help='project keys')
    ap.add_argument('--force', action='store_true', help='overwrite existing SVGs')
    ap.add_argument('--no-readme', action='store_true')
    args = ap.parse_args()
    only = set(args.only or [])
    made = skipped = 0
    for cfg in PETS:
        if only and cfg['key'] not in only:
            continue
        if cfg['skip']:
            print(f"skip {cfg['key']}: {cfg['note']}")
            continue
        project = ROOT / cfg['key'] if not cfg['key'].startswith('bag/') else ROOT / cfg['key']
        out_dir = project / cfg['out']
        out_dir.mkdir(parents=True, exist_ok=True)
        for slug, zh, en, code in MOODS:
            target = out_dir / f'{slug}.svg'
            if target.exists() and not args.force:
                skipped += 1
                continue
            svg = build_svg(cfg, slug)
            target.write_text(svg, encoding='utf-8')
            made += 1
        if not args.no_readme:
            update_readme(project, cfg['pet'], cfg['out'])
        print(f"ok {cfg['key']} -> {cfg['out']} ({len(MOODS)} forms)")
    print(f'done: {made} written, {skipped} existing skipped')

if __name__ == '__main__':
    main()
