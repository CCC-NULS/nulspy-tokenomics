import Vue from 'vue'
// import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: colors.teal.base, // #009688
  primarydark: colors.teal.darken1, // # 
  secondary: colors.deepPurple.base,  // deep purple  673AB7
  success: colors.cyan.base,   // cyan
  accent: colors.deepOrange.lighten2,    // deep-orangeFF5722
  info: colors.grey.base,              //   grey 
  
  error: colors.red.base,   // red
  warning: colors.deepOrange.base,    // deep-orange

  pagegrey: colors.grey.lighten4,   // off-white page backgrounds
  pagegreytext: colors.white,   // off-white page backgrounds
  lighttext: colors.deepOrange.lighten5,     //deep-orange lighten-5 e7
   
  mytext: colors.black,               // black for light them
  alwayswhite: colors.white,          // white 
  
  tertiary: colors.grey.darken2,     // darkdarkgrey
 
}
// teal=009688
 // deep purple  673AB7
 //  blue #0a406c from gradient
// #00BCD4',    // cyan
// #FF5722',    // deep-orange
//  '#F44336',   // red
// darkgrey: '#212121'
//'deep-orange lighten-5'
  // lighttext: '#FBE9E7',     //'deep-orange lighten-5 e7'

const dtheme = {
  primary: colors.teal.base, // #009688
  primarydark: colors.teal.darken1, // # 

  secondary: colors.deepPurple.base,  // deep purple  673AB7
  success: colors.cyan.base,   // cyan
  accent: colors.deepOrange.lighten2,    // deep-orangeFF5722
  info: colors.grey.base,              //   grey 
  error: colors.red.base,   // red
  warning: colors.deepOrange.base,    // deep-orange

  pagegrey: colors.grey.darken2,   // off-white page backgrounds
  pagegreytext: colors.white,   // off-white page backgrounds
  lighttext: colors.deepOrange.lighten5,     //deep-orange lighten-5  
 
  mytext: colors.white,        // white
  alwayswhite: colors.white,      // white

  tertiary: colors.grey.darken2,     // darkdarkgrey
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
