<template id="profilecard">
  <v-row>
    <v-col
      cols="12"
      md="4"
    >
      <base-material-card
        id="profilecardsub"
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
              <v-btn
                @click="submitfiles"
              >
                try submit
              </v-btn>
            </v-card-text>
          </v-col>
        </v-row>
      </base-material-card>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'ProfileCard',
    data: () => ({
      dataone: 'Try different values and view a plot of how they play out over time.',
      dataoneb: 'Intervals can be thought of as months or 30/day increments.',
      datatwo: 'For this blockchain, the following values are set: ',
      datathree: 'Initial Supply:  100,000,000',
    }),
    methods: {
      submitfiles: function () {
        console.log("submitfiles called")
      },
    },
  }
</script>
