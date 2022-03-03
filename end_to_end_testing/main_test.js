Feature('Test sentences toxicity');

Scenario('test positive sentence', async ({ I }) => {
  I.amOnPage('/')
  I.fillField("#text_id", "oh hi")
  I.click('Analyse')
  I.waitForText('sentence was rated', 25)
  I.see('The "oh hi" sentence was rated as not toxic')
});

Scenario('test negative sentence', async ({ I }) => {
  I.amOnPage('/')
  I.fillField("#text_id", "i hate you")
  I.click('Analyse')
  I.waitForText('sentence was rated', 15)
  I.see('The "i hate you" sentence was rated as toxic')
});

Scenario('test negative sentence 2', async ({ I }) => {
  I.amOnPage('/')
  I.fillField("#text_id", "you dumb idiot")
  I.click('Analyse')
  I.waitForText('sentence was rated', 15)
  I.see('The "you dumb idiot" sentence was rated as toxic')
});

Scenario('test positive sentence 2', async ({ I }) => {
  I.amOnPage('/')
  I.fillField("#text_id", "i love you")
  I.click('Analyse')
  I.waitForText('sentence was rated', 15)
  I.see('The "i love you" sentence was rated as not toxic')
});
