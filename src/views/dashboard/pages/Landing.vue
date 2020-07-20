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
          width="1200px"
          color="teal lighten-2"
          :style="`background-image: linear-gradient(306deg, #fdfcfb 0%, #2d1c3 100%);`"
        >
          <v-col 
            cols="12"
            md="12"
          >
            <base-material-card
              id="land1"
              color="blue-grey"
              height="250px"
              elevation-24
              raised
              centered
              outlined
              class="background-color=cyan"
              :class="`{ justify-content: center!important;  }`"
            >
              <template v-slot:heading>
                <div class="display-3 font-weight-light">
                  <h3> Welcome to NULS Tokenomics </h3>
                </div>
              </template>             
              <v-card
                id="emptyplacer"
                color="transparent"
                flat
                land1
                class="margin-top=-25px; d-flex justify-center pl-3 mt-2"
                width="100%"
                height="100px"
              >
                <v-card
                  id="tealplacer"
                  emptyplacer
                  shaped
                  width="90%"
                  height="90%"
                  class="d-flex justify-center pa-2 cyan--text text--darken-2 creategreygrad"
                >
                  <!--  button *-* *-* *-* *-* *-* *-*  -->
                  <v-btn
                    id="gocreate"
                    tealplacer
                    width="50%"
                    height="90%"
                    dark
                    color="success"
                    class="mb-3 justify-center createbtn"
                    to="/pages/creategraph"
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

export default {
  name: 'Landing',
  data: () => ({
    centerme: "{centered: true}",
    placeh: 'only number allowed'
  }),
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

  .creategreygrad {
    background-image: linear-gradient(306deg, #607d8b 0%, #93B0BE 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}
</style>