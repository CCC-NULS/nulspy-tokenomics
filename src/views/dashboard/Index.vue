<template>
  <v-app>
    <dashboard-core-app-bar />

    <dashboard-core-drawer />

    <core-view />
   
    <dashboard-core-settings />
  </v-app>
</template>

<script>


  export default {
    name: 'Index',

    components: {
      DashboardCoreAppBar: () => import('./components/core/AppBar'),
      DashboardCoreDrawer: () => import('./components/core/Drawer'),
      DashboardCoreSettings: () => import('./components/core/Settings'),
      CoreView: () => import('./components/core/View'),
    },

    data: () => ({
      expandOnHover: false,

    }),
  }
</script>
