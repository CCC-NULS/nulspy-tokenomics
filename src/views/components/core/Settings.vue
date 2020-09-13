<template>
  <div id="settings-wrapper">
    <!-- weird dark mode tab in upper right -->
    <v-card
      id="settings"
      class="py-2 px-2"
      color="rgba(117, 201, 181, 0.5)"
      flat
      link
      min-width="70"
      style="position: fixed; top: 0px; right: 200px;"
    >
      <span 
        class="primary--text text--darken2 mt-0"
        style="font-size:12px;"
      >
        Colors
      </span>
      <v-icon medium>
        mdi-settings
      </v-icon>
    </v-card>

    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      activator="#settings"
      bottom
      content-class="v-settings"
      left
      nudge-left="8"
      offset-x
      origin="top right"
      transition="scale-transition"
    >
      <v-card
        class="text-center mb-0 mt-0 pt-2 pb-2 pl-4"
        width="300"
      >
        <v-row
          align="center"
          no-gutters
        >
          <v-col cols="auto">
            Dark Mode
          </v-col>

          <v-spacer />

          <v-col cols="auto">
            <v-switch
              v-model="$vuetify.theme.dark"
              class="ma-0 pa-0"
              color="secondary"
              hide-details
            />
          </v-col>
        </v-row>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
  // Mixins
  import Proxyable from 'vuetify/lib/mixins/proxyable'
  import { mapMutations, mapState } from 'vuex'

  export default {
    name: 'CoreSettings',

    mixins: [Proxyable],

    data: () => ({
      color: '#E91E63',
      colors: [
        '#9C27b0',
        '#00CAE3',
        '#4CAF50',
        '#ff9800',
        '#E91E63',
        '#FF5252',
      ],
      image: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
      images: [
        'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
        'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-2.jpg',
        'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-3.jpg',
        'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-4.jpg',
      ],
      menu: false,
      saveImage: '',
      showImg: true,
    }),

    computed: {
      ...mapState(['barImage']),
    },

    watch: {
      color (val) {
        this.$vuetify.theme.themes[this.isDark ? 'dark' : 'light'].primary = val
      },
      showImg (val) {
        if (!val) {
          this.saveImage = this.barImage
          this.setBarImage('')
        } else if (this.saveImage) {
          this.setBarImage(this.saveImage)
          this.saveImage = ''
        } else {
          this.setBarImage(val)
        }
      },
      image (val) {
        this.setBarImage(val)
      },
    },

    methods: {
      ...mapMutations({
        setBarImage: 'SET_BAR_IMAGE',
      }),
    },
  }
</script>

<style lang="sass">
  .v-settings
    .v-item-group > *
      cursor: pointer

    &__item
      border-width: 3px
      border-style: solid
      border-color: transparent !important

      &--active
        border-color: #00cae3 !important
</style>
