import Vue from 'vue'
// import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import colors from 'vuetify/lib/util/colors'
import '@mdi/font/scss/materialdesignicons.scss' // Ensure you are using css-loader

Vue.use(Vuetify, VueAxios, axios)

const theme = {
  primary: colors.teal.darken1, // #009688
  secondary: colors.teal.base,  // deep purple  673AB7
  success: colors.cyan.base,   // cyan
  accent: colors.deepOrange.lighten2,    // deep-orangeFF5722
  info: colors.grey.base,              //   grey 
  error: colors.red.base,   // red
  warning: colors.deepOrange.base,    // deep-orange

  lighttext: colors.grey.lighten5,     //deep-orange lighten-5 e7
  stayblack: colors.black,
  switchtext:colors.black, 
  swdorangelght5: colors.deepOrange.lighten5,
  tertiary: colors.grey.darken2,     // darkdarkgrey

  swbluegreylight5: colors.blueGrey.lighten5,

  switchlightgrey3: colors.grey.lighten3,
  switchlightgrey4: colors.grey.lighten4,
  switchlightgrey5: colors.grey.lighten5,
  switchdarkgrey3: colors.grey.darken3,
  switchdarkgrey4: colors.grey.darken4,

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
// teal lighten-5 #E0F2F1

const dtheme = {
  primary: colors.teal.lighten1, // #009688
  secondary: colors.teal.base,  // deep purple  673AB7
  success: colors.cyan.lighten1,   // cyan
  accent: colors.deepOrange.darken2,    // deep-orangeFF5722
  info: colors.grey.lighten1,              //   grey 
  error: colors.red.base,   // red
  warning: colors.deepOrange.base,    // deep-orange

  lighttext: colors.grey.lighten5,     //deep-orange lighten-5  
  stayblack: colors.black,  
  switchtext: colors.white, 

  switchpaper: colors.grey.darken3,
  swdeepOrange: colors.deepOrange.lighten3,
  // following all reversed:
  switchlightgrey3: colors.grey.darken3,
  switchlightgrey4: colors.grey.darken4,
  switchlightgrey5: colors.grey.darken5,

  switchdarkgrey3: colors.grey.lighten3,
  switchdarkgrey4: colors.grey.lighten4,
  switchdarkgrey5: colors.grey.lighten5,
  swbluegreylight5: colors.blueGrey.darken3,

  tertiary: colors.grey.darken2,     // darkdarkgrey
}

export default new Vuetify({
  axios,
  VueAxios,
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  },
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
