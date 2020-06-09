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
          v-if="$store.state.gCounter > 0"
          id="plotcard"
          class="padplot"
          pl-2
          elevation-24
          raised
        >
          <pltreal
            v-show="showreal"
            :key="$store.state.gCounter"
            plotcard
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
      <watchedComp 
        v-if="true" 
        id="watchedcomp"
      />
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
  import axios from 'axios'
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import TopWords from '@/views/dashboard/components/TopWords'
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
 

  export default {
    name: 'CreateGraph',
    components: {
      TopWords,
      watchedComp: () => import('@/assets/plots/watchedcomp.vue'),
      pltreal: () => import('@/assets/plots/pltreal.svg'),
    },
    data: () => ({     // '' must be this to be "reactive"
      chipprops: {
        class: "v_chip_small", small: true, dark: false,
      },
      pltreal: '',
      imagepile: '',
      dirname: '',
      plotdirpath: '',
      showreal: false,
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
      makedirname: function () {
        let dirtimestr = Date.now().toString().substring(7,13);
        let dirname = `d${dirtimestr}`
        console.log("dirname=" + dirname)
        return dirname
      },
      geeDirName: function () {
        return this.$store.state.gDirName
      },
      // newestreal : async() => {
      //     return this.plotreal = () => import(newrealfile)
      // },
      // dogImage: function () {
      //   if (!this.selectedDog) {  }
      //   const fileName = this.selectedDog.toLowerCase()
      //   return require(`../assets/doggos/${fileName}.jpg`) // the module request
      // },  getimgs: function (tdir) {   let gDir = this.geeDirName
    //     // require.context ( folder, recurse, pattern )
    //     var images = require.context(`${tdir}`, false, /\.png$/)
    //     console.log("getimgs: " + tdir)
    //     return images
    //     // return images('./' + pet + ".png")   }
    },
    watch: {
      watchedComp:  {
        deep: true,
        immediate: true,
        handler () {
          console.log("!!! &&&&  &&&&  WATCH watchdir route change!!  ---------  ")
          let gct  =  this.$store.state.gCounter + 1
          this.$store.dispatch('gCounterAct', gct)
          let check_gct  =  this.$store.state.gCounter
          console.log('In watch: gCounter now: ' + check_gct)
          if (gct == 3) {
            console.log("gct is: ", gct)
            newrealfile = this.$store.state.gTimedPlotPathAct 
            console.log('just fixed pltreal - count: ' + check_gct)
          }
          }
        }         
      },
    created () {
      console.log("in created" )
      let ndir = this.makedirname
      console.log("made ndir:  " + ndir)
      this.plotdirpath = '@/assets/plots/' + ndir
      this.$store.dispatch('gDirNameAct', ndir)
      this.$store.dispatch('gDirPathAct', this.plotdirpath)

      console.log("set gDirPathAct to: " + this.plotdirpath)
      this.make_timey_dir(ndir)
      console.log("past make_timey_dir")
      // now python make a component to watch
    },
    mount () {
      // this.$router.go()  // big reset
      console.log("in mount" )
      // this.$store.dispatch('showmeAct', false)
    },
    updated () {
      console.log("in updated" )
      let checkgct  =  this.$store.state.gCounter
      console.log('In watch: gCounter now: ' + checkgct)
      if (checkgct > 1) {
        // imagepile = this.getimgs(this.plotdir)
        console.log('just got results')
      }
    },
    activated () {
      console.log("in activated" )
    },
   
    methods: {
      reimportWatchComp: function () {
        let thedir = this.plotdirpath
        console.log("inside reorientWatchComp - thedir: " + thedir)
        let thefile = thedir + "/watchedComp.vue"
        console.log("thedir: " + thefile)
        this.watchedComp = () => import(thefile)
        console.log("updated watchComp: " + thefile)
        let gcct  =  this.$store.state.gCounter + 1
        console.log("In reimportWatchComp: gCounter incremented: " +  gcct )
        this.$store.dispatch('gCounterAct', gcct)
        let checkgcct  =  this.$store.state.gCounter
        console.log('In reimportWatchComp: gCounter now: ' + checkgcct)

      },
      loadrealplot: function (realname) {
        async doThis => {
          await this.getAsync(realname)
        }
        this.showreal = true
      },
      getAsync : async(newrealfile) => {
          this.pltreal = () => import(newrealfile)
      },
      getimgs: function (tdir) {
        // require.context ( folder, recurse, pattern )
        var images = require.context(`${tdir}`, false, /\.png$/)
        console.log("getimgs: " + tdir)
        return images
        // return images('./' + pet + ".png")
      },
      resetc: function () {
        let gctt  =  this.$store.state.gCounter + 1
        this.$store.dispatch('gCounterAct', gctt)  // start over
        let mctt  =  this.$store.state.gCounter
        console.log("In resetc:  myCounter now: " + mctt)
      },
      storeTimedPlotNames: function (plot_name, plot_name_path) {
        this.$store.dispatch('gTimeNAMEonlyAct', plot_name)
        this.$store.dispatch('gTimedPlotPathAct', plot_name_path)
        console.log('chkg store: gTimedPlotPath: ' + this.$store.state.gTimedPlotPath )
        console.log("plot_name_path: " + plot_name_path + ": " + plot_name)
      },
      asyncRequestPython: function (baseurl) {
        try { 
          console.log('inside asyncRequestPython')
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
      make_timey_dir: function(gDir) {
          console.log(`!!! in make_timey_dir`)  
          // gDir is the unique directory for each session
          let pythonUrld = "http://localhost:5002/getpy?gdir=" + gDir
          try {
            this.asyncRequestPython(pythonUrld); 
          }
          catch (e) {
            console.log(e)
          }
          console.log(`!!! done making dir ${gDir}`)  
      },
      makePlot: function (a, b, c, d, e) {
        this.reimportWatchComp()
        console.log("a: " + a + "b: " + b + "d: " + d)
        const timestr = Date.now().toString().substring(5,13);
        let plotname_t = "plot" + timestr + ".svg"
        let gDir = this.$store.state.gDirName
        let plotname_t_path = "@/assets/plots/" + gDir + "/" + plotname_t
        this.storeTimedPlotNames(plotname_t, plotname_t_path)
        console.log("new plotname_t_path: " + plotname_t_path)

        // let bw = '&anninf=' + b.replace(/,/g, '')
        // let cw = '&startinf=' + c
        // let dw = '&stopinf=' + d.replace(/,/g, '')
        let ew = '&disinf=' + e
        // need to remove comma's twice from a, b, d

        let aw = "&initsup=100000000"  // let bw = "&anninf=5000000"   // let cw = "&startinf=24"   // let dw = "&stopinf=210000000"  // let ew = "&disinf=4"    
        let bw = "&anninf=5000000" 
        let cw = "&startinf=24" 
        let dw = "&stopinf=210000000" 
        let requestVars = aw + bw + cw + dw + ew + "&timestp=" + timestr + "&gdir=" + gDir
          // gDir is the unique directory for each session
        let pythonUrl = "http://localhost:5002/getpy?" + requestVars
        try {
          this.asyncRequestPython(pythonUrl); 
        }
        catch (e) {
          console.log(e)
        }
        console.log(`!!! pythonUrl: ${pythonUrl}`) 
        this.loadrealplot(plotname_t_path);  
      },
      keepplot: function () {
        let timePlotPath = this.$store.state.gTimedPlotPath
        console.log(`keepplot: timePlotPath2 is '${timePlotPath}'`)
        this.$store.dispatch('gPlotPATHARRAYpushAct', timePlotPath);
        console.log('in keepplot: pushed new val onto gPlotPATHARRAY: ' + this.$store.state.gPlotPATHARRAY)

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
