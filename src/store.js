import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    gCounter: 0,
    sCounter: 0,
    gTimeNAMEonly: '',
    gTimedPlotPath: '',
    gPlotPATHARRAY: [],
    showme: false,
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
    gPlotPATHARRAYMut(state, theval) {
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
    // sWhichPlotMut(state, theval) {
    //   state.sWhichPlot = theval
    // },
  },
  getters: {
    gShowPlotGet: state => state.gShowPlot,
    gTimedPlotPathGet: state => state.gTimedPlotPath,
    gPlotPATHARRAYGet: state => state.gPlotPATHARRAY,
    // gSaveOneGet: state => state.gSaveOne,
    // sWhichPlotGet: state => state.sWhichPlot,

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
    gPlotPATHARRAYAct (context, theval) {
      context.commit('gPlotPATHARRAYMut', theval)
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
    // sWhichPlotAct (context, theval) {
    //   context.commit('sWhichPlotMut', theval)
    // }
  }

})
