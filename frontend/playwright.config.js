// @ts-check

/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    use: {
        baseURL: 'http://10.0.0.36:5000/',
        browserName: 'chromium',
        headless: true,
    },
};

module.exports = config;