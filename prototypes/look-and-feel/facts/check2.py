import sys
from fontTools.ttLib import TTFont
for p in sys.argv[1:]:
    f = TTFont(p); cmap=f.getBestCmap()
    print(p.split('/')[-1], "U+2010:", 0x2010 in cmap, "U+0328 combining ogonek:", 0x328 in cmap, "U+0307:", 0x307 in cmap,
          "hinting: fpgm" , 'fpgm' in f, "prep", 'prep' in f, "glyf instr bytes:", sum(len(getattr(f['glyf'][g],'program',b'') and f['glyf'][g].program.getBytecode() or b'') for g in f.getGlyphOrder()) if 'glyf' in f else None,
          "gvar" in f, "HVAR" in f, "STAT" in f, "avar" in f)
    # locl langsys for LTH?
    if 'GSUB' in f:
        tags=set()
        for sr in f['GSUB'].table.ScriptList.ScriptRecord:
            for ls in sr.Script.LangSysRecord: tags.add(sr.ScriptTag+"/"+ls.LangSysTag)
        print("   GSUB langsys:", sorted(tags))
