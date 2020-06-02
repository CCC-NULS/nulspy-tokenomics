import Vue from 'vue'
import Router from 'vue-router'
// import { realpath } from 'fs'

Vue.use(Router)

const plotreal = {
  template: '<div>User</div>'
}

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
        {
          name: 'plotreal',
          path: 'assets/plots/comps',
          component: () => import('@/assets/plots/comps/plotreal.svg'),
        },
        
        //   children: [
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
        {
          name: 'Saved Graphs',
          path: 'pages/graphs',
          component: () => import('@/views/dashboard/pages/SavedGraphs'),
        },
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
