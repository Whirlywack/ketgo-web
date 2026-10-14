import sys
from fontTools.ttLib import TTFont
LT = "ąčęėįšųūžĄČĘĖĮŠŲŪŽ"
EXTRA = [0xA0,0xAD,0xB0,0xAB,0xBB,0x2013,0x2014,0x2018,0x2019,0x201A,0x201B,0x201C,0x201D,0x201E,0x2026,0x20AC,0x2192,0x2190,0x2713,0x2715]
for p in sys.argv[1:]:
    f = TTFont(p)
    cmap = f.getBestCmap()
    print("==", p.split('/')[-1], "glyphs:", f['maxp'].numGlyphs, "cmap entries:", len(cmap))
    print("  version:", f['name'].getDebugName(5))
    missLT = [c for c in LT if ord(c) not in cmap]
    print("  Lithuanian 18 letters present:", len(LT)-len(missLT), "/ 18; missing:", missLT)
    miss = ["U+%04X" % u for u in EXTRA if u not in cmap]
    print("  missing extra:", miss)
    asc = [u for u in range(0x20,0x7F) if u not in cmap]
    print("  missing ASCII:", ["U+%04X"%u for u in asc])
    if 'fvar' in f:
        print("  axes:", [(a.axisTag, a.minValue, a.defaultValue, a.maxValue) for a in f['fvar'].axes])
    print("  OS/2 weight:", f['OS/2'].usWeightClass, "width:", f['OS/2'].usWidthClass)
    feats=set()
    for t in ('GSUB','GPOS'):
        if t in f and f[t].table.FeatureList:
            feats |= {fr.FeatureTag for fr in f[t].table.FeatureList.FeatureRecord}
    print("  features:", sorted(feats))
    print("  has kern table:", 'kern' in f, " fsType:", f['OS/2'].fsType)
