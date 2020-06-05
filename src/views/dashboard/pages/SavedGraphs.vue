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
            @click="loadonenow"
          >
            Load ONE Now
          </v-btn>

          <v-card
            id="ponewrap"
            class="padplot"
            elevation-24
            raised
          >
            <!-- %%%%%%%%%%%%%%%% ONE %%%%%%%%%%%%%%%%%%  PLOT ONE ONE ONE  -->

            <plotonecomp
              v-if="$store.state.sCounter > 1"
              :key="$store.state.sCounter"
            />
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
              @click="loadtwonow"
            >
              Load TWO Now
            </v-btn>
            <!-- %%%%%%%%%%%%%%%%% TWO %%%%%%%%%%%%%%%%%%%  PLOT TWO  -->

            <testcomptwo 
              v-if="showtwocomp" 
              ptwowrap
            />
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
          <plottwocomp
            v-if="$store.state.sCounter > 1"
            :key="$store.state.sCounter"
          />

          <v-card-text class="px-0 pb-0">
            this is ptemp
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
  var plotonecomp
  var plottwocomp
  // plottwocomp = () => import('@/assets/plots/plotempty.svg')

  export default {
    name: "SavedGraphs",
    components: {
      plotonecomp: () => import(this.$store.state.gPlotPATHARRAY[0]),
      plottwocomp: loadtwo(),
    },
    data: () => ({
      showtwocomp,
      secondsrc: "http://localhost:5002/static/plots/plot00910117.svg",
      thirdsrc: "http://localhost:5002/static/plots/plot00910117.svg",
    }),
    computed: {
      loadtwo () {
        plottwocomp: () => import('@/assets/plots/plotempty.svg')
        let parry = this.$store.state.gPlotPATHARRAY
        if (parry.length > 1)
          plottwocomp: () => import( this.$store.state.gPlotPATHARRAY[1] )
        return plottwocomp
      },
    },
      //   compute_showval () {
      //     let ret_val = false
      //     let check_s_ct =  this.$store.state.sCounter
      //     console.log('In computeshowvcompute_showvalal: gCounter now: ' + check_s_ct)
      //     if (check_s_ct > 1)
      //       ret_val = true         
      //     console.log('value of theretval in compute_showval: ' + ret_val)
      //     return ret_val
      //   },
      // },
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
      cgPATHARRAY = self.$store.state.gPlotPATHARRAY
      cgName_One = cgPATHARRAY[0]
      cgName_Two = cgPATHARRAY[1]

      // this.$router.go()
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
   
    created () {
      // this.$router.go()
      var aPATHARRAY = self.$store.state.gPlotPATHARRAY
      if (aPATHARRAY.length > 0) {
        myplotnewone = aPATHARRAY[0]

        if (aPATHARRAY.length > 1) {
          myplotnametwo = aPATHARRAY[1]

        }
      }
    },
    
    methods: {
      get_name_one: function () {
        let myPATHARRAY = this.$store.state.gPlotPATHARRAY
        let save_one = myPATHARRAY[0]      
        console.log("in get_name_one: " + save_one)

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
