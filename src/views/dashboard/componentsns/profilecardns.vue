<template id="profilecard">
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
</template>
