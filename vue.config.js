module.exports = {
  devServer: {
    disableHostCheck: true,
  },

  transpileDependencies: ['vuetify'],

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false
    },
    svgLoader: {
      svgo: {
        plugins: [
          {removeDoctype: true},
          {removeComments: true}
        ]      
      }
    }
  },

  runtimeCompiler: true
}
