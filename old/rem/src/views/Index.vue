<template>
  <v-app>
    <core-app-bar />

    <core-drawer />

    <core-view />
   
    <core-settings />
  </v-app>
</template>

<script>


  export default {
    name: 'Index',

    components: {
      CoreAppBar: () => import('./components/core/AppBar'),
      CoreDrawer: () => import('./components/core/Drawer'),
      CoreSettings: () => import('./components/core/Settings'),
      CoreView: () => import('./components/core/View'),
    },
    data: () => ({
      expandOnHover: false,

    }),    
    
    mounted () {
      this.$store.dispatch('gShowMeAct', true)
    },
    created () {
      this.$store.dispatch('gShowMeAct', true)
    },
  }
</script>
