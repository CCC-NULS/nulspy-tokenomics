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
              height="700px"
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
    /* background-image: linear-gradient(306deg, #651FFF 0%, #5812F2 100%); */
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















<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
