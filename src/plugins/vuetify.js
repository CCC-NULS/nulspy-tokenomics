import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import i18n from '@/i18n'
import '@/sass/overrides.sass'

Vue.use(Vuetify)

const theme = {
  primary: '#6200EE',
  secondary: '#03DAC5',
  accent: '#9C27b0',
  info: '#3700B3',
  error: '#FF4D53',
  warning: '#37474F',
  success: '#00BFA5',
}

export default new Vuetify({
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
