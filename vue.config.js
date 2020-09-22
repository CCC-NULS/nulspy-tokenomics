
const westprod = false   // true in production on westteam

// if (westprod) {
//   const fs = require('fs')
//   const https = require('https')
//   const fn1 = "/etc/letsencrypt/archive/westteam.nulstar.com/fullchain1.pem"
//   const fn2 = "/etc/letsencrypt/archive/westteam.nulstar.com/privkey1.pem"
//   var devServer = {
//     https: {
//       cert: fs.readFileSync(fn1),
//       key: fs.readFileSync(fn2),
//       rejectUnauthorized: false
//     },
//     public: 'https://localhost:5000/',
//   }
// }
// else {
//   var devServer = ''
// }

module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/tokenlife/' : '/',
  outputDir: 'dist/',
  // devServer,
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
