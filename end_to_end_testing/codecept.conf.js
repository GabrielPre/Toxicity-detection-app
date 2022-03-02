exports.config = {
  tests: './**_test.ts',
  output: './output',
  helpers: {
    Playwright: {
      url: process.env.HOME_URL || 'http://localhost:5000',
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