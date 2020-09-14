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
        {
          name: 'Tokenomics',
          path: '/tokenomics',
          component: () => import('@/views/pages/Tokenomics'),
        },

      ],
    },
  ],
})
