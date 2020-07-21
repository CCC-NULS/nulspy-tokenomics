import Vue from 'vue'
// import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: '#607D8B',     // blue-grey
  secondary: '#673AB7',  // deep purple 
  tertiary: '#009688',  // teal
  success: '#673AB7',  // deep purple 
  accent: '#00BCD4',    // cyan
  info: '#0a406c',   //  blue from gradient
  error: '#F44336',   // red
  warning: '#FF5722',    // deep-orange
  darkgrey: '#212121',    // almost black
  orangeaccent: '#FF5722',  // deep-orange
  mywhite: "#FFFFFF"
}

const dtheme = {
  primary: '#607D8B',     // blue-grey
  secondary: '#673AB7',  // deep purple 
  tertiary: '#009688',  // teal
  success: '#673AB7',  // deep purple 
  accent: '#00BCD4',    // cyan
  info: '#0a406c',   //  blue from gradient
  error: '#F44336',   // red
  warning: '#FF5722',    // deep-orange
  darkgrey: '#212121',    // almost black
  orangeaccent: '#FF5722',  // deep-orange
  mywhite: "#000000"
}

export default new Vuetify({
  axios,
  VueAxios,
  lang: {
    t: (key, ...params) => i18n.t(key, params),
  },
  theme: {
    themes: {
      dark: dtheme,
      light: theme,
    },
  },
})
