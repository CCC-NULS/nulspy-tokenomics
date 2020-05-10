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
            id="mainform"
            ref="form"
            method="POST"
            enctype="multipart/form-data"
          >
            <v-container
              id="vcontain"
              class="py-4"
            >
              <v-card
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
                      id="smchip"
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
                    <v-select
                      id="vsel1"
                      class="margleft"
                      type="string"
                      label="Initial Token Supply"
                      :items="initsupply"
                      :rules="[v => !!v || 'Item is required']"
                      placeholder="100,000"
                    />
                  </v-col>
                  <!-- annual inflation:  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vsel2"
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
                      id="vsel3"
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
                      id="vsel4"
                      type="string"
                      label="Stop Inflation "
                      :items="stopinflation"
                    />
                  </v-col>
                  <!-- disinflation:  # # # #  # # # #  # # # #  -->

                  <v-col
                    cols="12"
                    md="3"
                  >
                    <v-select
                      id="vsel5"
                      type="string"
                      label="Disinflation Ratio %"
                      class="margright"
                      :items="disinflation"
                    />
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="12"
                    md="5"
                  />
                  <!-- submit:  # # # #  # # # #  submit: # # # # # # # # -->
                  <!--   @click="submit" # # # # # -->

                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-btn
                      align="center"
                      type="submit"
                      size="large"
                      color="warning"
                      @click="submitfiles"
                    >
                      Submit
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
      <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
          avatar="http://westteam.nulstar.com/nms/artws/Social_Telegram_G.svg"
        >
          <v-row>
            <v-col
              cols="12"
              md="12"
            >
              <v-card-text class="text-center">
                <h6 class="display-2 mb-1 grey--text">
                  Tryout Values
                </h6>

                <h4
                  class="display-2 font-weight-light mb-3 black--text"
                  :value="dataone"
                />

                <p
                  class="font-weight-light grey--text"
                  :value="dataoneb"
                />

                <p
                  class="font-weight-light grey--text"
                  :value="datatwo + datathree"
                />

                <v-btn
                  color="success"
                  rounded
                  class="mr-0"
                >
                  Continue
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  const { exec } = require('child_process')
  // const spwn = require('cross_spawn')
  const givenNumber = 100000000
  const inSupply = givenNumber.toLocaleString('en-US')
  const initsupply = ['100,000', '200,000', '500,000', '1,000,000']
  const chipprops = {
    class: 'v_chip_small',
    small: true,
    dark: false,
  }

  const a = '100000000'
  const b = '6000'
  const c = '26'
  const d = '210000000'
  const e = '.006'
  const formData = new FormData()
  formData.append('a', a)
  formData.append('b', b)
  formData.append('c', c)
  formData.append('d', d)
  formData.append('e', e)
  const optionAxios = {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Access-Control-Allow-Methods': 'POST',
      'Upgrade-Insecure-Requests': '1',
      Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    },
  }
  function newfunc () {
    alert('howdy')
    exec('ls -la')
  }
  function submitfiles () {
    console.log('submitting')
    const baseURL = 'http://127.0.0.1:5002/postdir'
    axios.post(baseURL, formData, optionAxios)
      .then(function (response) {
        console.log('hello')
        console.log(response)
      })
      .catch(function (error) {
        console.log(error)
      })
  }

  export default {
    data: () => ({
      givenNumber,
      inSupply,
      initsupply,
      chipprops,
      dataone: 'Try different values and view a plot of how they play out over time.',
      dataoneb: 'Intervals can be thought of as months or 30/day increments.',
      datatwo: 'For this blockchain, the following values are set: ',
      datathree: 'Initial Supply:  100,000,000',
      aninflation: ['500,000', '600,000'],
      inflatervals: ['12', '24', '36', '48'],
      stopinflation: ['500,000', '600,000'],
      disinflation: ['4 %', '5 %'],
    }),
    methods: {
      newfunc,
      submitfiles,
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
</style>
