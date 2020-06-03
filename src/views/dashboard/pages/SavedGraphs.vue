<template>
  <v-container
    id="google-maps"
    fluid
    tag="section"
  >
    <v-row>
      <v-col cols="12">
        <base-material-card
          color="success"
          title="Graph"
          class="px-5 py-3"
        >
          <v-card
            v-show="$store.state.sCounter > -1"
            id="splotcard"
            class="padplot"
            elevation-24
            raised
            margin-left="4px!important"
            padding-left="2px!important"
            margin-top="4px!important"
            margin-bottom="4px!important"
          >
            <plotone_comp 
              v-show="$store.state.sCounter > -1"
              :pkey="splotkey"
              splotcard
              margin-left="12px!important"
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
          title="Graph"
          class="px-5 py-3"
        >
          <v-card
            margin-left="9px"
            max-width="95%"
          >
            <v-btn
              @click="loadnow"
            >
              Load Now
            </v-btn>

            <savone_comp 
              v-if="showcomp" 
              max-width="95%"
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
          <v-card-text class="px-0 pb-0">
            Old links
          </v-card-text>
        </base-material-card>
      </v-col>
      <savtwo_comp v-show="false" />
      <plottwo_comp v-show="false" />
    </v-row>
  </v-container>
</template>

<script>
    // <spthree v-show="false" />
    // <plottwo_comp v-show="false" />
    // <plotthree_comp v-show="false" />
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import plotone_comp from '@/assets/plots/plotempty.svg'
  import plottwo_comp from '@/assets/plots/plotempty.svg'
  import plotthree_comp from '@/assets/plots/plotempty.svg'
  import savone_comp from '@/assets/plots/plotempty.svg'
  import savtwo_comp from '@/assets/plots/plotempty.svg'
  // var savonecompname = '@/assets/plots/' + 'plot86007891.svg'
  var plotsvg = 'plot86007891.svg'
  var savonecompname = `@/assets/plots/${plotsvg}`
  var savtwocompname = `@/assets/plots/${plotsvg}`
  var showcomp = false
  var splotslist
  var splotslen
  var splotkey = 0

export default {
  name: "SavedGraphs",
  components: {
    savone_comp,
    savtwo_comp,
    plotone_comp,
    plottwo_comp,
    // plotthree_comp,
    savone_comp: () => import(savonecompname),  // async dynamic load works
    // savtwo_comp: () => import(savtwocompname)  // async dynamic load works
    // savthree_comp: () => import(savthreecompname)  // async dynamic load works
  },
  data: () => ({
    isActive: false,
    showcomp,
    splotkey,
    secondsrc: "http://localhost:5002/static/plots/plot00910117.svg",
    thirdsrc: "http://localhost:5002/static/plots/plot00910117.svg",
  }),

  watch: {
    plotdirr:  {
      deep: true,
      immediate: true,
      handler () {
        console.log("!!! &&&&  &&&&  saw plotdirr route change!!  ---------  ")
        }         
      },
  },
  updated () {
    locsplotslist = this.$store.state.gPlotList
    savonecompname = locsplotslist[0]

    console.log("savonecompname from list: " + savonecompname)
    console.log("this.splotkey after increment: " + this.splotkey)
  },

  methods: {
    loadnow: function () {
      console.log("clicked loadnow. ")
      showcomp: true

    let splotslist22 = this.$store.state.gPlotList
    let splotslen22 = splotslist22.length
    console.log("!!! &&&& -- splotslist.length: " + splotslen22)
    // ++splotkey
    },
    getvals: function () {
      let a = 1
      splotslist = this.$store.state.gPlotList
      splotslen = splotslist.length
      console.log("!!! &&&& -- splotslist.length: " + splotslen)

      // sptwo = this.$store.state.gPlotList[1],
      // spthree = this.$store.state.gPlotList[2],
    },
  },  
  mount () {
    getvals
    console.log("this.splotkey: " + this.splotkey)
    ++this.splotkey
    
  },
}
</script>
<style src="@/assets/styles/mystyle.css">
</style>
