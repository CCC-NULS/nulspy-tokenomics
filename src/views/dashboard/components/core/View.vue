<template>
  <v-main>
    <router-view />
  
    <Home />

    <CoreFooter />
  </v-main>
</template>

<script>
  import {  mapState  } from 'vuex'
  this.$store.commit('gShowMe', true)
  export default {
    name: 'CoreView',

    components: {
      Home: () => import('./Home'),
      CoreFooter: () => import('./Footer'),
    },
  }
</script>
