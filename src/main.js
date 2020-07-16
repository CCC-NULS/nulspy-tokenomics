// =========================================================
// * Vuetify Material Dashboard - v2.1.0
// =========================================================
//
// * Product Page: https://www.creative-tim.com/product/vuetify-material-dashboard
// * Copyright 2019 Creative Tim (https://www.creative-tim.com)
//
// * Coded by Creative Tim
//
// =========================================================
//
// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import './plugins/chartist'
import vuetify from './plugins/vuetify'
import i18n from './i18n'
import 'material-icons'
import vuelidate from 'vuelidate'
import ISCENTOS from './constants.js'
import VueCurrencyInput from 'vue-currency-input'

// Vue.use(VueCurrencyInput)
Vue.config.productionTip = false

const pluginOptions = {
  globalOptions: {
    locale: 'en',
    precision: '0',
    'value-as-integer': 'true',
    'allow-negative': 'false',
  }
}
Vue.use(VueCurrencyInput, pluginOptions)

new Vue({
  ISCENTOS,
  vuelidate,
  router,
  store,
  vuetify,
  i18n,
  iconfont: 'mdi',
  render: h => h(App)
}).$mount('#app')
