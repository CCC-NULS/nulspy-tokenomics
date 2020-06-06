<template>
  <v-container
    id="google-maps"
    fluid
    tag="section"
  >
    <v-row>
      <v-col cols="12">
        <base-material-card
          id="mcforrunone"
          color="success"
          title="Graph"
          class="px-5 py-1"
        >
          <v-btn
            id="runonebtn"
          >
            Load ONE Now
          </v-btn>

          <v-card
            id="ponewrap"
            class="padplot"
            elevation-24
            raised
          >
            <!-- %%%%%%%%%%%%%%%% ONE %%%%%%%%%%%%%%%%%%  PLOT ONE ONE ONE 
            <v-lazy>
              <plotonecomp />
            </v-lazy>
            -->
          </v-card>
        </base-material-card>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          id="mcforruntwo"
          color="success"
          title="Graph"
          class="px-5 py-1"
        >
          <v-card
            id="ptwowrap"
            margin-left="9px"
            max-width="95%"
          >
            <v-btn
              id="runtwobtn"
            >
              Load TWO Now
            </v-btn>
            <!-- %%%%%%%%%%%%%%%%% TWO %%%%%%%%%%%%%%%%%%%  PLOT TWO  

            <testcomptwo 
              v-if="false" 
              ptwowrap
            />
                              %%%%%%%%%%%%%%%%%%%%%%%%%    -->
          </v-card>
        </base-material-card>
      </v-col>

      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          color="success"
          title="Inflation / Deflation"
          class="px-5 py-3"
        >
          <v-card-text class="px-0 pb-0">
            this is ptemp {{ a }}
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import { mapState, mapMutations, mapActions } from 'vuex'  
    // return require('@/assets/icons/icon_${name}.svg).default;
  const self = this
  // var plotonecomp
  var plotonecomp = () => import('@/assets/plots/plotempty.svg')
  // var ponen

  const reqSvgs = require.context ( '@/assets/plots', true, /\.svg$/ )

  const svgs = reqSvgs
    .keys ()
    .map ( path => ({ path, file: reqSvgs ( path ) }) )


  export default {
    name: "SavedGraphs",
    components: {
      // plotonecomp: () => import($store.state.gPlotPATHARRAY[0]),
    },
    data: () => ({
      a: 1,
    }),
    computed: {
      // ponen: function() {
      //   return self.$store.state.gPlotPATHARRAY[0]        
      // }
    },
    watch: {
      // plotreal:  {
      //   deep: true,
      //   immediate: true,
      //   handler () {
      //     console.log("!!! &&&&  &&&&  WATCH plotdir route change!!  ---------  ")
      //     let gct  =  this.$store.state.gCounter
      //     console.log("In watch: gCounter: " +  gct )
      //     gct += 1
      //     this.$store.dispatch('gCounterAct', gct)

      //     let check_gct  =  this.$store.state.gCounter
      //     console.log('In watch: gCounter now: ' + check_gct)

      //     this.showme = computeshowval();

      //     console.log("value of showme in handler: " + this.showme)
      //   }         
      // },
    },

    created () {
      console.log("in created2" )

    },
    mount () {
      // this.$router.go()
      console.log("in mount2" )
    },
    updated () {
      console.log("in updated2" )
    },
    activated () {
      console.log("in activated2" )
    },
      // this.$router.go() // big reset

    methods: {
      loadonenow: function () {
        console.log("in loadonenow: ")
      },
      get_name_two: function () {
        let myPATHARRAY = this.$store.state.gPlotPATHARRAY
        let save_two = myPATHARRAY[1]      
        console.log("in get_name_two: " + save_two)
      },
    },  
  }
  //  <v-lazy
  //           v-model="isActive"
  //           :options="{
  //             threshold: .5
  //           }"
  //           min-height="200"
  //           transition="fade-transition"
  //         >

  // reset everything:
  //
    // created () {
    //   this.$vuetify.rtl = true
    //   this.$i18n.locale = 'ar'
    // },

// Call router.go() or this.$router.go()
// That will refresh the page and your state will be reset to how it was when the user first loaded the app.


</script>
<style src="@/assets/styles/mystyle.css">
</style>
