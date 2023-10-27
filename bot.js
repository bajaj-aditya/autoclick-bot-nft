// Import necessary modules
const puppeteer = require("puppeteer-extra");
const StealthPlugin = require("puppeteer-extra-plugin-stealth");
puppeteer.use(StealthPlugin()); // Use the stealth plugin

(async () => {
  // Launch a new browser instance
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // 1. Use a Real User Agent
  await page.setUserAgent("Your User Agent");

  // 2. Set the Viewport
  await page.setViewport({ width: 1366, height: 768 });

  // 3. Wait for Network to be Idle while navigating
  await page.goto("https://play.maisonmargiela.digital/game", {
    waitUntil: "networkidle2",
  });

  // Set the cookies
  const cookies = [
    //your cookies
  ];

  await page.setCookie(...cookies);

  // Navigate again after setting the cookies
  await page.goto("https://play.maisonmargiela.digital/game", {
    waitUntil: "networkidle2",
  });

  // Wait for you to solve the captcha manually
  console.log(
    "Please solve the captcha manually. After you're done, press any key to continue..."
  );
  process.stdin.resume();
  process.stdin.once("data", async () => {
    // After you've indicated you're done (by pressing any key), the script will continue

    // Click the button
    try {
      await page.waitForSelector("YOUR_BUTTON_SELECTOR", { timeout: 10000 });
      await page.click("YOUR_BUTTON_SELECTOR");
    } catch (error) {
      console.error("Failed to find the button:", error);
    }

    // Wait for a bit to observe the browser (optional)
    await new Promise((resolve) => setTimeout(resolve, 20000));

    await browser.close();
  });
})();
