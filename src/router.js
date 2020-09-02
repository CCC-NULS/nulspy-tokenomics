import Vue from 'vue'
import Router from 'vue-router'
import $store from './store'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/Index'),
      // beforeEnter: $store.dispatch("gShowMeAct", true),
      // beforeRouteUpdate: $store.dispatch("gShowMeAct", true),
      children: [
        {
          path: '',
          name: 'Home',
          component: () => import('@/views/pages/Home'),
        },
        // Pages
        {
          name: 'Create Graph',
          path: 'pages/creategraph',
          component: () => import('@/views/pages/CreateGraph'),
        }, 
        {
          name: 'Saved Graphs',
          path: 'pages/savedgraphs',
          component: () => import('@/views/pages/SavedGraphs'),
        },
        {
          name: 'Tokenomics',
          path: 'pages/tokenomics',
          component: () => import('@/views/pages/Tokenomics'),
        },
        // {
        //   name: 'About',
        //   path: 'about',
        //   component: () => import('@/views/dashboard/pages/Tokenomics'),
        // },
        {
          name: 'Create Cs',
          path: 'pages/createcs',
          component: () => import('@/views/pages/CreateCs'),
        },
      ],
    },
  ],
})
