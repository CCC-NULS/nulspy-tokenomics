<template>
  <v-app-bar
    id="app-bar"
    absolute
    app
    color="grey lighten-4"
    flat
    height="75"
  >
    <v-btn
      class="ml-3 mr-6"
      elevation="1"
      fab
      small
      @click="setDrawer(!drawer)"
    >
      <v-icon v-if="value">
        mdi-restart
      </v-icon>

      <v-icon v-else>
        mdi-dots-vertical
      </v-icon>
    </v-btn>
   
    <!-- <v-btn
      class="mr-1"
      style="margin-left:400px!important;"
      color="rgba(117, 201, 181, 0.5)"
      elevation="99"
      medium
      @click="setDrawer(!drawer)"
    >
      close this menu
      <v-icon v-if="value">
        mdi-close
      </v-icon>

      <v-icon v-else>
        mdi-close
      </v-icon>
    </v-btn>
    <v-toolbar-title
      class="hidden-sm-and-down font-weight-light"
      v-text="$route.name"
    /> -->


    <v-spacer />
    <!-- removed text search from here  -->

    <div class="mx-0" />

    <v-btn
      class="ml-2"
      color="primary"
      
      shaped
      filled="true"
      text
      dark
      large
      href="https://nuls.io"
    > 
      NULS <pre>&emsp;</pre> 
    </v-btn>
  </v-app-bar>
</template>

<script>
  // Components
  import { VHover, VListItem } from 'vuetify/lib'

  // Utilities
  import { mapState, mapMutations } from 'vuex'

  export default {
    name: 'CoreAppBar',

    components: {
    },

    props: {
      value: {
        type: Boolean,
        default: false,
      },
    },

    data: () => ({
      rlabel: "Restart",
      notifications: [
      ],
    }),

    computed: {
      ...mapState(['drawer']),
    },

    methods: {
      ...mapMutations({
        setDrawer: 'SET_DRAWER',
      }),
    },
  }
</script>
<style scoped>
  .v-btn.v-size--large { 
    font-size: 16px; 
  }
</style>
