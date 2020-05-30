import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    showButton: false,
    gShowPlot: false,
    gCounter: 0,
    gDky: "0",
    gLocPlotPath: '@/assets/plots/plotreal.svg',
    gLocPlotName: 'plotreal.svg',
    gPlotList: null,
  },
  mutations: {
    SET_BAR_IMAGE (state, payload) {
      state.barImage = payload
    },
    SET_DRAWER (state, payload) {
      state.drawer = payload
    },
    showButtonMut(state, theval) {
      state.showButton = theval
    },
    gShowPlotMut(state, theval) {
      state.gShowPlot = theval
    },
    gCounterMut(state, theval) {
      state.gCounter = theval
    },
    gDkyMut(state, theval) {
      state.gDky = theval
    },
    gLocPlotPathMut(state, theval) {
      state.gLocPlotPath = theval
    },
    gPlotListMut(state, theval) {
      state.gPlotList = theval
    },
    gLocPlotNameMut(state, theval) {
      state.gLocPlotName = theval
    },
  },
  getters: {
    // gLocPlotPathGet: state => state.gLocPlotPath,
    gShowPlotGet: state => state.gShowPlot,
    // gPlotListGet: state => state.gPlotList,
  },
  actions: {
    showButtonAct (context, theval) {
      context.commit('showButtonMut', theval)
    },
    gShowPlotAct (context, theval) {
      context.commit('gShowPlotMut', theval)
    },
    gCounterAct (context, theval) {
      context.commit('gCounterMut', theval)
    },
    gDkyAct (context, theval) {
      context.commit('gDkyMut', theval)
    },
    gLocPlotPathAct (context, theval) {
      context.commit('gLocPlotPathMut', theval)
    },
    gPlotListAct (context, theval) {
      context.commit('gPlotListMut', theval)
    },
    gLocPlotNameAct (context, theval) {
      context.commit('gLocPlotNameMut', theval)
    }
  }

})
