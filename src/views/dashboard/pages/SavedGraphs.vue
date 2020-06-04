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

            <testcomp 
              v-show="true"
              :key="splotkeyone"
              ponewrap
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
          <testcomptwo />

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

  var showonecomp = true
  var showtwocomp = false
  var splotkeyone = 0

  var pltone = 'plote.svg'
  var myplotnewone = '@/assets/plots/plote.svg'
  var myplotnametwo = '@/assets/plots/plote.svg'
    // return require('@/assets/icons/icon_${name}.svg).default;
  
  const self = this

  const testcomp = require(myplotnewone).default;
  const testcomptwo = require(myplotnewone).default;

  export default {
    name: "SavedGraphs",
    components: {
      testcomp,
      testcomptwo,
    },
    data: () => ({
      showonecomp,
      showtwocomp,
      splotkeyone,
      secondsrc: "http://localhost:5002/static/plots/plot00910117.svg",
      thirdsrc: "http://localhost:5002/static/plots/plot00910117.svg",
    }),
    watch: {
      runonebtn:  {
        deep: true,
        immediate: true,
        handler () {
          console.log("!!! runonebtn change in watch !!  ---------  ")
          }         
        },
    },
    created () {
      var plotslist = self.$store.state.gPlotList
      if (plotslist.length > 0) {
        myplotnewone = plotlist[0]
        testcomp = require(myplotnewone).default;

        if (plotslist.length > 1) {
          myplotnametwo = plotslist[1]
          testcomptwo = require(myplotnametwo).default;

        }
      }
    },
    
    methods: {
      loadonenow: function () {
        this.$store.dispatch('sWhichPlotAct', 1);
        let locsplotslist = this.$store.state.gPlotList
        let savonecompname = locsplotslist[1]      
        console.log("!!! beginning splotkeyone: " + splotkeyone)
        console.log("!!! savonecompname: " + savonecompname)
        showonecomp: true
        ++splotkeyone
        console.log("!!! splotkeyone: " + splotkeyone)
      },
      loadtwonow: function () {
        console.log("clicked loadtwonow. ")
        showtwocomp: true
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


// Call router.go() or this.$router.go()
// That will refresh the page and your state will be reset to how it was when the user first loaded the app.


</script>
<style src="@/assets/styles/mystyle.css">
</style>
