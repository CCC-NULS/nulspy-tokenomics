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
        <v-card>
          <plotempty />
        </v-card>

        <v-card
          v-show="$store.state.gShowPlot"
        >
          <plotreal />
        </v-card>

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
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
  import axios from 'axios'
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import TopWords from '@/views/dashboard/components/TopWords'
  import plotreal from '@/assets/plots/comps/plotreal.svg'
  import plotempty from '@/assets/plots/comps/plotempty.svg'  
  
  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
  const timestr = Date.now().toString().substring(9,12)
  const plotdir = '@/assets/plots/comps/'


  export default {
    name: 'UserProfilePage',
    components: {
      TopWords,
      plotreal,
      plotempty,
    },
    data: () => ({
                  // '' must be this to be "reactive"
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
      aninflation: ["2000", "3000", "40,000", "50,000"],
      inflatervals: ["12", "18", "24", "36", "48"],
      stopinflation: ["400,000", "450,000", "500,000", "600,000", "700,000"],
      disinflation: ["3", "4", "5"],
    }),
    watch: {
      plotdir: function() {
        console.log("!!! &&&&  &&&&  saw plotreal route change!!  ---------  ")
      },
      plotreal: function() {
        console.log("!!! &&&&  &&&&  saw plotreal route change!!  ---------  ")
      },
    },
    //   $route: function() {
    //     if (this.$route.path === "assets/plots/comps") {
    //       console.log("!!!  saw route change!!  ---------  ")
    //         //   this.$refs.page1expantion.show();
    //         //   } else  {
    //         // this.$refs.page1expantion.hide();
    //       }
    //     }
    //   },

    mount () {
      this.$store.dispatch('gShowPlotAct', false)
    },
    methods: {
      storeTimedPlotNames: function (plot_name, plot_name_path) {
        this.$store.dispatch('gLocPlotNameAct', plot_name)
        this.$store.dispatch('gLocPlotPathAct', plot_name_path)
        console.log('checking store: state.gLocPlotPath: ' + this.$store.state.gLocPlotPath )
        console.log("!!! local plot_name_path: " + plot_name_path )
        console.log("!!! local plot_name: " + plot_name)
        this.$store.dispatch('gShowPlotAct', true)
      },
      runAsyncGet: function (baseurl) {
        console.log('inside runAsyncGet')
        ;(async () => {
          let response = await axiosi({
            url: baseurl,
            method: "get",
          })
        })()
      },
      makePlot: function (aa, bb, c, dd, e) {
        console.log("aa: ", aa)
        console.log("bb: ", bb)
        console.log("dd: ", dd)

        const timestr = Date.now().toString().substring(5,13);
        let plotname_t = "plot" + timestr + ".svg"
        let plotname_t_path = "@/assets/plots/" + plotname_t
        this.storeTimedPlotNames(plotname_t, plotname_t_path)

        // let aaa = aa.replace(',', '')
        // let aw = '&initsup=' + aaa.replace(',', '')
        // let bw = '&anninf=' + bb.replace(',', '')
        // let cw = '&startinf=' + c
        // let dw = '&stopinf=' + dd.replace(',', '')
        // let ew = '&disinf=' + e
        // need to remove comma's twice from a

        let aw = "&initsup=100000000"
        let bw = "&anninf=5000" 
        let cw = "&startinf=24"
        let dw = "&stopinf=50000"
        let ew = "&disinf=5"    
        let requestVars = aw + bw + cw + dw + ew + "&timestp=" + timestr
        let baseurl = "http://localhost:5002/getpy?" + requestVars
        this.runAsyncGet(baseurl); 
        console.log("!!!baseurl: " + baseurl)   
      },

      keepplot: function () {
        let pname = this.$store.state.gLocPlotPath
        let count = plotsSaved.push(pname);
        this.$store.dispatch('gPlotListAct', plotsSaved);
        console.log('keepplot plots: ' + count + " " + plotsSaved)
      },
    }
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
  // const AsyncComponent = new Promise((resolve, reject) => {
  //   import('@/assets/plots/plotmain.svg') 
  //   }) 
  