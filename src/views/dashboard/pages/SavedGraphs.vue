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
            <plotonecomp 
              v-show="true"
              :key="splotkeyone"
              ponewrap
            />
          </v-card>
        </base-material-card>
      </v-col>
      <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PLOT TWO  -->
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

            <plottwocomp 
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
          <testcomp />

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
  import plotonecomp from '@/assets/plots/plotone.svg'
  import plottwocomp from '@/assets/plots/plotempty.svg'

  var showonecomp = true
  var showtwocomp = false
  var splotkeyone = 0
  var extraword = 'plote.svg'
  const testcomp = require('@/assets/plots/' + extraword).default;
    // return require('@/assets/icons/icon_${name}.svg).default;
   

export default {
  name: "SavedGraphs",
  components: {
    testcomp,
    plotonecomp,
    plottwocomp,
    // asyncLoad: function () {
    //   var modone
    //   (async () => {
    //     const moduleSpecifier = '@/assets/plots/plotempty.svg';
    //     modone = (await import(moduleSpecifier))
    //     })();
    //   return modone
    // },
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
  
  methods: {
    asyncLoadtwo: function () {
      (async () => {
        const moduleSpecifier = './plotempty.svg';
        const modone = (await import(moduleSpecifier)).default()
        })();
      return modone
    },
    loadonenow: function () {
      this.$store.dispatch('sWhichPlotAct', 1);
      console.log("!!! beginning splotkeyone: " + splotkeyone)
      console.log("clicked loadonenow. ")
      let locsplotslist = this.$store.state.gPlotList
      let savonecompname = locsplotslist[1]
      // plotonecomp: () => import(savonecompname),  // async dynamic load works
      console.log("!!! &&&& savonecompname: " + savonecompname)
      showonecomp: true
      ++splotkeyone
      console.log("!!! splotkeyone: " + splotkeyone)
    },
    loadtwonow: function () {
      console.log("clicked loadtwonow. ")
      // let locsplotslist = this.$store.state.gPlotList
      // let savtwocompname = locsplotslist[1]
      console.log("!!! &&&& still in loadtwonow: ")
      showtwocomp: true
    },
    getvals: function () {
      let splotslist = this.$store.state.gPlotList
      let splotslen = splotslist.length
      console.log("!!! &&&& -- splotslist.length: " + splotslen)
    },
  },  
  mount () {
    console.log("mounted")
  },
}
</script>
<style src="@/assets/styles/mystyle.css">
</style>
