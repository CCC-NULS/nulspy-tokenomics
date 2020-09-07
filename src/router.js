import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/Index'),

      children: [
        // {
        //   path: '',
        //   name: 'Home2',
        //   component: () => import('@/views/pages/Home'),
        // },
        // Pages
        {
          name: 'Home',
          path: '',
          component: () => import('@/views/pages/CreateGraph'),
        }, 
        // {
        //   name: 'Saved Graphs',
        //   path: 'pages/savedgraphs',
        //   component: () => import('@/views/pages/SavedGraphs'),
        // },
        {
          name: 'Tokenomics',
          path: '/tokenomics',
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
