<template>
  <v-main>
    <router-view />

    <Footer />
  </v-main>
</template>

<script>
  import {  mapState  } from 'vuex'
  export default {
    name: 'CoreView',

    components: {
      Footer: () => import('./Footer'),
    },
  }
</script>
