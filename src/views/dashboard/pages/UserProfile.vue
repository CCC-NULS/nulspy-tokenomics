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
                  v-model="submitPlot"
                  justify-center
                  align="center"
                  type="submit"
                  size="large"
                  color="warning"
                  @click="submitPlot"
                >
                  submitform
                </v-btn>
                <div>
                  <br>
                </div>
                <!--   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # # -->
                <!--   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # # -->
              </v-card>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>          <!--  v-show works like v-if  -->
    <v-row
      justify="center"
      align="center"
    >
      <v-col
        cols="12"
        md="7"
      >
        <v-card
          v-if="finalshow"
          id="infocard"
          class="gradneww"
          elevation-24
          raised
          pb-5
        >
          <v-row
            justify="center"
            align="center"
          >
            <v-col
              cols="12"
              md="10"
            >
              <v-card-title
                :class="orangetxt"
              >
                Your Selections
              </v-card-title>

              <v-card-text
                :class="whitetxt"
              >
                <p>&nbsp;</p>
                <v-spacer />
                <p> Initial Tokens:  {{ vmodsel1 }} </p>
                <p> Inflation begins: {{ vmodsel2 }} </p>
                <p> Inflation tokens per 12 intervals: {{ vmodsel3 }} </p>
                <p> Inflation is turned off at: {{ vmodsel4 }} </p>
                <p> Dis-inflation ratio: {{ vmodsel5 }} </p>
              </v-card-text>
            </v-col>
          </v-row>
          <div
            justify="center"
            align="center"
            mb-5
            pb-5
          >
            <v-btn
              id="sub"
              align="center"
              size="medium"
              elevation-24
              raised
              color="cyan darken-4"
              :class="margbott"
              gtime="makeGTimestamp"
              @click="makePlot"
            >
              Make Plot
            </v-btn>
          </div>
          <div>
            <br>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <ProfileCard />

    <SecondCard />

    <PlotView />
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->

<script>
  //import pyplot from 'E:\\wsvue\\vuetify-material-dashboard-master\\src\\assets\\plots\\plot1589179263048.svg'
  import ProfileCard from '@/views/dashboard/componentsns/ProfileCardNs'
  import PlotView from '@/views/dashboard/componentsns/PlotView'
  import SecondCard from '@/views/dashboard/componentsns/SecondCard'
  import axios from 'axios'

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
  let a = '&initsup=' + initsup
  let b = '&anninf=' + anninf
  let c = '&startinf=' + startinf
  let d = '&stopinf=' + stopinf
  let e = '&disinf=' + disinf

  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT, DELETE'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    components: {
      ProfileCard,
    },
    data: () => ({
      chipprops,
      formvmodel: '',
      isHidden: false,
      finalshow: '',
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
      gdate: '',
      gtime: '',
      pname: "plot" + this.gtime + ".svg"
    }),

    methods: {
      submitform: function () {
        this.finalshow = "true"
        console.log("selection Changed submitform this.finalshow: " + this.finalshow)
        return this.finalshow
        },

      // setshowfalse: function () {
      //   this.showx = false
      //   },
      // setbtncolor: function () {
      //   console.log("just pressed chg color button")
      //   this.mycolor="purple"
      //   return this.mycolor
      //   },
      // setmyshow: function () {
      //   console.log("just pressed setmyshow button")
      //   this.myshow=false
      //   return this.myshow
      //   },
      // selectionChanged: function () {
      //   let msg = "in selectionChanged routine"
      //   this.showx = true
      //   console.log("selectionChanged: " + vmodsel1)
      //   },
      // subfiles: function () {
      //   console.log("just pressed subfiles button")
      //   this.finalshow = "true"
      //   return this.finalshow
      //   },

      makeGTimestamp: function () {
        return + new Date()
      },
      getPlotName: function (grtime) {
        return ("plot" + grtime + ".svg")
      },
      getPlotUrl: function (gggtime) {
        let tsText = '&timestp=' + gggtime
        let requestVars = a + b + c + d + e + tsText
        return 'http://localhost:5002/getpy?' + requestVars
      },
      makePlot: function  (ggtime) {
        let baseurl = getPlotUrl(ggtime)
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
