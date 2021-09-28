const { test, expect } = require('@playwright/test');
const { WabbywabboCrmPage } = require('./wabbywabbocrm-page');

// Make up an email address for this test
const serverDomain = 'gmail.com';
const randomString = new Date().getTime();
const testEmail = `${randomString}@${serverDomain}`;
const testPassword = randomString.toString();

test('test user registration', async ({ page }) => {
  // goto registration page
  const crm = new WabbywabboCrmPage(page);
  await crm.goto();
  await crm.goToRegister();

  // fill in and submit
  await crm.page.fill('[placeholder="Username"]', testEmail);
  await crm.page.fill('[placeholder="Password"]', testPassword);
  await crm.page.fill('[placeholder="Confirm password"]', testPassword);
  await page.click('button:below([placeholder="Confirm password"])');
  // test whether go to dashboard
  await expect(crm.page).toHaveURL('/app/dashboard');
});

test('test user login', async ({ page }) => {
    // goto login  page
  const crm = new WabbywabboCrmPage(page);
  await crm.goto();
  await crm.goToLogin();
  // fill in and submit
  await crm.page.fill('[placeholder="Username"]', testEmail);
  await crm.page.fill('[placeholder="Password"]', testPassword);
  await page.click('text=Log in');
  // test whether go to dashboard
  await expect(crm.page).toHaveURL('/app/dashboard');
});