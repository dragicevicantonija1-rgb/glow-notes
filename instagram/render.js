// HTML objave -> JPG 1080×1350 (poziva ga make_instagram.py)
const { chromium } = require("playwright");

(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const j of jobs) {
    await page.goto("file://" + j.html);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: j.jpg, type: "jpeg", quality: 92 });
  }
  await browser.close();
})();
