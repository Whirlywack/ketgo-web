import sys, os
from fontTools.ttLib import TTFont
LT = "ąčęėįšųūžĄČĘĖĮŠŲŪŽ"
WANT = list(range(0x20,0x7F)) + [ord(c) for c in LT] + [0xA0,0xAD,0xB0,0xAB,0xBB,0x2013,0x2014]+list(range(0x2018,0x201F))+[0x2026,0x20AC,0x2192,0x2190,0x2713,0x2715]
for p in sys.argv[1:]:
    f = TTFont(p); cmap = f.getBestCmap()
    miss = ["U+%04X"%u for u in WANT if u not in cmap]
    feats=set()
    for t in ('GSUB','GPOS'):
        if t in f and f[t].table.FeatureList:
            feats |= {fr.FeatureTag for fr in f[t].table.FeatureList.FeatureRecord}
    axes = [(a.axisTag, a.minValue, a.maxValue) for a in f['fvar'].axes] if 'fvar' in f else "static wght=%d"%f['OS/2'].usWeightClass
    lt_ok = all(ord(c) in cmap for c in LT)
    print(f"{os.path.basename(p):48s} {os.path.getsize(p):6d} B glyphs={f['maxp'].numGlyphs:3d} LT18={lt_ok} axes={axes} feats={sorted(feats)} missing={miss}")
