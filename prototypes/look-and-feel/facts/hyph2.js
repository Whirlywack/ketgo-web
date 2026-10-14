const base = process.argv[2];
const createHyphenator = require(base + "/hyphen/hyphen.js");
const patterns = require(base + "/hyphen/patterns/lt.js");
const h = createHyphenator(patterns, { hyphenChar: "·", exceptions: ["ly-gia-reikš-mių", "kel-kraš-ty-je"] });
console.log(h("lygiareikšmių kelkraštyje lygiareikšmis PĖSČIŲJŲ"));
const h2 = createHyphenator(patterns, { hyphenChar: "·" });
console.log(h2('<p class="automagistralėje">Automagistralėje <b>pėsčiųjų</b> perėjoje, 2026 m.</p>'));
