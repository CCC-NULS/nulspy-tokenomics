import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    barColor: 'rgba(33, 138, 184, 1), rgba(0, 241, 181, 1)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    gCounter: 0,
    gLocPlotPath: '@/assets/plots/plotreal.svg',
    gLocPlotName: 'plotreal.svg',
    gPlotList: [],
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
    gLocPlotPathMut(state, theval) {
      state.gLocPlotPath = theval
    },
    gPlotListMut(state, theval) {
      state.gPlotListpush(theval)
    },
    gLocPlotNameMut(state, theval) {
      state.gLocPlotName = theval
    },
    
    // showButtonMut(state, theval) {
    //   state.showButton = theval
    // },
    // gShowPlotMut(state, theval) {
    //   state.gShowPlot = theval
    // },

    // gDkyMut(state, theval) {
    //   state.gDky = theval
    // },
  },
  getters: {
    gShowPlotGet: state => state.gShowPlot,
   
    gLocPlotPathGet: state => state.gLocPlotPath,
    gPlotListGet: state => state.gPlotList,
  },
  actions: {
    // showButtonAct (context, theval) {
    //   context.commit('showButtonMut', theval)
    // },
    // gShowPlotAct (context, theval) {
    //   context.commit('gShowPlotMut', theval)
    // },
    // gDkyAct (context, theval) {
    //   context.commit('gDkyMut', theval)
    // },    
    gCounterAct (context, theval) {
      context.commit('gCounterMut', theval)
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
