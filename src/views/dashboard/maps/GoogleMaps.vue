<template>
  <v-container
    id="google-maps"
    fluid
    tag="section"
  >
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          color="success"
          title="Graph"
          class="px-5 py-3"
        >
          <v-card-text class="px-0 pb-0">
            <v-sheet>
              <iframe
                :src="secondsrc"
                width="100%"
                height="450"
                frameborder="0"
                style="border:0"
                allowfullscreen
              />
            </v-sheet>
          </v-card-text>
        </base-material-card>
      </v-col>

      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          color="success"
          title="Inflation / Deflation"
          class="px-5 py-3"
        >
          <v-card-text class="px-0 pb-0">
            <v-sheet>
              <iframe
                :src="thirdsrc"
                width="100%"
                height="450"
                frameborder="0"
                style="border:0"
                allowfullscreen
              />
            </v-sheet>
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import plotreal from '@/assets/plots/plotreal.svg'
  const plotdirr = '@/assets/plots/'

  var mymodule
  var plotkey1 = 0

export default {
  components: {
    },
  data: () => ({
    plotkey1,
  }),
  watch: {
    plotdirr:  {
      deep: true,
      immediate: true,
      handler () {
        console.log("!!! &&&&  &&&&  saw plotdirr route change!!  ---------  ")
        }         
      },
  },  
  mount () {
    ++this.plotkey1
  },
  beforeUpdate() {
    console.log() // Logs the counter value every second, before the DOM updates.
  },
  afterUpdate() {
    this.async2()
  },

  methods: {
    }
  }
</script>
<style src="@/assets/styles/mystyle.css">
</style>
