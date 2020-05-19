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
        // Dashboard
        {
          name: 'Dashboard',
          path: '',
          component: () => import('@/views/dashboard/Dashboard'),
        },
        // Pages
        {
          name: 'Create Graph',
          path: 'pages/user',
          component: () => import('@/views/dashboard/pages/UserProfile'),
        },
        // {
        //   name: 'Inflation',
        //   path: 'components/notifications',
        //   component: () => import('@/views/dashboard/component/Notifications'),
        // },
        // {
        //   name: 'Nodes',
        //   path: 'components/icons',
        //   component: () => import('@/views/dashboard/component/Icons'),
        // },
        {
          name: 'Staking',
          path: 'components/typography',
          component: () => import('@/views/dashboard/component/Typography'),
        },
        // Tables
        {
          name: 'Blockchain',
          path: 'tables/regular-tables',
          component: () => import('@/views/dashboard/tables/RegularTables'),
        },
        // Maps
        {
          name: 'View Graph',
          path: 'maps/google-maps',
          component: () => import('@/views/dashboard/maps/GoogleMaps'),
        },
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
