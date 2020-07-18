<template>
  <v-main>
    <router-view />
  
    <Landing />

    <dashboard-core-footer />
  </v-main>
</template>

<script>
  export default {
    name: 'DashboardCoreView',

    components: {
      Landing: () => import('@/views/dashboard/pages/Landing'),
      DashboardCoreFooter: () => import('./Footer'),
    },
  }
</script>
