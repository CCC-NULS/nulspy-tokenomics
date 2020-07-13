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
        //   name: 'TimedFile',
        //   path: 'assets/plots',
        //   component: () => import('@/assets/plots/plotnone'),
        // },
        
        // Dashboard
        // {
        //   name: 'Dashboard',
        //   path: 'dashboard',
        //   component: () => import('@/views/dashboard/Dashboard'),
        // },        
        // Tables
        // {
        //   name: 'Blockchain',
        //   path: 'tables/regular-tables',
        //   component: () => import('@/views/dashboard/tables/RegularTables'),
        // },
        // E:\wsvue\vuetify-material-dashboard-master\src\views\dashboard\components\svgs
        // {
        //   name: 'Profile Card',
        //   path: 'componentsns',
        //   component: () => import('@/views/dashboard/componentsns/ProfileCardNs'),
        // },
        // Upgrade
        // {
        //   name: 'Upgrade',
        //   path: 'upgrade',
        //   component: () => import('@/views/dashboard/Upgrade'),
        // },
      ],
    },
  ],
})
