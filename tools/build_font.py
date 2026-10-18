#!/usr/bin/env python3
"""Build the pet-emoji colour bitmap font (CBDT/CBLC) with shortcode ligatures."""
from __future__ import annotations
import json, struct
from io import BytesIO
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables import C_B_D_T_, C_B_L_C_, E_B_L_C_
from fontTools.ttLib.tables.BitmapGlyphMetrics import SmallGlyphMetrics
from fontTools.ttLib.tables.DefaultTable import DefaultTable
from PIL import Image, ImageDraw, ImageFont

EMOJI = Path('/home/wwwroot/emoji')
BASE_FONT = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
LICENSE = Path('/usr/share/doc/fonts-dejavu-core/copyright')
PPEM = 128

def glyph_name(entry):
    return 'pet_' + entry['project_slug'].replace('-', '_') + '_' + entry['mood']

def main():
    manifest = json.loads((EMOJI / 'emoji.json').read_text(encoding='utf-8'))
    entries = manifest['emojis']
    font = TTFont(BASE_FONT)
    chars = ':abcdefghijklmnopqrstuvwxyz- '
    opts = subset.Options()
    opts.glyph_names = True
    opts.notdef_outline = True
    opts.recommended_glyphs = False
    ss = subset.Subsetter(opts)
    ss.populate(text=chars)
    ss.subset(font)
    for t in ('GSUB', 'GPOS', 'GDEF', 'kern', 'MATH'):
        if t in font:
            del font[t]
    print('subset done', flush=True)
    name = font['name']
    for nid, val in ((1, 'Pet Emoji Atlas'), (2, 'Regular'), (3, 'PetEmojiAtlas-Regular'),
                     (4, 'Pet Emoji Atlas Regular'), (6, 'PetEmojiAtlas-Regular'),
                     (16, 'Pet Emoji Atlas')):
        name.setName(val, nid, 3, 1, 0x409)
        name.setName(val, nid, 1, 0, 0)

    def add_glyph(gname):
        pen = TTGlyphPen(None)
        glyph = pen.glyph()
        glyph.recalcBounds(font['glyf'])
        font['glyf'][gname] = glyph
        font['hmtx'][gname] = (2048, 0)
        if gname not in font.getGlyphOrder():
            font.setGlyphOrder(list(font.getGlyphOrder()) + [gname])

    pua = {}
    for i, e in enumerate(entries):
        g = glyph_name(e)
        add_glyph(g)
        pua[g] = 0xE000 + i
    for table in font['cmap'].tables:
        if table.isUnicode():
            for g, cp in pua.items():
                table.cmap[cp] = g

    print('pua glyphs added', flush=True)
    # CBDT / CBLC
    cblc = C_B_L_C_.table_C_B_L_C_()
    cbdt = C_B_D_T_.table_C_B_D_T_()
    cblc.version = 3.0
    cbdt.version = 3.0
    cblc.numSizes = 1
    strike = E_B_L_C_.Strike()
    bst = strike.bitmapSizeTable
    bst.ppemX = bst.ppemY = PPEM
    bst.bitDepth = 32
    bst.flags = 1
    bst.colorRef = 0
    for direction in ('hori', 'vert'):
        m = E_B_L_C_.SbitLineMetrics()
        m.ascender = PPEM - 1
        m.descender = -1
        m.widthMax = PPEM
        m.caretSlopeNumerator = 0
        m.caretSlopeDenominator = 0
        m.caretOffset = 0
        m.minOriginSB = 0
        m.minAdvanceSB = 0
        m.maxBeforeBL = 0
        m.minAfterBL = 0
        m.pad1 = 0
        m.pad2 = 0
        setattr(bst, direction, m)
    names = [glyph_name(e) for e in entries]
    ids = [font.getGlyphID(g) for g in names]
    bst.startGlyphIndex = min(ids)
    bst.endGlyphIndex = max(ids)
    ist = E_B_L_C_.eblc_index_sub_table_1(None, None)
    ist.indexFormat = 1
    ist.imageFormat = 17
    ist.names = names
    ist.firstGlyphIndex = min(ids)
    ist.lastGlyphIndex = max(ids)
    strike.indexSubTables = [ist]
    cblc.strikes = [strike]
    strike_data = {}
    for e in entries:
        g = glyph_name(e)
        png = EMOJI / e['png']
        im = Image.open(png).convert('RGBA')
        if im.size != (PPEM, PPEM):
            canvas = Image.new('RGBA', (PPEM, PPEM), (0, 0, 0, 0))
            canvas.alpha_composite(im, ((PPEM - im.width) // 2, (PPEM - im.height) // 2))
            buf = BytesIO()
            canvas.save(buf, format='PNG')
            data = buf.getvalue()
        else:
            data = png.read_bytes()
        bg = C_B_D_T_.cbdt_bitmap_format_17(b'', font)
        bg.imageData = data
        m = SmallGlyphMetrics()
        m.height = PPEM
        m.width = PPEM
        m.BearingX = 0
        m.BearingY = PPEM - 1
        m.Advance = PPEM
        bg.metrics = m
        strike_data[g] = bg
    cbdt.strikeData = [strike_data]
    font['CBLC'] = cblc
    font['CBDT'] = cbdt

    print('bitmaps collected', flush=True)
    # shortcode ligatures: build the GSUB binary directly (fontTools' generic
    # compiler is far too slow for 600+ ligatures).  Primary shortcodes only;
    # aliases remain available in shortcodes.json.
    cmap = font.getBestCmap()
    def gid(ch): return font.getGlyphID(cmap[ord(ch)])
    colon_gid = gid(':')
    ligs = []
    for e in entries:
        g = font.getGlyphID(glyph_name(e))
        code = e['shortcode']
        comps = [gid(c) for c in code[1:]]  # includes the trailing colon
        ligs.append((g, comps))
    ligs.sort(key=lambda x: -len(x[1]))
    recs = [struct.pack('>HH', g, len(c)) + b''.join(struct.pack('>H', x) for x in c) for g, c in ligs]
    n = len(recs)
    cur = 2 + 2 * n
    offs = []
    for rec in recs:
        offs.append(cur)
        cur += len(rec)
        if cur % 2: cur += 1
    ls = struct.pack('>H', n) + b''.join(struct.pack('>H', o) for o in offs)
    for rec in recs:
        ls += rec
        if len(ls) % 2: ls += b'\0'
    cov = struct.pack('>HHH', 1, 1, colon_gid)
    sub = struct.pack('>HHHH', 1, 8, 1, 8 + len(cov)) + cov + ls
    lookup = struct.pack('>HHH', 4, 0, 1) + struct.pack('>H', 8) + sub
    lookuplist = struct.pack('>HH', 1, 4) + lookup
    feature = struct.pack('>HHH', 0, 1, 0)
    featurelist = struct.pack('>H', 1) + b'liga' + struct.pack('>H', 8) + feature
    langsys = struct.pack('>HHHH', 0, 0xFFFF, 1, 0)
    script = struct.pack('>HH', 4, 0) + langsys
    scriptlist = struct.pack('>H', 2) + b'DFLT' + struct.pack('>H', 14) + b'latn' + struct.pack('>H', 14) + script
    scriptlist_off = 10
    featurelist_off = scriptlist_off + len(scriptlist)
    lookuplist_off = featurelist_off + len(featurelist)
    gsub_data = struct.pack('>IHHH', 0x00010000, scriptlist_off, featurelist_off, lookuplist_off) + scriptlist + featurelist + lookuplist
    class RawGSUB(DefaultTable):
        def __init__(self, data):
            super().__init__('GSUB')
            self.data = data
        def compile(self, ttFont): return self.data
        def decompile(self, data, ttFont): self.data = data
    font['GSUB'] = RawGSUB(gsub_data)
    rules = recs
    print('gsub built', flush=True)
    font_dir = EMOJI / 'font'
    font_dir.mkdir(exist_ok=True)
    out = font_dir / 'emoji.ttf'
    print('saving font...', flush=True)
    font.save(out)
    print('font saved', flush=True)
    if LICENSE.exists():
        import shutil
        shutil.copyfile(LICENSE, font_dir / 'LICENSE-DejaVu.txt')
    (font_dir / 'emoji.css').write_text(
        "@font-face {\n  font-family: 'Pet Emoji Atlas';\n  src: url('emoji.ttf') format('truetype');\n"
        "  font-display: swap;\n}\n\n.mood-emoji { font-family: 'Pet Emoji Atlas', sans-serif; }\n"
        "img.emoji { width: 1em; height: 1em; vertical-align: -0.125em; }\n", encoding='utf-8')
    print('wrote', out, out.stat().st_size, 'bytes;', len(entries), 'glyphs;', len(rules), 'ligatures')

    # preview the first project's 12 forms from the compiled font
    try:
        f = ImageFont.truetype(str(out), PPEM)
        first = manifest['projects'][0]
        cell = 160
        sheet = Image.new('RGB', (4 * cell, 3 * cell), 'white')
        for i, e in enumerate(first['forms']):
            im = Image.new('RGBA', (cell, cell), (255, 255, 255, 255))
            dd = ImageDraw.Draw(im)
            dd.text((16, 8), chr(int(e['codepoint'][2:], 16)), font=f, embedded_color=True)
            sheet.paste(im.convert('RGB'), ((i % 4) * cell, (i // 4) * cell))
        sheet.save(font_dir / 'preview.png')
        print('font preview ok')
    except Exception as exc:
        print('font preview failed:', exc)

if __name__ == '__main__':
    main()
