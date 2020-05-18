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
              <v-chip
                medium
                dark
                color="tertiary"
              >
                DEFAULT / PRESET VALUES
              </v-chip>
              <br>
              <ul>
                <li>
                  Initial Token Supply: &nbsp; 100,000,000<br>
                </li>
                <li>
                  Inflation begins in how many intervals? &nbsp; 24 = 2 yrs
                  <br>
                </li>
                <li>
                  Inflation tokens per 12 intervals? &nbsp;5,000,000 /12 (416,666.66) <br>
                </li>
                <li>
                  Inflation is turned off at: &emsp;&emsp; 210,000,000<br>
                </li>
                <li>
                  De-inflation ratio: &emsp;&emsp; 0.004 ( 0.01 = 1% )  <br><br>
                </li>
              </ul>
              <v-chip
                color="info"
                medium
                raised
              >
                Inflation and de-inflation begin at the same time
              </v-chip>
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

                <!--
                <v-row>
                  <v-col
                    cols="12"
                    md="5"
                  />
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-btn
                      v-model="mycolor"
                      :color="mycolor"
                      @click="setbtncolor"
                    >
                      new button
                    </v-btn>
                    <v-btn
                      v-show="myshow"
                      v-model="myshow"
                      color="orange"
                      @click="setmyshow"
                    >
                      new setmyshow button
                    </v-btn>

                    <v-btn
                      id="chgbtn"
                      @click="setshowfalse"
                    >
                      Hide button
                    </v-btn>
                  -->
                <!--   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # # -->
                <!--   click=submit BUTTON  # # #BUTTON # # # BUTTON  # # # BUTTON  # # # # # -->
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
                <div> <br>
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
              @click="subfiles"
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
    <!-- profilecard  component  profilecard avatar  # # # #  # # # #  template: # # # # # # # # -->
    <v-row>
      <v-col
        cols="12"
        md="4"
      >
        <ProfileCard />
      </v-col>
    </v-row>

    <!-- card: submitted vals # # # #  # # # #  card: # # # # # # # # -->
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          id="basematcard"
          color="success"
          class="v-card-profile"
        >
          <span>
            Second Card starts here
          </span>
          <template v-show="!isHidden">
            <span> {{ vmodsel1 }} </span>
            <span> {{ vmodsel2 }} </span>
            <span> {{ vmodsel3 }} </span>
            <span> {{ vmodsel4 }} </span>
            <span> {{ vmodsel4 }} </span>
          </template>
        </base-material-card>
      </v-col>
    </v-row>


    <!-- card:  # # # #  # # # #  card: # # # # # # # # -->

  <template>
    <v-row>
      <v-col
        cols="12"
        md="10"
      >
        <v-card
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
            class="m2-3 mr-2 mt-3 pa-2 plotcenter"
            elevation-24
            raised
            color="success"
          >
            <pyplot
              width="90%"
              height="90%"
            />
          </v-card>
          <v-card-actions>
            <v-btn>
              Redo
            </v-btn>
            <v-btn
              color="purple"
            >
              Save
            </v-btn>
            <v-spacer />

            <v-btn
              icon
              @click="showx = !showx"
            >
              <v-icon>
                {{ showx ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}
              </v-icon>
            </v-btn>
          </v-card-actions>

          <v-slide-y-transition>
            <v-card-text v-show="showx">
              I'm a thing. But, like most politicians,
              he promised more than he could deliver.
            </v-card-text>
          </v-slide-y-transition>
        </v-card>
      </v-col>
    </v-row>
  </template>
  </v-container>
</template>

<script>
  //import pyplot from 'E:\\wsvue\\vuetify-material-dashboard-master\\src\\assets\\plots\\plot1589179263048.svg'
  import pyplot from '@/assets/plots/plot1589179263048.svg'
  import ProfileCard from '@/views/dashboard/componentsns/ProfileCardNs'
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
  let timestp = + new Date()
  let a = '&initsup=' + initsup
  let b = '&anninf=' + anninf
  let c = '&startinf=' + startinf
  let d = '&stopinf=' + stopinf
  let e = '&disinf=' + disinf
  let ts = '&timestp=' + timestp
  let datalist = a + b + c + d + e + ts

  let baseuri = 'http://localhost:5002/getpy?' + datalist
  const axiosi = axios.create({
    });
  axiosi.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
  axiosi.defaults.headers.post['Content-Type'] = 'application/json'
  axiosi.defaults.headers.post['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, UPDATE, PUT, DELETE'
  axiosi.defaults.headers.post['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'

  export default {
    components: {
      pyplot,
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
    }),
    methods: {
      submitform: function () {
        this.finalshow = "true"
        console.log("selection Changed submitform this.finalshow: " + this.finalshow)
        return this.finalshow
        },
      setshowfalse: function () {
        this.showx = false
        },
      setbtncolor: function () {
        console.log("just pressed chg color button")
        this.mycolor="purple"
        return this.mycolor
        },
      setmyshow: function () {
        console.log("just pressed setmyshow button")
        this.myshow=false
        return this.myshow
        },
      subfiles: function () {
        console.log("just pressed subfiles button")
        this.finalshow = "true"
        return this.finalshow
        },
      selectionChanged: function () {
        let msg = "in selectionChanged routine"
        this.showx = true
        console.log("selectionChanged: " + vmodsel1)
        },
      submitPlot: function  () {
        ;(async () => {
          console.log("inside submitPlot")
          const response = await axiosi({
            url: baseuri,
            method: 'get'
      })
      console.log(response)
    })()
  }
    },
  }
</script>

<style>
  .margleft {
    margin-left:12px!important;
  }
  .margright {
    margin-right:29px!important;
  }
  .displaynms {
    line-height: 1.7em;
    font-size: 24px!important;
    padding-left: 26px!important;
  }
  .v_chip_small {
    padding: 2px;
    margin-bottom: 10px!important;
    font-size: 16px!important;
    font-weight: 300;
    text-align: center;
  }
  .v-chip {
    padding: 19px;
    margin-bottom: 10px!important;
  }
  .v-chip__content {
    font-size: 19px;
    font-weight: 300;
    padding-left: 22px;
    padding-right: 22px;
    padding-bottom: 14px;
    padding-top: 14px;
  }
  .v-card__title {
    font-size: 22px;
    font-weight: 300;
    padding-top: 12px;
    padding-bottom: 14px;
    padding-left: 22px;
    margin-right: 22px;
    text-align: center;
  }
  .plotcenter {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
