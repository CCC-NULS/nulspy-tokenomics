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
    gImgName: '',
    gDirPath: '',
    gSessionStr: 'a',
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
    gImgNameMut(state, theval) {
      state.gImgName = theval
    },
    gDirPathMut(state, theval) {
      state.gDirPath = theval
    },
    gSessionStrMut(state, theval) {
      state.gSessionStr = theval
    },
  },
  getters: {
    gShowMeGet: state => state.gShowMe,
    gDirPathGet: state => state.gDirPath,
    gImgNameGet: state => state.gImgName,
    gSessionStrGet: state => state.gSessionStr,
  },
  actions: {
    gShowMeAct (context, theval) {
      context.commit('gShowMeMut', theval)
    },
    gImgNameAct(context, theval) {
      context.commit('gImgNameMut', theval)
    },
    
    gDirPathAct(context, theval) {
      context.commit('gDirPathMut', theval)
    },
    gSessionStrAct(context, theval) {
      context.commit('gSessionStrMut', theval)
    }
  }
});
