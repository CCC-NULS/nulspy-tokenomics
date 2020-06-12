import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
// var ps = createPersistedState()

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    gCounter: 0,
    sCounter: 0,
    gTimeNAMEonly: null,
    gTimedPlotPath: '',
    gPlotPATHARRAY: [],
    showme: false,
    gDirName: '',
    gDirPath: '',
    gSessionStr: '',

  },
  mutations: {
    SET_BAR_IMAGE (state, payload) {
      state.barImage = payload
    },
    SET_DRAWER (state, payload) {
      state.drawer = payload
    },
    gCounterMut(state, theval) {
      state.gCounter = theval
    },   
    sCounterMut(state, theval) {
      state.sCounter = theval
    },    
    gTimedPlotPathMut(state, theval) {
      state.gTimedPlotPath = theval
    },
    gPlotPATHARRAYpushMut(state, theval) {
      state.gPlotPATHARRAY.push(theval)
    },
    // gPlotPATHARRAYMutZero(state, theval) {
    //   state.gPlotPATHARRAY[0] = theval  //replaces a val
    // },
    gTimeNAMEonlyMut(state, theval) {
      state.gTimeNAMEonly = theval
    },
    showmeMut(state, theval) {
      state.showme = theval
    },
    gDirNameMut(state, theval) {
      state.gDirName = theval
    },
    gDirPathMut(state, theval) {
      state.gDirPath = theval
    },
    gSessionStrMut(state, theval) {
      state.gSessionStr = theval
    },
  },
  getters: {
    gShowPlotGet: state => state.gShowPlot,
    gTimedPlotPathGet: state => state.gTimedPlotPath,
    gPlotPATHARRAYGet: state => state.gPlotPATHARRAY,
    // gSaveOneGet: state => state.gSaveOne,
    gSessionStrGet: state => state.gSessionStr,

  },
  actions: {  
    gCounterAct (context, theval) {
      context.commit('gCounterMut', theval)
    },
    sCounterAct (context, theval) {
      context.commit('sCounterMut', theval)
    },
    gTimedPlotPathAct (context, theval) {
      context.commit('gTimedPlotPathMut', theval)
    },
    gPlotPATHARRAYpushAct (context, theval) {
      context.commit('gPlotPATHARRAYpushMut', theval)
    },
    // gPlotPATHARRAYActZero (context, theval) {
    //   context.commit('gPlotPATHARRAYMutZero', theval)
    // },
    gTimeNAMEonlyAct (context, theval) {
      context.commit('gTimeNAMEonlyMut', theval)
    },
    showmeAct (context, theval) {
      context.commit('showmeMut', theval)
    },
    gDirNameAct (context, theval) {
      context.commit('gDirNameMut', theval)
    },
    gDirPathAct (context, theval) {
      context.commit('gDirPathMut', theval)
    },
    gSessionStrAct (context, theval) {
      context.commit('gSessionStrMut', theval)
    }
  }
})
