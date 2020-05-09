import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuetify, VueAxios, axios)

// Vue.axios.get(api).then((response) => {
//   console.log(response.data)
// })

// const result = axios.post(POSTURL_w4,
//   {
//     "jsonrpc": "2.0",
//     "method": METHOD_D,
//     "params": PARAMS,
//     "id": ID_D
//   })

const theme = {
  primary: '#37474F',
  secondary: '#651FFF',
  tertiary: '#009688',
  success: '#00BFA5',
  accent: '#212121',
  info: '#651FFF',
  error: '512DA8',
  warning: '#455A64',
  darkgrey: '#212121',
}

export default new Vuetify({
  axios,
  VueAxios,
  lang: {
    t: (key, ...params) => i18n.t(key, params),
  },
  theme: {
    themes: {
      dark: theme,
      light: theme,
    },
  },
})
