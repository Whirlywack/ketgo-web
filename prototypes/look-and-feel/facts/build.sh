#!/bin/bash
set -e
D=/private/tmp/claude-501/-Users-superoptimised-Documents-KETGO-BETA/580834ea-9f48-43f2-8da2-6a295a30b2d3/scratchpad/facts
PY="$D/venv/bin/python -I"
DL=$D/dl; O=$D/out; I=$D/out/inst; mkdir -p $O $I
U="U+0020-007E,U+0104,U+0105,U+010C,U+010D,U+0116,U+0117,U+0118,U+0119,U+012E,U+012F,U+0160,U+0161,U+016A,U+016B,U+0172,U+0173,U+017D,U+017E,U+00A0,U+00AD,U+00B0,U+00AB,U+00BB,U+2013,U+2014,U+2018-201E,U+2026,U+20AC,U+2192,U+2190,U+2713,U+2715"
sub() { # in out [extra args]
  local in=$1 out=$2; shift 2
  $PY -m fontTools.subset "$in" --unicodes="$U" --layout-features=kern,liga,calt,tnum --flavor=woff2 --output-file="$O/$out" "$@" 2>&1 | grep -v "^$" || true
}
subdef() { local in=$1 out=$2; shift 2
  $PY -m fontTools.subset "$in" --unicodes="$U" --layout-features+=tnum --flavor=woff2 --output-file="$O/$out" "$@" 2>&1 | grep -v "^$" || true
}
inst() { local in=$1 out=$2; shift 2; $PY -m fontTools.varLib.instancer "$in" "$@" -o "$I/$out" -q; }

# Atkinson Hyperlegible Next
sub $DL/AtkinsonHyperlegibleNext.ttf AHN-var-wght200-800.woff2
inst $DL/AtkinsonHyperlegibleNext.ttf AHN-400-700.ttf wght=400:700; sub $I/AHN-400-700.ttf AHN-var-wght400-700.woff2
inst $DL/AtkinsonHyperlegibleNext.ttf AHN-400.ttf wght=400; sub $I/AHN-400.ttf AHN-static-400.woff2
inst $DL/AtkinsonHyperlegibleNext.ttf AHN-700.ttf wght=700; sub $I/AHN-700.ttf AHN-static-700.woff2
subdef $I/AHN-400-700.ttf AHN-var-wght400-700.deffeat.woff2

# Barlow
sub $DL/Barlow-Regular.ttf Barlow-400.woff2
sub $DL/Barlow-SemiBold.ttf Barlow-600.woff2
sub $DL/BarlowCondensed-Bold.ttf BarlowCondensed-700.woff2
sub $DL/Barlow-Regular.ttf Barlow-400.nohint.woff2 --no-hinting
sub $DL/Barlow-SemiBold.ttf Barlow-600.nohint.woff2 --no-hinting
sub $DL/BarlowCondensed-Bold.ttf BarlowCondensed-700.nohint.woff2 --no-hinting
subdef $DL/Barlow-Regular.ttf Barlow-400.deffeat.woff2
subdef $DL/Barlow-SemiBold.ttf Barlow-600.deffeat.woff2
subdef $DL/BarlowCondensed-Bold.ttf BarlowCondensed-700.deffeat.woff2

# Archivo
sub $DL/Archivo.ttf Archivo-var-full.woff2
inst $DL/Archivo.ttf Arc-w400-700-wd100-125.ttf wght=400:700 wdth=100:125; sub $I/Arc-w400-700-wd100-125.ttf Archivo-var-wght400-700-wdth100-125.woff2
inst $DL/Archivo.ttf Arc-w400-800-wd100-125.ttf wght=400:800 wdth=100:125; sub $I/Arc-w400-800-wd100-125.ttf Archivo-var-wght400-800-wdth100-125.woff2
inst $DL/Archivo.ttf Arc-w400-700-wd100.ttf wght=400:700 wdth=100; sub $I/Arc-w400-700-wd100.ttf Archivo-var-wght400-700-wdth100.woff2
inst $DL/Archivo.ttf Arc-w700-wd125.ttf wght=700 wdth=125; sub $I/Arc-w700-wd125.ttf Archivo-static-wght700-wdth125.woff2
inst $DL/Archivo.ttf Arc-w800-wd125.ttf wght=800 wdth=125; sub $I/Arc-w800-wd125.ttf Archivo-static-wght800-wdth125.woff2
inst $DL/Archivo.ttf Arc-w400-wd100.ttf wght=400 wdth=100; sub $I/Arc-w400-wd100.ttf Archivo-static-wght400-wdth100.woff2
inst $DL/Archivo.ttf Arc-w700-wd100.ttf wght=700 wdth=100; sub $I/Arc-w700-wd100.ttf Archivo-static-wght700-wdth100.woff2
inst $DL/Archivo.ttf Arc-w700-wd100-125.ttf wght=700 wdth=100:125; sub $I/Arc-w700-wd100-125.ttf Archivo-var-wght700-wdth100-125.woff2
subdef $I/Arc-w400-700-wd100-125.ttf Archivo-var-wght400-700-wdth100-125.deffeat.woff2
