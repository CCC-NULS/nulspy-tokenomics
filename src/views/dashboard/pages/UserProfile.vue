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
                  @click="getStarted(vmd1, vmd2, vmd3, vmd4, vmd5)"
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
        <base-material-card
          id="plotdiv"
          name="plotdiv"
          width="92%"
        >
          <tplotmain />    
          <tplotWatchme
            v-show="false"
          />    

          <v-card 
            color="success"
            class="padbotcard"
            elevation-24
            raised
          >
            <v-btn id="redobtn">
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
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->

<script>
  import axios from 'axios'
  import { mapState, mapMutations, mapActions } from 'vuex'
  import TopWords from '@/views/dashboard/components/TopWords'
  // import tplotmain from '@/assets/plots/tempPlotmain.vue'  //temp placeholder
  import tplotWatchme from '@/assets/plots/plotmain.svg'
  // import tplotmain from $router

  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    name: 'UserProfilePage',
    components: {
      TopWords,
      tplotmain,
      tplotWatchme,
    },

    data: () => ({
      // formvmodel: '',
      // componentKey: 0, 
      myShowPlot: '',  // must be this to be "reactive"
      plotsSaved: [],
      chipprops: {
        class: "v_chip_small",
        small: true,
        dark: false,
      },
      vmd1: '',
      vmd2: '',
      vmd3: '',
      vmd4: '',
      vmd5: '',
      initsupply: ["100,000,000", "700,000", "500,000", "300,000"],
      aninflation: ["200,000", "300,000", "400,000", "500,000"],
      inflatervals: ["12", "18", "24", "36", "48"],
      stopinflation: ["400,000", "450,000", "500,000", "600,000", "700,000"],
      disinflation: ["3", "4", "5"],
    }),

    mounted () {
      console.log("val gShowPlot in store: " + this.$store.state.gShowPlot);
      myShowPlot: false;
      },

    methods: {
      storePlotNames: function (plotNameLocc, locPlotPathe) {
        this.$store.dispatch('gLocPlotNameAct', plotNameLocc)
        this.$store.dispatch('gLocPlotPathAct', locPlotPathe)
        this.$store.dispatch('gShowPlotAct', true)
        console.log('just ran storePlotName and path')

        console.log('state.gLocPlotPath: ' + this.$store.state.gLocPlotPath )
        console.log('state.gTimeStamp: ' + this.$store.state.gTimeStamp )
        console.log('state.gShowplot: ' + this.$store.state.gShowPlot )
        console.log("!!! local locPlotPath: " + locPlotPathe )
        console.log("!!! local plname: " + plotNameLocc)
      },
      repl: function (pfilename) {
        // pfilename: 'plotmain2.svg',
        this.$router.replace({ 
          name: 'plotmain',
          id: 'pmid',
          pfilename: pfilename,
          // // path: 'assets/plots',
          // tpath: '@/assets/plots/:pfilename', 
          // component: () => import(tpath),
        })
      console.log("here")
      },       
      makePlotTwo: function (baseurl) {
        console.log('inside makePlotTwo')

        ;(async () => {
          let response = await axiosi({
            url: baseurl,
            method: "get",
          })
        })()
      },
      makePlot: function (aa, bb, c, dd, e, plname, timestpLong) {
        console.log('inside makePlot function');
        // const self = this
        // let aaa = aa.replace(',', '')
        // let aw = '&initsup=' + aaa.replace(',', '')
        // let bw = '&anninf=' + bb.replace(',', '')
        // let cw = '&startinf=' + c
        // let dw = '&stopinf=' + dd..replace(',', '')
        // let ew = '&disinf=' + e
        // need to remove comma's twice from a

        let aw = "&initsup=100000000"
        let bw = "&anninf=500000" 
        let cw = "&startinf=24"
        let dw = "&stopinf=500000"
        let ew = "&disinf=5"    
        let requestVars = aw + bw + cw + dw + ew + timestpLong
        let baseurl = "http://localhost:5002/getpy?" + requestVars
        let locPlotPath = "@/assets/plots/" + plname
        this.storePlotNames(plname, locPlotPath)
        console.log("!!!baseurl: " + baseurl)   
        this.makePlotTwo(baseurl); 
        this.repl('plotmain2.svg')
      },

      getStarted: function (a, b, c, d, e) {
        console.log('inside timestring function');
        const timestr = Date.now().toString().substring(5,13);
        this.$store.dispatch("gTimeStampAct", timestr);
        console.log("timestr: " + timestr);
        const timestpLg = "&timestp=" + timestr
        let plname = "plot" + timestr + ".svg"
        this.makePlot(a, b, c, d, e, plname, timestpLg);
      },

      keepplot: function () {
        let pname = this.$store.state.gLocPlotPath
        const count = plotsSaved.push(pname);
        this.$store.dispatch('gPlotListAct', plotsSaved);
        console.log('Inside keepplot. Plots pushed: ' + count)
        console.log(plotsSaved)
      },
    },
  }
</script>

<style src="@/assets/styles/mystyle.css">
  .padbotcard {
    margin-top: 1px!important;
    padding-top: 7px;
    padding-bottom: 7px;
    display: flex;
    align: top;
    justify-content: center;
  }
</style>

    //   AsyncComponent: () => ({
    //     // The component we want to load.
    //     component: AsyncComponent,
    //     // The component to use as a placeholder while the
    //     // async component is loading.
    //     loading: AsyncLoading,
    //     // The component to render instead if there is an error
    //     // loading the async component.
    //     error: AsyncLoadError,
    //     // The delay before the loading component is shown.
    //     delay: 100,
    //     // If this timeout is reached, the async component is considered
    //     // to have failed loading.
    //     timeout: 5000
    //   }),
    // },    
