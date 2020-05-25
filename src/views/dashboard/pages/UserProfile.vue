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

          <v-form
            id="form"
            ref="form"
            v-model="formvmodel"
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
                  id="submit"
                  type="submit"
                  size="large"
                  color="warning"
                  @click="makeTimeStamp(vmd1, vmd2, vmd3, vmd4, vmd5)"
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
        <div
          v-show="myShowPlot"
          id="plotdiv"
          name="plotdiv"
          width="92%"
        >
          <LastCard2 
            id="lastcard2"
            class="width=90%"
          /> 
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->

<script>
  import axios from 'axios'
  import { mapState, mapMutations } from 'vuex'
  import LastCard2 from '@/views/dashboard/components/LastCard2'
  import TopWords from '@/views/dashboard/components/TopWords'
  let formvmodel = ''
  let myShowPlot = false

  function makeTimeStamp (a, b, c, d, e) {
    console.log("inside timestring method");
    let tss = new Date()
    let ts = tss.valueOf();
    let timestr = ts.toString().substring(5,13);
    this.$store.dispatch('gTimeStampAct', timestr);
    this.myShowPlot = true
    console.log('timestr: ' + timestr);
    this.makePlot(a, b, c, d, e, timestr) 
    };

  // need to remove comma's twice from a
  function makePlot (aa, bb, c, dd, e, timestp) {
    const self = this
    // let aaa = aa.replace(',', '')
    // let a = aaa.replace(',', '') 
    // let b = bb.replace(',', '')
    // let d = dd.replace(',', '')
    // let aw = '&initsup=' + a
    // let bw = '&anninf=' + b
    // let cw = '&startinf=' + c
    // let dw = '&stopinf=' + d
    // let ew = '&disinf=' + e
    let aw = '&initsup=100000000'
    let bw = '&anninf=500000' 
    let cw = '&startinf=24'
    let dw = '&stopinf=500000'
    let ew = '&disinf=5'    
    
    console.log("gtime is: " + timestp)
    let timestpLong = '&timestp=' + timestp
    let requestVars = aw + bw + cw + dw + ew + timestpLong
    let baseurl = 'http://localhost:5002/getpy?' + requestVars
    console.log("baseurl is: " + baseurl)
    let plname = 'plot' + timestp + '.svg'
    let locPlotPath = '@/assets/plots/plotmain.svg' // for testing
    let locPlotPathTS = '@/assets/plots/' + plname + '.svg'

    this.$store.dispatch('gLocPlotPathAct', locPlotPath)
    self.makePlotTwo(baseurl, locPlotPath);
    setTimeout(console.log("timeout 1.5 seconds for chart to be made"), 1500);
    this.$store.dispatch('gShowPlotAct', true)
    console.log("state.gShowplot: " + this.$store.state.gShowPlot )
    console.log("state.gLocPlotPath: " + this.$store.state.gLocPlotPath )
    console.log("state.gTimeStamp: " + this.$store.state.gTimeStamp )
  };

  const chipprops = {
    class: 'v_chip_small',
    small: true,
    dark: false,
  }

  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT, DELETE'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    components: {
      TopWords,
      LastCard2,
    },
    data: () => ({
      myShowPlot,
      chipprops,
      formvmodel,
      vmd1: '',
      vmd2: '',
      vmd3: '',
      vmd4: '',
      vmd5: '',
      initsupply: ['100,000,000', '700,000', '500,000', '300,000'],
      aninflation: ['200,000', '300,000', '400,000', '500,000'],
      inflatervals: ['12', '18', '24', '36', '48'],
      stopinflation: ['400,000', '450,000', '500,000', '600,000', '700,000'],
      disinflation: ['3', '4', '5'],
    }),
    computed: {
      // myShowPlot: this.$store.state.gShowPlot,
      // ...mapState(['gLocPlotPath', 'gShowPlot', 'gTimeStamp']),
    },
    methods: {
      makeTimeStamp,
      makePlot,
      makePlotTwo: function (baseurl) {
        ;(async () => {
          let response = await axiosi({
            url: baseurl,
            method: 'get',
          })
        })()
      },
    }
  }
</script>

<style src="@/assets/styles/mystyle.css">
</style>
