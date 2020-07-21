import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
// console.log("this in store: " + this)

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    // gCounter: 0,
    // sCounter: 0,
    // gTimeNAMEonly: '',
    // gTimedPlotPath: '',
    // gPlotPATHARRAY: [],
    gShowMe: false,
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
    // gCounterMut(state, theval) {
    //   state.gCounter = theval
    // },
    // sCounterMut(state, theval) {
    //   state.sCounter = theval
    // },
    // gTimedPlotPathMut(state, theval) {
    //   state.gTimedPlotPath = theval
    // },
    // gPlotPATHARRAYpushMut(state, theval) {
    //   state.gPlotPATHARRAY.push(theval)
    // },
    // gTimeNAMEonlyMut(state, theval) {
    //   state.gTimeNAMEonly = theval
    // },
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
    // gShowPlotGet: state => state.gShowPlot,
    // gTimedPlotPathGet: state => state.gTimedPlotPath,
    // gPlotPATHARRAYGet: state => state.gPlotPATHARRAY,
    // gSaveOneGet: state => state.gSaveOne,

    gDirPathGet: state => state.gDirPath,
    gImgNameGet: state => state.gImgName,
    gSessionStrGet: state => state.gSessionStr,

    
  },
  actions: {
    // gCounterAct (context, theval) {
    //   context.commit('gCounterMut', theval)
    // },
    // sCounterAct (context, theval) {
    //   context.commit('sCounterMut', theval)
    // },
    // gTimedPlotPathAct (context, theval) {
    //   context.commit('gTimedPlotPathMut', theval)
    // },
    // gPlotPATHARRAYpushAct (context, theval) {
    //   context.commit('gPlotPATHARRAYpushMut', theval)
    // },
    // gTimeNAMEonlyAct (context, theval) {
    //   context.commit('gTimeNAMEonlyMut', theval)
    // },
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
