import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
// var ps = createPersistedState()
const APP_KEY = 'My Vuex App';
// { key: APP_KEY }
// if (module.hot) {
//   // accept actions and mutations as hot modules
//     module.hot.accept(['./modules'], () => {
//       // require the updated modules
//       // have to add .default here due to babel 6 module output
//       import('./modules').then((newModules) => {
//         // swap in the new actions and mutations
//         store.hotUpdate({
//           modules: newModules.default,
//         });
//       });
//     });
//   }

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
    gShowMe: false,
    gDirName: '',
    gDirPath: '',
    gSessionStr: 'a',

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
    gShowMeMut(state, theval) {
      state.gShowMe = theval
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
    gShowMeAct (context, theval) {
      context.commit('gShowMeMut', theval)
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
