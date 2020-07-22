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
      color="teal"
      text
      dark
      large
      to="/"
    > 
      Reset - Restart <pre>&emsp;</pre> 
      <v-icon>mdi-view-dashboard</v-icon>
    </v-btn>
    <v-chip
      color="mywhitetext"
      flat
    />
    <!-- <v-menu
      bottom
      left
      offset-y
      origin="top right"
      transition="scale-transition"
    >
      <template v-slot:activator="{ attrs, on }">
        <v-btn
          class="ml-2"
          min-width="0"
          text
          v-bind="attrs"
          v-on="on"
        >
          <v-badge
            color="red"
            overlap
            bordered
          >
            <template v-slot:badge>
              <span>5</span>
            </template>

            <v-icon>mdi-restart</v-icon>
          </v-badge>
        </v-btn>
      </template>

      <v-list
        :tile="false"
        nav
      >
        <div>
          <app-bar-item
            v-for="(n, i) in notifications"
            :key="`item-${i}`"
          >
            <v-list-item-title v-text="n" />
          </app-bar-item>
        </div>
      </v-list>
    </v-menu> -->

    <v-btn
      class="ml-2"
      min-width="0"
      text
      to="/"
    >
      <v-icon>mdi-chart-bell-curve-cumulative</v-icon>
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
