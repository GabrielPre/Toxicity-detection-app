require('ts-node/register')
const { setHeadlessWhen } = require('@codeceptjs/configure');

// turn on headless mode when running with HEADLESS=true environment variable
// HEADLESS=true npx codecept run
setHeadlessWhen(process.env.HEADLESS);

exports.config = {
  tests: './**_test.ts',
  output: './output',
  helpers: {
    Playwright: {
      url: 'http://localhost:5000',
      show: false,
      windowSize: '1200x900',
      browser: 'chromium'
    }
  },
  name: 'end_to_end_testing',
  plugins: {
    retryFailedStep: {
      enabled: true
    },
    screenshotOnFail: {
      enabled: true
    }
  }
}