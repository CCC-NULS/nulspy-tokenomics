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
        <base-material-card primary>
          <template v-slot:heading>
            <div class="display-2 font-weight-medium" />

            <div class="display-2 font-weight-medium">
              The following values are already set:<br><br>
              <ul>
                <li>
                  Initial Supply:  &emsp;&emsp; 100,000,000 NULS<br>
                </li>
                <li>
                  Inflation begins in intervals: &emsp;&emsp; 24 (2 years)<br>
                </li>
                <li>
                  Inflation tokens per 12 intervals: &emsp;&emsp; 5,000,000 / 12 (416,666.66) NULS<br>
                </li>
                <li>
                  Inflation is turned off at: &emsp;&emsp; 210,000,000  NULS<br>
                </li>
                <li>
                  Disinflation ratio is: &emsp;&emsp; 0.004     ( 0.01 = 1% )  <br><br>
                  Inflation and disinflation begin at the same time.<br><br>
                </li>
              </ul>
            </div>

            <div class="subtitle-1b display-2 font-weight-bold">
              &emsp;&emsp;&emsp;&emsp; <br>
            </div>
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <!-- class="inputc"  -->
                  <v-text-field
                    class="purple-input display-2"
                    label="Initial Supply:"
                    :value="inSupply"
                    type="string"
                    name="initial_supply_y"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <!-- class="inputc"  -->
                  <v-text-field
                    label="Inflation tokens per 12 intervals:"
                    class="purple-input display-2"
                    value="5000000"
                    type="number"
                    name="annual_inflation"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <!-- class="inputc"  -->
                  <v-text-field
                    label="Inflation begins in how many intervals:"
                    class="purple-input display-2"
                    value="24"
                    type="number"
                    name="start_inflation"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Inflation stops at:"
                    class="purple-input display-2"
                    value="210000000"
                    type="number"
                    name="stop_inflation_y"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Disinflation ratio ( .01 = 1% ):"
                    class="purple-input display-2"
                    value="0.004"
                    type="number"
                    name="disinflation_ratio"
                  />
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
                  >
                    Plot Graph
                  </v-btn>
                </v-col>
              </v-row>
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
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  const givenNumber = 100000000
  const inSupply = givenNumber.toLocaleString('en-US')

  export default {
    data () {
      return {
        inSupply: inSupply,
        dataone: 'Try different values and view a plot of how they play out over time.',
        dataoneb: 'Intervals can be thought of as months or 30/day increments.',
        datatwo: 'For this blockchain, the following values are set: ',
        datathree: 'Initial Supply:  100,000,000 VKG/NULS',
        datafour: 'Inflation begins in intervals: &emsp;&emsp; 24 (2 years)',
        datafive: 'Inflation tokens per 12 intervals: &emsp;&emsp; 5,000,000 / 12 (416,666.66) VKG/NULS',
        datasix: 'Inflation is turned off when inflation reaches:   210,000,000  VKG/NULS',
        dataseven: 'Disinflation ratio is:   0.004       ( 0.01 = 1% ) ',
        dataeight: 'Inflation and disinflation begin at the same time.',
      }
    },
  }
</script>
