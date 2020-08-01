<template>
  <v-main>
    <router-view />
  
    <Home />

    <CoreFooter />
  </v-main>
</template>

<script>
  import {  mapState  } from 'vuex'
  export default {
    name: 'CoreView',

    components: {
      Home: () => import('./Home'),
      CoreFooter: () => import('./Footer'),
    },
  }
</script>
