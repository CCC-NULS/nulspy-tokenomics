
const fs = require('fs')
const https = require('https')

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/tokenlife/' : '/',
  outputDir: 'dist/',
  devServer: {
    https: {
      cert: fs.readFileSync("/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem"),
      key: fs.readFileSync("/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem"),
      rejectUnauthorized: false
    },
    public: 'https://localhost:5000/'
  },
  transpileDependencies: ['vuetify'],
  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false,
    },
  },
}
