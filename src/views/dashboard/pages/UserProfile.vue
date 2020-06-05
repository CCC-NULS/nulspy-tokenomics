<template>
  <v-container
    id="user-profile"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card
          color="tertiary"
        >
          <template v-slot:heading>
            <div
              id="firstdiv"
              shaped
              class="displaynms font-weight-light"
            >
              <TopWords />
            </div>
          </template>

          <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <!--             v-model="formvmodel"   -->

          <v-form
            id="mainform"
            ref="formref"
            @submit.prevent
          >
            <v-container
              id="vcontain"
              class="py-4"
            >
              <v-card
                id="vcardform"
                align="center"
                pr-5
                pl-5
                elevation-15
                raised
              >
                <v-row>
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <v-chip
                      id="choicechip"
                      v-bind="chipprops"
                      class="margleft"
                      elevation-14
                      raised
                    >
                      Make Your Choices:&emsp;
                    </v-chip>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <!-- choice chip:  # # # #  # # # #  # # # #  -->
                    <!--:items="initsupply" -->

                    <v-select
                      id="vselone"
                      v-model="vmd1"
                      class="margleft"
                      type="string"
                      label="Initial Token Supply"

                      :items="initsupply"
                      placeholder="100,000"
                    />
                  </v-col>

                  <!-- annual inflation:  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vseltwo"
                      v-model="vmd2"
                      type="string"
                      label="Annual Inflation"
                      :items="aninflation"
                      placeholder="1,000"
                    />
                  </v-col>
                </v-row>

                <v-row>
                  <!-- annual inflation:  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselthree"
                      v-model="vmd3"
                      type="string"
                      label="Inflation Interval"
                      class="margleft"
                      :items="inflatervals"
                    />
                  </v-col>
                  <!-- stop inflation:  # # # #  # # # #  # # # #  -->

                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselfour"
                      v-model="vmd4"
                      type="string"
                      label="Stop Inflation "
                      :items="stopinflation"
                    />
                  </v-col>

                  <v-col
                    cols="12"
                    md="3"
                  >
                    <!-- disinflation # select # five five:  # # # #  # # # #  # # # #  -->
                    <v-select
                      id="vselfive"
                      v-model="vmd5"
                      type="string"
                      label="Disinflation Ratio %"
                      class="margright"
                      :items="disinflation"
                    />
                  </v-col>
                </v-row>

                <v-btn
                  id="submitmain"
                  type="submit"
                  size="large"
                  color="warning"
                  @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                >
                  submitform
                </v-btn>
                <div>  <br>  </div>
              </v-card>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <v-card
          v-if="true"
          id="plotcard"
          :key="$store.state.gCounter"
          class="padplot"
          pl-2
          elevation-24
          raised
        >
          This is the wrapper card

          <plotreal
            v-if="$store.state.gCounter > 1"
            :key="$store.state.gCounter"
          />
        </v-card>

        <v-card 
          id="buttoncard"
          color="success"
          class="padbotcard"
          elevation-24
          raised
        >
          <v-btn 
            id="redobtn"
            @click="resetc"
          >
            Redo
          </v-btn>
          <v-btn
            id="savebtn"
            color="purple"
            @click="keepplot"
          >
            Save
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
  import axios from 'axios'
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import TopWords from '@/views/dashboard/components/TopWords'
  import plotrealv from '@/assets/plots/plotreal.svg'
  
  var acceptStr = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
  var restTypes = 'GET, POST, HEAD, UPDATE, PUT'  
  const axiosi = axios.create({ 
    defaults: {
      headers: {
        get: { 'Accept': acceptStr, 'Access-Control-Allow-Methods': restTypes,
         'Content-Type': 'application/json' },
        common: { 'Access-Control-Allow-Origin':  '*'}
      } }
    });

  const self = this
  var showme
  var plotreal

  export default {
    name: 'UserProfile',
    components: {
      TopWords,
      plotreal: () => import('@/assets/plots/plotreal.svg'),
    },
    data: () => ({     // '' must be this to be "reactive"
      chipprops: {
        class: "v_chip_small", small: true, dark: false,
      },
      showme: false,
      vmd1: '',
      vmd2: '',
      vmd3: '',
      vmd4: '',
      vmd5: '',
      initsupply: ["300,000,000","260,000,000","225,000,000","200,000,000", "175,000,000","150,000,000","100,000,000",],
      aninflation: ["2,000,000", "3,000,000", "4,000,000", "5,000,000", "6,000,000"],
      inflatervals: ["12", "18", "24", "36", "48"],
      stopinflation: ["510,000,000","450,000,000","350,000,000", "310,000,000", "250,000,000", "155,000,000", "120,000,000"],
      disinflation: ["3", "4", "5"],
    }),
    computed: {
      computeshowval () {
        let theretval = false
        let check_gctc =  this.$store.state.gCounter
        console.log('In computeshowval: gCounter now: ' + check_gctc)
        if (check_gctc > 1)
          theretval = true         
        console.log('value of theretval in computeshowval: ' + theretval)
        return theretval
      },
    },
    watch: {
      plotreal:  {
        deep: true,
        immediate: true,
        handler () {
          console.log("!!! &&&&  &&&&  WATCH plotdir route change!!  ---------  ")
          let gct  =  this.$store.state.gCounter
          console.log("In watch: gCounter: " +  gct )
          gct += 1
          this.$store.dispatch('gCounterAct', gct)

          let check_gct  =  this.$store.state.gCounter
          console.log('In watch: gCounter now: ' + check_gct)

          this.showme = this.computeshowval

          console.log("value of showme in handler: " + this.showme)
        }         
      },
    },

    created () {
      // this.$router.go()
      console.log("in created" )
      this.$store.dispatch('showmeAct', false)
    },
    mount () {
      // this.$router.go()
      console.log("in mount" )
      this.$store.dispatch('showmeAct', false)
    },
    updated () {
      console.log("in updated" )
    },
    activated () {
      console.log("in activated" )
    },
   
    methods: {
      resetc: function () {
        let gctt  =  self.$store.state.gCounter
        console.log("In resetc: myCounter: " +  gctt )
        ++gctt
        self.$store.dispatch('gCounterAct', gctt)  // start over
        let mctt  =  self.$store.state.gCounter
        console.log("In resetc:  myCounter now: " + mctt)
      },
      storeTimedPlotNames: function (plot_name, plot_name_path) {
        this.$store.dispatch('gTimeNAMEonlyAct', plot_name)
        this.$store.dispatch('gTimedPlotPathAct', plot_name_path)
        console.log('chkg store: gTimedPlotPath: ' + this.$store.state.gTimedPlotPath )
        console.log("plot_name_path: " + plot_name_path + ": " + plot_name)
      },
      asyncRequestPlot: function (baseurl) {
        try { 
          console.log('inside asyncRequestPlot')
          ;(async () => {
            let response = await axiosi({
              url: baseurl,
              method: "get",
              })
            })()
        }
        catch (e) {
          console.log(e)
        }
      },
      makePlot: function (a, b, c, d, e) {
        console.log("a: " + a + "b: " + b + "d: " + d)
        const timestr = Date.now().toString().substring(5,13);
        let plotname_t = "plot" + timestr + ".svg"
        let plotname_t_path = "@/assets/plots/" + plotname_t
        this.storeTimedPlotNames(plotname_t, plotname_t_path)
        // let bw = '&anninf=' + b.replace(/,/g, '')
        // let cw = '&startinf=' + c
        // let dw = '&stopinf=' + d.replace(/,/g, '')
        let ew = '&disinf=' + e
        // need to remove comma's twice from a, b, d

        let aw = "&initsup=100000000"  // let bw = "&anninf=5000000"   // let cw = "&startinf=24"   // let dw = "&stopinf=210000000"  // let ew = "&disinf=4"    
        let bw = "&anninf=5000000" 
        let cw = "&startinf=24" 
        let dw = "&stopinf=210000000" 
        let requestVars = aw + bw + cw + dw + ew + "&timestp=" + timestr
        let pythonUrl = "http://localhost:5002/getpy?" + requestVars
        try {
          this.asyncRequestPlot(pythonUrl); 
        }
        catch (e) {
          console.log(e)
        }
        console.log(`!!! pythonUrl: ${pythonUrl}`)   
      },
      keepplot: function () {
        let timePlotPath = this.$store.state.gTimedPlotPath
        this.$store.dispatch('gPlotPATHARRAYpushAct', timePlotPath);
        this.$store.dispatch('gCounterAct', 1)  // reset start mostly over
        console.log('pushed new val onto gPlotPATHARRAY: ' + this.$store.state.gPlotPATHARRAY)
      },
    }
  }
  //    gTimeNAMEonly: '',
    // gTimedPlotPath: '',
    // gPlotPATHARRAY: [],
// Before create
// Created
// Before mount
// Mounted
// Before update
// Updated
// Before destroy
// Destroyed
</script>
<style src="@/assets/styles/mystyle.css">
</style>
