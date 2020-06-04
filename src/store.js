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
    gLocPlotPath: '@/assets/plots/plotreal.svg',
    gLocPlotName: 'plotreal.svg',
    gPlotList: [],
    gSaveOne: '@/assets/plots/plotreal.svg',
    sWhichPlot: 0,
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
    gLocPlotPathMut(state, theval) {
      state.gLocPlotPath = theval
    },
    gPlotListMut(state, theval) {
      state.gPlotList = theval
    },
    gPlotListMutZero(state, theval) {
      state.gPlotList[0] = theval  //replaces a val
    },
    gLocPlotNameMut(state, theval) {
      state.gLocPlotName = theval
    },
    gSaveOneMut(state, theval) {
      state.gSaveOne.push(theval)
    },
    sWhichPlotMut(state, theval) {
      state.sWhichPlot = theval
    },
  },
  getters: {
    gShowPlotGet: state => state.gShowPlot,
    gLocPlotPathGet: state => state.gLocPlotPath,
    gPlotListGet: state => state.gPlotList,
    gSaveOneGet: state => state.gSaveOne,
    sWhichPlotGet: state => state.sWhichPlot,

  },
  actions: {  
    gCounterAct (context, theval) {
      context.commit('gCounterMut', theval)
    },
    sCounterAct (context, theval) {
      context.commit('sCounterMut', theval)
    },
    gLocPlotPathAct (context, theval) {
      context.commit('gLocPlotPathMut', theval)
    },
    gPlotListAct (context, theval) {
      context.commit('gPlotListMut', theval)
    },
    gPlotListActZero (context, theval) {
      context.commit('gPlotListMutZero', theval)
    },
    gLocPlotNameAct (context, theval) {
      context.commit('gLocPlotNameMut', theval)
    },
    gSaveOneAct (context, theval) {
      context.commit('gSaveOneMut', theval)
    },
    sWhichPlotAct (context, theval) {
      context.commit('sWhichPlotMut', theval)
    }
  }

})
