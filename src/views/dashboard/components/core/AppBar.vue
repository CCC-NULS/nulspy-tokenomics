<template>
  <v-app-bar
    id="app-bar"
    absolute
    app
    color="transparent"
    flat
    height="75"
  >
    <v-btn
      class="mr-3"
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

    <v-toolbar-title
      class="hidden-sm-and-down font-weight-light"
      v-text="$route.name"
    />

    <v-spacer />
    <!-- removed text search from here  -->

    <div class="mx-3" />

    <v-btn
      class="ml-2"
      color="teal lighten-1"
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
    name: 'DashboardCoreAppBar',

    components: {
      // AppBarItem: {
      //   render (h) {
      //     return h(VHover, {
      //       scopedSlots: {
      //         default: ({ hover }) => {
      //           return h(VListItem, {
      //             attrs: this.$attrs,
      //             class: {
      //               'black--text': !hover,
      //               'white--text secondary elevation-12': hover,
      //             },
      //             props: {
      //               activeClass: '',
      //               dark: hover,
      //               link: true,
      //               ...this.$attrs,
      //             },
      //           }, this.$slots.default)
      //         },
      //       },
      //     })
      //   },
      // },
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
        // 'You sold',
        // 'Another Notification',
        // 'Another one',
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
