<template>
  <v-container
    id="landing"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="12"
        md="12"
      >
        <v-card
          id="landingcard"
          width="1200px"
          color="primary lighten-2"
          :style="`background-image: linear-gradient(306deg, #fdfcfb 0%, #2d1c3 100%);`"
        >
          <v-col 
            cols="12"
            md="12"
          >
            <base-material-card
              id="land1"
              color="primary"
              height="190px"
              elevation-24
              raised
              centered
              outlined
              :class="`{ justify-content: center!important;  }`"
            >
              <template v-slot:heading>
                <div class="display-3 font-weight-light">
                  <h3 :style="`text-shadow: 2px 2px 2px #000000;`">                
                    Welcome to NULS Tokenomics
                  </h3>
                </div>
              </template>             
              <v-card
                id="emptyplacer"
                color="transparent"
                flat
                land1
                class="margin-top=-25px; margin-bottom=-25px; d-flex justify-center pl-3"
                width="100%"
                height="100px"
              >
                <v-card
                  v-if="$store.state.gShowMe"
                  id="tealplacer"
                  emptyplacer
                  shaped
                  width="30%"
                  height="70%"
                  :style="`margin-top:-12!important;`"
                  class="d-flex justify-center pa-2 creategreygrad"
                >
                  <!--  button *-* *-* *-* *-* *-* *-*  -->
                  <v-btn
                    v-if="$store.state.gShowMe"
                    id="gocreate"
                    tealplacer
                    width="90%"
                    height="90%"
                    dark
                    color="success"
                    class="mb-3 justify-center createbtn"
                    to="/pages/creategraph"
                    @onClick="onClickB"
                  >
                    <h1>Create Plot</h1>
                  </v-btn>
                </v-card>    
              </v-card>   
            </base-material-card>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Landing',
  data: () => ({
    centerme: "{centered: true}",
    placeh: 'only number allowed'
  }),
  created () {
   // this.$refs.formref.reset()
    var localShowMe =  this.$store.state.gShowMe
    console.log("localshowme in landing: " + localShowMe)
  },
  methods: {
    onClickB() {
      this.$forceUpdate();
    },
    reload() {
      this.$forceUpdate();
    }
  },
}
</script>
<style>
  .matstyle {
    justify-content: center!important;
  }
  .vmdMarginStyle {
      margin-top: 0px!important;   
      padding-bottom: 2px!important;
      justify-content: center!important;
  }
  .justifycontent {
    justify-content: center!important;
  } 

  .createbtn {
    background-image: linear-gradient(306deg, #651FFF 0%, #5812F2 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}

  .creategreygrad3 {
    background-image: linear-gradient(306deg, #607d8b 0%, #93B0BE 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}
  .creategreygrad {
    background-image: linear-gradient(306deg, #1DE9B6 0%, #93B0BE 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}


</style>