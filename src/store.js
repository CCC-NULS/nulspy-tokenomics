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
    gTimeStamp: null,
    gLocPlotPath: null,
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
    gTimeStampMut(state, theval) {
      state.gTimeStamp = theval
    },
    gLocPlotPathMut(state, theval) {
      state.gLocPlotPath = theval
    },
    gPlotListMut(state, theval) {
      state.gPlotList = theval
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
    gTimeStampAct (context, theval) {
      context.commit('gTimeStampMut', theval)
    },
    gLocPlotPathAct (context, theval) {
      context.commit('gLocPlotPathMut', theval)
    },
    gPlotListAct (context, theval) {
      context.commit('gPlotListMut', theval)
    }
  }

})
