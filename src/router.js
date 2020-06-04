import Vue from 'vue'
import Router from 'vue-router'
// import store from './store'

Vue.use(Router)

const plotreal = {
  template: '<div>User</div>'
}
// const plist = store.state.gPlotList

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
          path: '',
          component: () => import('@/views/dashboard/pages/UserProfile'),
        }, 
        // Dashboard
        {
          name: 'Dashboard',
          path: 'dashboard',
          component: () => import('@/views/dashboard/Dashboard'),
        },

        // {
        //   name: 'plotreal',
        //   path: 'assets/plots/comps',
        //   component: () => import('@/assets/plots/comps/plotreal.svg'),
        // },
        // {
        //   name: 'plotdirnew',
        //   path: 'assets/plots/comps',
          
        // },
        
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
        // {
        //   name: 'plotonecomp',
        //   path: 'assets/plots',
        //   tplot: plist[1],
        //   component: () => import(tplot),  // async dynamic load works component: () => import('@/assets/plots/plot.svg'),
        // },
      ],
    },
  ],
})
