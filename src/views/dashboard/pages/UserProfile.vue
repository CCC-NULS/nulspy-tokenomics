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

    <base-material-card
      v-if="finalshow"
      id="plotmatcard"
      v-model="currentPlotPath"
    >
      <v-row>
        <v-col
          cols="12"
          md="10"
        >
          <v-card
            id="vcardone"
            color="warning lighten-2"
            class="ml-2 mr-2 mt-3 pa-2"
            elevation-24
            raised
          >
            <v-card-title
              display-3
              color="white!important"
            >
              Your Plot
            </v-card-title>
            <v-card
              id="vcardtwo"
              class="m2-3 mr-2 mt-3 pa-2 plotcenter"
              elevation-24
              raised
              color="success"
            >
              <div
                :html="currentPlotPath"
                width="90%"
                height="90%"
              >
                Plot is Here
              </div>

              <v-card-actions>
                <v-btn id="redobtn">
                  Redo
                </v-btn>
                <v-btn
                  id="savebtn"
                  color="purple"
                >
                  Save
                </v-btn>
                <v-spacer />
              </v-card-actions>
            </v-card>
          </v-card>
        </v-col>
      </v-row>
    </base-material-card>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->

<script>
  import ProfileCard from '@/views/dashboard/componentsns/ProfileCardNs'
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
  let pname = 'empty'
  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT, DELETE'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    components: {
      ProfileCard,
      SecondCard,
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
      pname,
      currentPlotPath: '@/views/dashboard/componentsns/' + pname,
    }),

    methods: {
      submitform: function () {
        this.finalshow = "true"
        console.log("selection Changed submitform this.finalshow: " + this.finalshow)
        return this.finalshow
        },

      makePlot: function  () {
        ggtime = '"+ new Date()"'
        pname = 'plot' + ggtime + '.svg'
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
