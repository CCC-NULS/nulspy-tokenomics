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
                      v-model="vmodsel1"
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
                      v-model="vmodsel2"
                      type="string"
                      label="Annual Inflation"
                      :items="aninflation"
                      placeholder="100,000"
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
                      v-model="vmodsel3"
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
                      v-model="vmodsel4"
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
                      v-model="vmodsel5"
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
                  @click="makePlot"
                >
                  submitform
                </v-btn>
                <div>  <br>  </div>

                <!--

                <v-btn
                  color="green lighten-1"
                  @click="showPlotNow(true)"
                >
                  Show Plot
                </v-btn>
                <div> <br> </div>

                <   -   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # #
                <  -   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # #


                <v-btn
                  color="purple lighten-1"
                  @click="changeToTrue(false)"
                >
                  Hide Card
                </v-btn>
                <div> <br> </div>
                <v-btn
                  color="green darken-1"
                  @click="changeToTrue(true)"
                >
                  Show Card
                </v-btn>
                <div> <br> </div>
                <v-btn
                  v-show="showButton"
                  id="nmscardid"
                  color="orange"
                >
                  HIDE THIS BUTTON
                </v-btn>
                -->

                <div> <br> </div>
              </v-card>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>

    <LastCard v-show="showPlot" />
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->

<script>
  // import ProfileCardNs from '@/views/dashboard/components/ProfileCardNs'
  // import SecondCard from '@/views/dashboard/components/SecondCard'
  import TopWords from '@/views/dashboard/components/TopWords'
  import LastCard from '@/views/dashboard/components/LastCard'
  import store from '@/store'
  import axios from 'axios'
  import { mapState } from 'vuex'

  const chipprops = {
    class: 'v_chip_small',
    small: true,
    dark: false,
  }
  const initsup = '100000000'
  const anninf = '6000000'
  const startinf = '26'
  const stopinf = '210000000'
  const disinf = '6'
  // let a = '&initsup=' + initsup
  // let b = '&anninf=' + anninf
  // let c = '&startinf=' + startinf
  // let d = '&stopinf=' + stopinf
  // let e = '&disinf=' + disinf
  let fa = '&initsup='
  let fb = '&anninf='
  let fc = '&startinf='
  let fd = '&stopinf='
  let fe = '&disinf='
  let pname = 'empty'
  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT, DELETE'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    components: {
      // ProfileCardNs,
      // SecondCard,
      TopWords,
      LastCard,
    },
    data: () => ({
      chipprops,
      formvmodel: '',
      isHidden: false,
      finalshow: false,
      vmodsel1: '',
      vmodsel2: '',
      vmodsel3: '',
      vmodsel4: '',
      vmodsel5: '',
      initsupply: ['100,000', '200,000', '500,000', '1,000,000'],
      aninflation: ['400,000', '450,000', '500,000', '600,000'],
      inflatervals: ['12', '24', '36', '48'],
      stopinflation: ['400,000', '450,000', '500,000', '600,000', '700,000'],
      disinflation: ['3', '4', '5'],
      showx: true,
      mycolor: 'red',
      whitetxt: 'white--text',
      orangetxt: 'orange--text',
      heavy: 500,
      margbott: '16px',
      myshow: true,
      secondcardshow: false,
      lastcardshow: false,
      pname,
      currentPlotPath: '@/assets/plots/' + pname,
    }),
    computed: {
      ...mapState(['showButton', 'showPlot']),
    },
    methods: {
      changeToTrue: function (theval) {
        this.$store.dispatch('showButtonAct', theval)
      },
      showPlotNow: function (theval) {
        this.$store.dispatch('showPlotAct', theval)
      },
      getTimestamp: function () {
        let timestr = new Date().valueOf().toString().substring(5,13)
        return timestr
      },
      getLocalPlotPath: function (plotname) {
        let timestr = '@/assets/plots/' + plotname
        return plotname
      },
      makePlot: function  (a, b, c, d , e) {
        this.$store.dispatch('showPlotAct', true)
        ggtime = "this.getTimestamp()"
        pname = 'plot' + ggtime + '.svg'
        //let requestVars = a + b + c + d + e + '&timestp=' + ggtime
        let requestVars = a + b + c + d + e + '&timestp=' + ggtime
        let baseurl = 'http://localhost:5002/getpy?' + requestVars
        ;(async () => {
          console.log("inside submitPlot")
          const response = await axiosi({
            url: baseurl,
            method: 'get'
          })
        console.log(response)

        })()
      },
    },

  }
</script>

<style src="@/assets/styles/mystyle.css">
</style>
