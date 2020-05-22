import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    showButton: false,
    showPlot: false,
    gTimeStamp: null,
    gLocPlotPath: null,
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
    showPlotMut(state, theval) {
      state.showPlot = theval
    },
    gTimeStampMut(state, theval) {
      state.gTimeStamp = theval
    },
    gLocPlotPathMut(state, theval) {
      state.gLocPlotPath = theval
    },
  },
  getters: {
    gLocPlotPathGet: state => state.gLocPlotPath
  },
    // getters: {
  //   getShowButton: state => state.showButton,
  //   getShowPlot: state => state.showPlot
  // },
  // getters: {
  //   getShowButton: state => state.showButton,
  //   getShowPlot: state => state.showPlot
  // },
  // setters: {
  //   setShowButton: state.showButton = true,
  //   setShowPlot: state.showPlot = true
  // },
  actions: {
    showButtonAct (context, theval) {
      context.commit('showButtonMut', theval)
    },
    showPlotAct (context, theval) {
      context.commit('showPlotMut', theval)
    },
    gTimeStampAct (context, theval) {
      context.commit('gTimeStampMut', theval)
    },
    gLocPlotPathAct (context, theval) {
      context.commit('gLocPlotPathMut', theval)
    }
  }

})
