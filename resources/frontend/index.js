const puppeteer = require('puppeteer');
const path = require('path');

// 从命令行参数获取 HTML 文件路径和输出文件名
const htmlFileName = process.argv[2]; // 第一个参数为 HTML 文件名
const outputFileName = process.argv[3]; // 第二个参数为输出文件名

(async () => {
  const browser = await puppeteer.launch({
    headless: true, // 强制无头模式
    args: ['--no-sandbox', '--disable-setuid-sandbox'] // 适用于某些环境
  });
  const page = await browser.newPage();

  // 使用命令行参数指定的 HTML 文件
  const filePath = htmlFileName; // 用哪个 HTML 就改成哪个
  
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });

  const element = await page.$("#canvas");
  await element.screenshot({ path: outputFileName }); // 使用命令行参数指定的输出文件名

  await browser.close();
})();
