// wabbywabbocrm-page.js
const { expect } = require('@playwright/test');

exports.WabbywabboCrmPage = class WabbywabboCrmPage {

  /**
   * @param {import('@playwright/test').Page} page
   */
  constructor(page) {
    this.page = page;
    this.LoginLink = page.locator('text=Login');
    this.RegisterLink = page.locator('text=Register');
    // this.tocList = page.locator('article ul > li > a');
  }

  async goto() {
    await this.page.goto('/');
  }

  async goToLogin() {
    await this.LoginLink.first().click();
    await expect(this.page).toHaveURL('/app/login');
    await expect(this.page.locator('text=Sign in to').first()).toBeVisible();
  }

  async goToRegister() {
    await this.RegisterLink.first().click();
    await expect(this.page).toHaveURL('/app/register');
    await expect(this.page.locator('text=Sign up for').first()).toBeVisible();
  }
}