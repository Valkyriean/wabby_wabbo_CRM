const { test, expect } = require('@playwright/test');
const { WabbywabboCrmPage } = require('./wabbywabbocrm-page');

test('test homepage functionalities', async ({ page }) => {
  const crm = new WabbywabboCrmPage(page);
  await crm.goto();
  // Expect a title "to contain" a substring.
  await expect(crm.page).toHaveTitle(/wabby_wabbo_crm/);

  await crm.goToRegister();
  await crm.goToLogin();
});