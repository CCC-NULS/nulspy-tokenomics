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
        md="7"
      >
        <base-material-card
          id="land1"
          color="blue-grey"
          height="500px"
          elevation-24
          raised
          centered
          outlined
          class="background-color=cyan"
          :class="matstyle"
        >
          <template v-slot:heading>
            <div class="display-3 font-weight-light">
              <h3> Welcome to NULS Tokenomics </h3>
            </div>
          </template>             
          <v-card
            id="emptyplacer"
            flat
            land1
            class="d-flex justify-center"
            width="99%"
            height="70%"
          >
            <v-card
              id="tealplacer"
              emptyplacer
              shaped
              color="teal lighten-4"
              width="90%"
              height="40%"
              class="d-flex justify-center pa-3 cyan--text text--darken-2"
            >
              <!--  button *-* *-* *-* *-* *-* *-*  -->
              <v-btn
                id="gocreate"
                tealplacer
                width="50%"
                height="70%"
                dark
                color="success"
                class="mb-3 justify-center"
                to="/pages/creategraph"
              >
                <h1>Create Plot</h1>
              </v-btn>
            </v-card>    
          </v-card>   
        </base-material-card>
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
<style scoped>
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
</style>