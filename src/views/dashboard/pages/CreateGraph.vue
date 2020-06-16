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
                  @submit.prevent
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
          id="plotcard"
          class="padplot"
          pl-2
          elevation-24
          raised
        >
          <pltreal
            id="therealplot"
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
    <v-card id="testcard">
      <pic
        testcard
      />
    </v-card>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
  import Vue from 'vue'
  import axios from 'axios'
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import pltreal from '@/assets/plots/pltreal.svg'
  import TopWords from '@/views/dashboard/components/TopWords'
  const acceptStr = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
  const restTypes = 'GET, POST, HEAD, UPDATE, PUT'  
  const axiosi = axios.create({ 
    defaults: {
      headers: {
        get: { 'Accept': acceptStr, 'Access-Control-Allow-Methods': restTypes,
         'Content-Type': 'application/json' },
        common: { 'Access-Control-Allow-Origin':  '*'}
      } }
    });

  var showtrue = false;
  var nm = 'pb'
  self = this
  const pic = (async () => { 
            var p = (await require(`./${nm}.svg`));
            return p
            }) 
            
  var d = async () => { await require(`./${nm}.svg`) }
             
  export default {
    components: {
      TopWords,
      pltreal,
      pic,
    },    
    data: () => ({     // '' must be this to be "reactive"
      chipprops: {
        class: "v_chip_small", small: true, dark: false,
      },
      showtrue,
      showMagicHat: false,
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
      mypic (nm) {
        try { 
          console.log('inside asyncReqSvg: ' + nm)
          ;(async () => { 
            var icon = (await import(`./${nm}.svg`));
            }) ()
        }
          catch (e)
              {  throw err;
          } finally { 
          }
        return icon 
      },    
    },
    watch: {
      showMagicHat(value) {
        if (value) {
          mycontext => require.context('../../../assets/plots', false, /\.svg$/)
        }
      },
    },
    methods: {
      asyncReqSvg2(nm) {
        try { 
          console.log('inside asyncReqSvg: ' + nm)
          ;(async () => { 
            var icon = (await import(`./${nm}.svg`));
            }) ()
        }
          catch (e)
              {  throw err;
          } finally { 
          return icon }
      },    
      svgLoaded () {
        console.log('Inline SVG is loaded!')
      },
      getSessStr() {
        let gsess = this.$store.state.gSessionStr
        if (gsess.length < 2) { // nothing there
          gsess = Date.now().toString().substring(7,13);
          this.$store.dispatch('gSessionStrAct', gsess)
        }
        else {
          gsess = this.$store.state.gSessionStr
        }
        this.showtrue = true
        return gsess
      },
      asyncRequestPython (baseurl) {
        try { 
          console.log('inside asyncRequestPython: ' + baseurl)
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
      makePlot (a, b, c, d, e) {
        let sessn = this.getSessStr()
        console.log("sessn in makePlot: " + sessn)
        console.log("a: " + a + "b: " + b + "d: " + d)
        let filetstmp = Date.now().toString().substring(5,13);
        // let bw = '&anninf=' + b.replace(/,/g, '')
        // let cw = '&startinf=' + c
        // let dw = '&stopinf=' + d.replace(/,/g, '')
        let ew = '&disinf=' + e
        // need to remove comma's twice from a, b, d
        let aw = "&initsup=100000000"  // let bw = "&anninf=5000000"   // let cw = "&startinf=24"   // let dw = "&stopinf=210000000"  // let ew = "&disinf=4"    
        let bw = "&anninf=5000000" 
        let cw = "&startinf=24" 
        let dw = "&stopinf=210000000" 
        let longstmp = sessn + filetstmp
        let requestVars = aw + bw + cw + dw + ew + `&timestp=${longstmp}`
          // gDir is the unique directory for each session
        let pythonUrl = `http://localhost:5002/getpy?${requestVars}`
        try {
          this.asyncRequestPython(pythonUrl); 
        }
        catch (e) {
          console.log(e)
        }
        console.log(`The pythonUrl is: ${pythonUrl}`) 
      },
      resetc () {
        console.log("in resetc")
      },
      keepplot () {
        console.log("in keepplot")
      },
    }
  }


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
