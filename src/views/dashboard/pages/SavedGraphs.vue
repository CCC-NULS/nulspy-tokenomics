<template>
  <v-container
    id="google-maps"
    fluid
    tag="section"
  >
    <v-row>
      <v-col cols="12">
        <base-material-card
          color="success"
          title="Graph"
          class="px-5 py-3"
        >
          <v-card
            v-show="$store.state.sCounter > -1"
            id="splotcard"
            class="padplot"
            elevation-24
            raised
            margin-left="4px!important"
            padding-left="2px!important"
            margin-top="4px!important"
            margin-bottom="4px!important"
          >
            <plotone_comp 
              v-show="$store.state.sCounter > -1"
              :pkey="splotkey"
              splotcard
              margin-left="12px!important"
            />
          </v-card>
        </base-material-card>
      </v-col>

      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          color="success"
          title="Graph"
          class="px-5 py-3"
        >
          <v-card
            margin-left="9px"
            max-width="95%"
          >
            <v-btn
              @click="loadnow"
            >
              Load Now
            </v-btn>

            <savone_comp 
              v-if="showcomp" 
              max-width="95%"
            />
          </v-card>
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
  import { mapState, mapMutations, mapActions } from 'vuex'  
  import plotone_comp from '@/assets/plots/plotone.svg'
  import savone_comp from '@/assets/plots/plotempty.svg'
  var savonecompname = '@/assets/plots/' + 'plot86007891.svg'
  var showcomp = false

  var splotkey = 0

export default {
  name: "SavedGraphs",
  components: {
    savone_comp,
    plotone_comp,
    savone_comp: () => import(savonecompname)  // async dynamic load works
  },
  data: () => ({
    isActive: false,
    showcomp,
    splotkey,
    secondsrc: "http://localhost:5002/static/plots/plot00910117.svg",
    thirdsrc: "http://localhost:5002/static/plots/plot00910117.svg",
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
  methods: {
      loadnow: function () {
        showcomp: true
      },
    },  
  mount () {
    ++this.splotkey
    console.log(this.splotkey)
  },
}
</script>
<style src="@/assets/styles/mystyle.css">
</style>
