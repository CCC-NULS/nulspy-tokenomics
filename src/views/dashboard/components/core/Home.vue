<template>
  <div class="home">
    <v-container
      id="Home"
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
          <v-col 
            cols="12"
            md="12"
          >
            <base-material-cardn
              v-if="$store.state.gShowMe"
              id="land1"
              color="teal lighten-4"
              height="300px"
              elevation-24
              raised
              centered
              outlined
              :class="`{ justify-content: center!important;  }`"
            >
              <template v-slot:heading>
                <div class="display-3 font-weight-light">
                  <h3 :style="`text-shadow: 1px 2px 2px #000000;font-family:Montserrat,sans-serif;`">                
                    NULS Tokenomics
                  </h3>
                </div>
              </template>              
            </base-material-cardn>
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'Home',
  data: () => ({
    centerme: "{centered: true}",
    placeh: 'only number allowed'
  }),
  created () {
   // this.$refs.formref.reset()
    var localShowMe =  this.$store.state.gShowMe
    console.log("localshowme in home: " + localShowMe)
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
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital@1&display=swap');

</style>















<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
