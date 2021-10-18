// @ts-check

/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    use: {
        baseURL: 'https://wabby-wabbo-crm.herokuapp.com',
        browserName: 'chromium',
        headless: true,
    }  
};

module.exports = config;