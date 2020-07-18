import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/dashboard/Index'),
      children: [
        // Pages
        {
          name: 'Create Graph',
          path: 'pages/creategraph',
          component: () => import('@/views/dashboard/pages/CreateGraph'),
        }, 
        {
          name: 'Saved Graphs',
          path: 'pages/savedgraphs',
          component: () => import('@/views/dashboard/pages/SavedGraphs'),
        },
        {
          name: 'Tokenomics',
          path: 'pages/tokenomics',
          component: () => import('@/views/dashboard/pages/Tokenomics'),
        },
        {
          name: 'About',
          path: 'about',
          component: () => import('@/views/dashboard/pages/Tokenomics'),
        },
        // {
        //   name: 'Create Cs',
        //   path: 'pages/createcs',
        //   component: () => import('@/views/dashboard/pages/CreateCs'),
        // },
        {
          name: 'Landing',
          path: 'pages/landing',
          component: () => import('@/views/dashboard/pages/Landing'),
        }, 
      
      ],
    },
  ],
})
