<template>
  <div>
    <!--  v-show works like v-if  -->
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
  </div>
</template>

<script>
  // import { vmodsel1, vmodsel2, vmodsel3, vmodsel4, vmodsel5 } from '@/views/dashboard/pages/UserProfile'
  export default {
    name: 'OtherCard',
    data: () => ({
      placehold: 'placeholder',
      tshowing: true,
      // vmodsel2,
      // vmodsel3,
      // vmodsel4,
      // vmodsel5,
    }),
  }
</script>
