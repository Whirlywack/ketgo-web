# KETGO facts: font sizes and Lithuanian hyphenation

Measured on 2026-10-14 for the "Look and feel" ticket (Whirlywack/ketgo-web#12). Tools: fonttools 4.67.0 + brotli, npm `hyphen` 1.14.1. Scripts are in this folder (`build.sh`, `verify.py`, `hyph.js`, `hyph2.js`, `cfhyph.py`, ...).

## 1. Fonts for self-hosting

Budget (from "First impression and mobile UI"): at most 2 WOFF2 files, at most 60 KB, all 18 Lithuanian letters.

How: TTFs from `raw.githubusercontent.com/google/fonts/main/ofl/<name>/`; `fonttools varLib.instancer` to cut axes; `pyftsubset --flavor=woff2 --layout-features=kern,liga,calt,tnum` with Basic Latin, the 18 Lithuanian letters, U+00A0, U+00AD, U+00B0, « », – —, ‘ ’ ‚ “ ” „, …, €, ← →, ✓ ✕.

Licences: all **OFL-1.1**, no Reserved Font Name (Atkinson Hyperlegible Next 2020-2024; Barlow 2017; Archivo 2020). All full fonts have the 18 Lithuanian letters as precomposed code points, so content must be NFC-normalised at build time.

| Font | Files | Kept | Bytes | Fits? |
|---|---|---|---|---|
| Atkinson Hyperlegible Next | 1 variable | wght 400–700 | **13,340** | yes |
| Atkinson Hyperlegible Next | 2 static | 400 + 700 | 15,560 | yes |
| Barlow + Barlow Condensed | 3 static | 400, 600, Condensed 700 (no hinting) | 27,908 | **no: 3 files** |
| Barlow + Barlow Condensed | 2 static | 400 + Condensed 700 (no hinting) | ~18,400 | yes (sum of the two files above) |
| Archivo | 1 variable | wght 400–700, wdth 100–125 | 32,032 | yes |
| Archivo | 2 files | text wght 400–700 @ wdth 100 + heading 700 @ wdth 125 | **25,320** | yes |

- Instancing to only the needed range always helps (Atkinson −41 %, Archivo −38 %).
- Missing in the full fonts (so from a system fallback): ✓ ✕ in all; ← → in Atkinson and Barlow; U+201B (unused in Lithuanian). Draw icons as SVG.
- At a soft-hyphen break, browsers draw U+2010 if the font has it, else U+002D (Blink `ComputedStyle::HyphenString()`, WebKit `ComputedStyle::hyphenString()`). Atkinson has no U+2010, so it shows "-". Fine.

## 2. Lithuanian hyphenation

**Browser `hyphens: auto` with `lang="lt"` does not work on iPhones or on Android 12 and older.**
- iOS Safari: WebKit asks `CFStringIsHyphenationAvailableForLocale` (`HyphenationCF.cpp`); on macOS 26.6.2 it returns false for `lt` (true for `pl`, `de`, `ru`, ...). MDN BCD: `safari: false`. Not tested on a real iPhone.
- Chrome Android: reads the OS file `hyph-lt.hyb` (`hyphenation_impl.cc`, `hyphenation_minikin.cc`); AOSP added `addHyphenator("lt", 2, 2)` in Android 13. Not tested on a real phone; vendor images may differ.

**Build-time soft hyphens work everywhere.** `hyphen/lt` (package ISC; patterns MIT, hyph-lt.tex by Sigitas Tolušis and Yannis Haralambous, 1992) inserts U+00AD; `hyphens: manual` is supported from Chrome Android 55 and iOS Safari 4.2. Patterns file 24 KB, build time only. Min-left/right 2/2, words under 5 letters untouched.

Output on KET words: `per·si·ri·kiuo·jan·ty·sis`, `tra·jek·to·ri·jos`, `ar·tė·jan·čioms`, `su·si·ker·tan·čių`, `prie·mo·nėms`, `pir·me·ny·bės`, `san·kry·žo·je`, `pės·čių·jų`, `per·ėjo·je`, `au·to·ma·gist·ra·lė·je`, `ne·pil·na·me·čiams`, `vai·ruo·to·jas`, `at·si·žvelg·ti`, `švie·so·fo·ro`, `ap·si·su·ki·mas`, `greit·ke·ly·je`.

Checked against VLKK resolution No. 60 (1997), point 1.5:
- **Wrong:** `ly·gi·a·reikš·mių` (should be `ly·gia·reikš·mių`), `de·ši·ni·a·ran·kis`. Same error class: "i" marking a soft consonant before a vowel in some compounds.
- Minor: `juo·dže·mis` (VLKK: `juod-žemis`).
- Missed breaks only: `kelkraš·ty·je`, `vie·nakryp·tis`.
- Allowed: `gist·ra`, `elekt·ro`, `ašt·rus`, prefix breaks like `per·ėjo·je`.
- The `exceptions` option matches exact word forms only, so each inflected form must be listed (`lygiareikšmių`, `lygiareikšmis`, ...).
