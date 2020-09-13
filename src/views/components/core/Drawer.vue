<template>
  <v-navigation-drawer
    id="core-navigation-drawer"
    v-model="drawer"
    class="gradientnuls2"
    :expand-on-hover="expandOnHover"
    :right="$vuetify.rtl"
    :dark="barColor !== 'rgba(228, 226, 226, 1), rgba(255, 255, 255, 0.7)'"
    mobile-breakpoint="960"
    app
    :width="`twidth`"
    v-bind="$attrs"
  >
    <!-- v-slot:img below does drawer expand -->
    <template v-slot:img="props">
      <v-img
        v-bind="props"
      />
    </template>
    <!-- begin top nav -->
    <v-list
      dense
      nav
    >
      <v-list-item>
        <v-list-item-avatar
          class="align-self-center"
          contain
        >
          <v-img
            src="@/assets/images/nulsWhiteLogo40.jpg"
            max-height="45"
          />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title
            class="display-1"
            v-text="profile.title"
          />
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mb-2" />

    <v-list
      expand
      nav
      dark
    >
      <template v-for="(item, i) in computedItems">
        <item-group
          v-if="item.children"
          :key="`group-${i}`"
          :item="item"
        >
          <!--  -->
        </item-group>
        <item
          v-else
          :key="`item-${i}`"
          :item="item"
        />
      </template>
    </v-list>
    <v-spacer />
    <!-- CLOSE DRAWER IN MOBILE --> 
    <v-btn
          class="mr-0 ml-0"
          style="margin-top:300px;"
          color="rgba(117, 201, 181, 0.5)"
          elevation="1"
          medium
          flat
          @click="setDrawer(!drawer)"
        >
          Close
          <v-icon v-if="value">
            mdi-swap-horizontal
          </v-icon>

          <v-icon 
            v-else
            class="pl-4"
          >
            mdi-swap-horizontal
          </v-icon>
        </v-btn>
        <!-- <v-toolbar-title
          class="hidden-sm-and-down font-weight-light"
          v-text="$route.name"
        /> -->

    <template v-slot:append>
      <item
        dark
        :item="{
          title: $t(''),
          icon: 'mdi-package-up',
          to: '/',
        }"
      />
    </template>
  </v-navigation-drawer>
</template>

<script>   

  import {  mapState, mapMutations  } from 'vuex'
  export default {
    name: 'CoreDrawer',
    props: {
      expandOnHover: {
        type: Boolean,
        default: false,
      },
    },

    data: () => ({
      items: [
       {
          title: 'home',
          icon: 'mdi-poll',
          to: '/',
        },       
        {
          title: 'tokenomics',
          icon: 'mdi-electron-framework',
          to: '/tokenomics',

        },
        // {
        //   title: 'createcs',
        //   icon: 'mdi-chart-areaspline',
        //   to: '/pages/createcs',
        // },           
      ],
    }),

    computed: {
      ...mapState(['drawer']),
      ...mapState(['barColor', 'barImage']),
      drawer: {
        get () {
          return this.$store.state.drawer
          },
        set (val) {
          this.$store.commit('SET_DRAWER', val)
          },
        },
        twidth () {
          return window.outerWidth < 960 ? 200 : 260   
        },
      computedItems () {
        return this.items.map(this.mapItem)
      },
      profile () {
        return {
          avatar: true,
          title: this.$t('avatar'),
        }
      },
    },
    methods: {
      ...mapMutations({
        setDrawer: 'SET_DRAWER',
      }),
      mapItem (item) {
        return {
          ...item,
          children: item.children ? item.children.map(this.mapItem) : undefined,
          title: this.$t(item.title),
        }
      },
    },
  }
</script>

<style lang="sass">
  @import '~vuetify/src/styles/tools/_rtl.sass'

  #core-navigation-drawer
    .v-list-group__header.v-list-item--active:before
      opacity: .24
    .v-list-item
      &__icon--text,
      &__icon:first-child
        justify-content: center
        text-align: center
        width: 20px
        +rtl()
          margin-left: 24px
          margin-right: 12px !important

    .v-list--dense
      .v-list-item
        &__icon--text,
        &__icon:first-child
          margin-top: 10px

    .v-list-group--sub-group
      .v-list-item
        +rtl()
          padding-right: 8px

      .v-list-group__header
        +rtl()
          padding-right: 0
        .v-list-item__icon--text
          margin-top: 19px
          order: 0
        .v-list-group__header__prepend-icon
          order: 2
          +rtl()
            margin-left: 8px
  .gradientnuls2
    background-image: linear-gradient(306deg, grey, black)
</style>
