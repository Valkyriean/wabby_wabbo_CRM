const { test, expect } = require('@playwright/test');

// Make up an email address for this test
const serverDomain = 'gmail.com';
const randomString = new Date().getTime();
const testEmail = `${randomString}@${serverDomain}`;
const testPassword = randomString.toString();

test.beforeEach(async ({ page }) => {
    // Runs before each test and signs in each page.
    await page.goto('/');
    await page.click('text=Login');
    // await page.click('text=Register');
    // fill in and submit
    await page.fill('[placeholder="Email"]', "test11@163.com");
    await page.fill('[placeholder="Password"]', "aaaa1111");
    await page.click('text=Log in');
    
});

test('test go to create form page', async ({ page }) => {
    // page is signed in.
    // test whether go to dashboard
    await expect(page).toHaveURL('/app/dashboard');
    // test create form
    const createForm = page.locator('text=Create Form');
    await createForm.first().click();
    await expect(page).toHaveURL('/app/form_create');

});

test('test create form without question contained', async ({ page }) => {
    // page is signed in.
    // test whether go to dashboard
    await expect(page).toHaveURL('/app/dashboard');
    // go to create form
    await page.locator('text=Create Form').first().click();
    await expect(page).toHaveURL('/app/form_create');
    // fill in form name and description
    await page.fill('input:above([placeholder="Please write your description"])', "Test form");
    await page.fill('[placeholder="Please write your description"]', "This is a test form");
    // await page.click('button:left-of(button:has-text("Submit"))');
    await page.click('button:has-text("Submit")');
    await expect(page).toHaveURL('/app/dashboard');
    await expect(page.locator('text = Test form').first()).toBeVisible();
    //
});

// test('test create form with questions', async ({ page }) => {
//     // page is signed in.
//     // test whether go to dashboard
//     await expect(page).toHaveURL('/app/dashboard');
//     // go to create form
//     await page.locator('text=Create Form').first().click();
//     await expect(page).toHaveURL('/app/form_create');
//     // fill in form name and description
//     await page.fill('input:above([placeholder="Please write your description"])', "Test form");
//     await page.fill('[placeholder="Please write your description"]', "This is a test form");
//     // add question
//     await page.click('button:left-of(button:has-text("Submit"))');
//     await expect(page.locator('text = Multiple choice').first()).toBeVisible();
//     // await page.fill('input:left-of(button:has-text("Multiple choice"))', "Q1");
//     await page.fill('input[name="Multiple choice"]', "Q1");
//     // await page.fill('input:below(button:has-text("Multiple choice"))', "option1");
//     await page.fill('input[name="option0"]', "option1");
//     //summit form
//     await page.click('button:has-text("Submit")');
//     await expect(page).toHaveURL('/app/dashboard');
//     await expect(page.locator('text = Test form').first()).toBeVisible();
// });