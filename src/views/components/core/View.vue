<template>
  <v-main>
    <router-view />
  
    <Home />

    <Footer />
  </v-main>
</template>

<script>
  import {  mapState  } from 'vuex'
  export default {
    name: 'CoreView',

    components: {
      Home: () => import('./Home'),
      Footer: () => import('./Footer'),
    },
  }
</script>
