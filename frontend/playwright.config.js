// @ts-check

/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    use: {
        baseURL: 'http://127.0.0.1:5000/',
        browserName: 'chromium',
        headless: true,
    },
};

module.exports = config;