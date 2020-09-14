import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    // barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    gShowMe: true,
    gThemeChgKey: '',
    gDirPath: '',
    gTheme: false,
    gThemeChgKey: 0,
  },
  mutations: {
    SET_BAR_IMAGE(state, payload) {
      state.barImage = payload
    },
    SET_DRAWER(state, payload) {
      state.drawer = payload
    },
    gShowMeMut(state, theval) {
      state.gShowMe = theval
    },
    gThemeChgKeyMut(state, theval) {
      state.gThemeChgKey = theval
    },
    gDirPathMut(state, theval) {
      state.gDirPath = theval
    },
    gThemeMut(state, theval) {
      state.gTheme = theval
    },
  },
  getters: {
    gShowMeGet: state => state.gShowMe,
    gDirPathGet: state => state.gDirPath,
    gThemeChgKeyGet: state => state.gThemeChgKey,
    gThemeGet: state => state.gTheme,
  },
  actions: {
    gShowMeAct (context, theval) {
      context.commit('gShowMeMut', theval)
    },
    gThemeChgKeyAct(context, theval) {
      context.commit('gThemeChgKeyMut', theval)
    },
    
    gDirPathAct(context, theval) {
      context.commit('gDirPathMut', theval)
    },
    gThemeAct(context, theval) {
      context.commit('gThemeMut', theval)
      context.commit('gThemeChgKeyMut', theval)
      console.log("-- inside store.actions.gThemeAct")
      // might as well do key at some time
    }
    // this.$store.dispatch('gShowMeAct', true)

  }
});
