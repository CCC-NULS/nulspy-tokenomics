import Vue from 'vue'
// import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: '#009688',     // teal
  secondary: '#673AB7',  // deep purple  673AB7
  success: '#FF5722',   // deep-orange 
  accent: '#00BCD4',    // cyan
  info: 'grey',              //   grey 
  error: '#F44336',   // red
  warning: '#FF5722',    // deep-orange

  darkgrey: '#212121',    // almost black
  pagegrey: 'grey darken-4',

  mytext: "#000000",   // black
  alwayswhite: "#FFFFFF",  // white

  tertiary:  '#212121',     // darkdarkgrey

}
// teal=009688
 // deep purple  673AB7
 //  blue #0a406c from gradient
// #00BCD4',    // cyan
// #FF5722',    // deep-orange
//  '#F44336',   // red
// darkgrey: '#212121'

const dtheme = {
  primary: '#009688',     // teal
  secondary: '#673AB7',  // deep purple 
  success: '#FF5722',   // deep-orange 
  accent: '#00BCD4',    // cyan
  info: 'grey',   //  grey
  error: '#F44336',   // red
  warning: '#FF5722',    // deep-orange
  darkgrey: '#212121',    // almost black
  pagegrey: 'grey darken-4',

  mytext: "#FFFFFF",        // white
  alwayswhite: '#FFFFFF',     // white

  tertiary:  '#212121',     // darkdarkgrey

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
