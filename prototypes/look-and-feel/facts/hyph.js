const path = process.argv[2];
const { hyphenateSync } = require(path + "/hyphen/lt");
const words = ["persirikiuojantysis","lygiareikšmių","trajektorijos","artėjančioms","susikertančių","transporto","priemonėms","pirmenybės","sankryžoje","pėsčiųjų","perėjoje","automagistralėje","nepilnamečiams","apšviestumas","vairuotojas","atsižvelgti","šviesoforo","kelkraštyje","apsisukimas","greitkelyje"];
const extra = (process.argv[3]||"").split(",").filter(Boolean);
for (const w of words.concat(extra)) {
  const h = hyphenateSync(w, { hyphenChar: "·" });
  const parts = h.split("·");
  const flag = parts.length>1 && (parts[0].length<2 || parts[parts.length-1].length<2) ? "  <-- 1-letter piece" : "";
  console.log(w.padEnd(22), h, flag);
}
// capitalised + sentence check, default soft hyphen
const s = hyphenateSync("Automagistralėje Pėsčiųjų perėjoje.");
console.log(JSON.stringify(s), [...s].filter(c=>c==="­").length, "soft hyphens");
