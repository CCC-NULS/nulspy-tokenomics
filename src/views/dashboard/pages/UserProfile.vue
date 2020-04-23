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
        <base-material-card>
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              Edit Values
            </div>

            <div class="subtitle-1 font-weight-light">
              Complete your choices
            </div>
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Company (disabled)"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Tokens"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Tokens"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Initial Supply"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    label="Inflation begins in intervals"
                    class="purple-input"
                  />
                </v-col>

                <v-col cols="12">
                  <v-text-field
                    label="Inflation tokens per 12 intervals"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Inflation is turned off when inflation reaches:"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Disinflation ratio is:"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    class="purple-input"
                    label="Inflation and disinflation begin at the same time."
                    type="number"
                  />
                </v-col>

                <v-col cols="12">
                  <v-textarea
                    class="purple-input"
                    label="Intervals"
                    :value="dataoneb"
                  />
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
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
          avatar="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg"
        >
          <v-card-text class="text-center">
            <h6 class="display-1 mb-1 grey--text">
              Tryout Values
            </h6>

            <h4 class="display-2 font-weight-light mb-3 black--text">
              Test Inflation
            </h4>

            <p
              class="font-weight-light grey--text"
              :value="dataone"
            />

            <v-btn
              color="success"
              rounded
              class="mr-0"
            >
              Follow
            </v-btn>
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        // mypg: "new ptitle in CART source7777",
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
