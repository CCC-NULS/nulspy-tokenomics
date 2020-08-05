<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        sm="9"
      >
        <base-material-cardn
          id="basematcard"
          width="1000px"
          min-width="400px"

          min-height="400px"
          height="700px"
          max-height="1500px"
          class="d-flex flex-column grow align-start"
        >
          <template v-slot:heading>
            <div
              id="firstdiv"              
              class="display-4 font-weight-light orange--text text--lighten-5"
              :style="`font-family:Rubik, sans-serif;text-shadow: 1px 1px 1px black;`"
            >
              design your graph
            </div>
          </template>
          <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <!--             v-model="formvmodel"   -->

          <v-card
            id="vcardform"
            height="600px"
            max-height="1900px"
            min-height="500px"
            width="90%"
            elevation-24
            raised
            shaped
            mainform
            filled="true"
            class="d-flex flex-column flex-grow grow align-start text-align-start justify-start px-4 py-5 mx-4 mb-4"
            :style="`background-image: linear-gradient(306deg, #4DB6AC, #000000)`"
          >
            <v-chip
              id="chipnote"
              color="transparent"
              class="pa-4 white--text ma-2 justify-right"
              flat
              large               
              vcardform
            >
              <span :style="`font-size:20px;font-family:'Montserrat', sans-serif;padding-top:2px;`">
                Inflation and disinflation begin at the same time
              </span>
            </v-chip>
            <!-- choice chip: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
            <!--:items="initsupply" # # # #  # # # #  # #  # # # ## #  # # # ## # #  -->
            <v-form
              id="mainform"
              ref="formref"
              :key="resetform"
              basematcard
              class="d-flex flex-grow-1 flex-shrink-1 flex-wrap my-1 ml-4 pa-2"

              @submit.prevent
            >             
              <v-card 
                id="vmd1card"
                color="teal lighten-5"
                width="450px"
                min-width="65px"               
                max-width="450px"  
                height="110px"
                max-height="360px"
                min-height="100px"
                class="d-flex flex-grow-1 flex-shrink-1 flex-wrap my-1 ml-4 pa-2"
              >
                <v-card
                  id="vmd1cardsub1"
                  width="350px"
                  max-width="450px"
                  min-width="25px"
                  height="70px"
                  max-height="360px"
                  min-height="50px"
                  color="deep-orange lighten-2"
                  flat
                  vmd1card
                  class="d-flex flex-grow-1 flex-shrink-1 my-1 ml-4 pa-2 display-1"
                  :style="`text-align:right;`"
                >
                  Initial Token Supply - Min 10,000,  Suggestion: 100,000,000: 
                </v-card>
                <v-card
                  id="vmd1cardsub2"
                  height="50px"
                  max-height="260px"
                  min-height="50px"

                  width="225px"
                  max-width="350px"
                  min-width="25px"
                  
                  color="white"
                  outlined
                  elevation-24
                  raised
                  vmd1card
                  focusable="true"
                  focus="true"
                  class="pa-1 ma-1"
                >                
                  <vue-autonumeric
                    id="vmd1auto"
                    v-model="vmd1"
                    :options="vmd1opts"
                    :style="vmdInputBox"
                  />
                </v-card>
              </v-card>    

              <!-- Max Supply: 2  # # # # Max Supply: 2  # # # #  # # # #  -->
              <!--  "start 2" # # # # Max Supply:  # # # ## # # #  # # # #  -->
                  
              <v-card 
                id="vmd2card"
                class="pa-1 ma-1 switchtext"
                color="switchpaper"
              >
                <v-row
                  :style="`text-align:left;`"
                >
                  <v-chip
                    cols="3"
                    md="3"
                    :style="`text-align:right;`"
                  >           
                    Max Supply
                  </v-chip>
                  <v-chip
                    cols="3"
                    md="3"
                  >                    
                    <vue-autonumeric
                      v-model="vmd2"
                      :placeholder="vmdHold"
                      :options="vmd2opts"
                      :style="vmdInputBox" 
                    />
                  </v-chip>
                  <v-chip cols="6">
                    Total supply when inflation ends - Min 20,000  
                    Must be more than Initial Supply. Try: 210,000,000
                  </v-chip>
                </v-row>
              </v-card>                                       
              <!-- <v-select id="end 2" # # # #  # # # ## # # #  # # # #  -->
              
              <!--3   annual inflation:  3  # # # #  # # # #  # # # #  -->

              <v-card 
                id="vmd3card"
                class="pa-1 ma-1 switchtext"
                color="switchpaper"
              >
                <v-row
                  :style="`text-align:left;`"
                >
                  <v-chip
                    cols="3"
                    md="3"
                    :style="`text-align:right;`"
                  >
                    Annual Inflation - Min 1,000
                  </v-chip>
                  <v-chip cols="3">                
                    <vue-autonumeric
                      id="vmd3auto"
                      v-model="vmd3"
                      :options="vmd3opts"
                      :style="vmdInputBox" 
                    />
                  </v-chip>
                  <v-chip 
                    cols="6"
                    md="6"
                  > 
                    Try: 5,000,000
                  </v-chip>
                </v-row>
              </v-card> 
              <!-- 4  inflatervals Inflation Interval:  4  # # # #  # # # #  # # # #  -->
                  
                
              <!-- wrapped to align cards-->
              <v-card 
                id="vmd4card"
                class="pa-1 ma-1 switchtext"
                color="switchpaper"
              >
                <v-row
                  :style="`text-align:left;`"
                >
                  <v-chip
                    cols="3"
                    md="3"
                    :style="`text-align:right;`"
                  >
                    Disinflation Starts in
                  </v-chip>
                  <v-chip 
                    cols="3"
                    md="3"
                    flex-column 
                    flex-wrap
                    direction-end
                  >                
                    <vue-numeric-input
                      id="vmd4id"
                      v-model="vmd4" 
                      :value="vmd4"
                      size="30px"
                      :min="0" 
                      :max="100" 
                      :step="1"
                      :precision="0"
                      vmd4card
                      controls-type="updown"
                      align="center"
                      :style="arrowvuenumeric"                     
                    />                
                  </v-chip>                
                  <v-chip 
                    cols="6"
                    md="6"
                    :style="`text-align:left;`"
                  >
                    How many Invervals - (Usually Months) Try: 24
                  </v-chip>                
                </v-row>
              </v-card>                                           
              <!-- 5  5  5  # # # #  # # # #  # # # #  -->
              <!--  5  5  Disinflation ratio:   5  5  # # # #  # # # #  # # # #  -->
                  
              <v-card 
                id="vmd5card"
                class="pa-1 ma-1 switchtext"
                color="switchpaper"
              >
                <v-row
                  :style="`text-align:left;`"
                >
                  <v-chip 
                    cols="3"
                    md="3"
                    :style="`text-align:right;`"
                  >
                    Disinflation
                  </v-chip>
                  <v-chip cols="3">
                    <vue-numeric-input
                      id="vmd5id"
                      v-model="vmd5" 
                      :value="vmd5"
                      :min=".1" 
                      :max=".9" 
                      :step=".1"
                      :precision="1"
                      size="30px"
                      vmd5card
                      controls-type="updown"
                      align="center"
                      :style="arrowvuenumeric"
                    />
                    <span style="font-size:14px"> % </span>
                  </v-chip>
                  <v-chip cols="6">
                    Ratio:  Min 0, Max .9  Try: 0.4
                  </v-chip>
                </v-row>
              </v-card>                                                                          

              <v-card
                class="justify-center ml-10 mb-1"
                width="500px"
                min-width="300px"

                color="transparent"
                flat
              >
                <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                <v-btn
                  id="submitmain"
                  type="submit"
                  elevation-24
                  raised
                  dark
                  hover
                  shaped
                  filled="true"
                  width="345px"
                  color="deep-orange lighten-1"
                  class="mb-3 justify-center rounded-tl-xl"
                  :style="`text-transform:lowercase;`"
                  @submit.prevent
                  @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                >
                  <h1> make graph </h1>
                </v-btn>
              </v-card>
            </v-form>
          </v-card>                                      
        </base-material-cardn>

        <v-alert
          v-show="false"
          id="alertm"
          v-model="alertm"
          close-text="Close Alert"
          color="warning lighten-1"
          dark
          dismissible
          width="200px"
        >
          Inputs not valid.
        </v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <base-material-cardn
          v-if="keyShowCard"
          :key="resetImage"
          color="teal lighten-3"
          class="justify-center ml-6 mb-5 pb-5 pt-7 mt-1"
        >
          <img
            :key="resetImage"
            :src="finalIMAGE"
          >
          To save - right click
        </base-material-cardn>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
import Vue from 'vue'
import {  mapState  } from 'vuex'

import { acceptStr, restTypes, acctlMeths, acctlOrig, appJson, ctType, finalIPwPORT, finalIMAGEp1 } 
  from "./CreateVars.js"
import {	initsup } from "./TopWords.js"
// beware: arrow functions cause problems with 'this'
import axios from "axios";
import AutoNumeric from 'autonumeric'
import VueAutonumeric from '../../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';
import VueNumericInput from 'vue-numeric-input'

// import { extend, ValidationObserver, ValidationProvider, } from 'vee-validate'
// import { max,  min,  numeric,   required, } from 'vee-validate/dist/rules'
// console.log("initsupply finalIPwPORT at top: " + initsupply, finalIPwPORT +  finalIMAGEp1)
// extend('max', max)
// extend('min', min)
// extend('numeric', numeric)
// extend('required', required)
// Vue.component('validation-provider', ValidationProvider)
// Vue.component('validation-observer', ValidationObserver)

const vmdopts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  decimalPlaces: 0,
  overrideMinMaxLimits: 'invalid'
}
const vmd1opts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  minimumValue: 10000,
  rawValue: 10000,
  initialValueOnFirstKeydown: 100000000,
  decimalPlaces: 0,
  maximumValue: 10000000000000,
  overrideMinMaxLimits: 'invalid',
}
const vmd2Val = {         // max supply
  minimumValue: 20000,  // 10 thousand
  maximumValue: 10000000000,  // 10 trillion
  initialValueOnFirstKeydown: 210000000,

}
const vmd3Val = {
  minimumValue: 1000,  // one thousand
  maximumValue: 10000000,  // 10 million  annual inflation
  initialValueOnFirstKeydown: 5000000,
}

const vmd2opts = { ...vmdopts, ...vmd2Val }   // max supply
const vmd3opts = { ...vmdopts, ...vmd3Val }   // annual inflation

const vmdInputBox = "font-size:16px; width:122px; font-weight:500; justify:right; \
  line-height:30px; padding-left:2px; margin-left:2px;\
  padding-right:3px;text-align:right; margin-bottom:2px;"

// const arrowbox = "font-size:20px; background-color:#ffffff; "

const arrowvuenumeric = "font-size:20px; height:30px; width: 127px;background-color:#ffffff;"

const vmdHold = 'numbers only'
// const gcardProps = {
//   color: "dark-orange lighten-5",
//   width: "500px",
//   height: "70px",
//   "max-height": "1000px",
//   "min-height": "50px",
//   "min-width": "155px",

//   }
// const gcard5Props = {
//   color: "dark-orange lighten-5",
//   width: "400px",
//   height: "100px",
//   "max-height": "900px",
//   "min-height": "100px",
//   "min-width": "195px",
//   class: "pa-1 ma-1 boxshade d-flex flex-wrap",
//   }          

const cardSubtitle = "deep-purple--text text--darken-4 font-size=11px justify-left"

export default {
  name: "CreateGraph",
  components: {
    VueAutonumeric,
    VueNumericInput
  },

  data: () => ({
    initsup,
    vmd1opts,
    vmd2opts,
    vmd3opts,
    arrowvuenumeric,
    vmdInputBox,
    vmd1: 100000000,  // start supply
    vmd2: 210000000,   // max supply
    vmd3: 5000000,   // annual inflation
    vmd4: 1,    // when inflation starts
    vmd5: .1,   // Disinflation
    alertm: false,
    cardSubtitle,
    vmdHold,
    resetform: 0,
    keyShowCard: false,
    resetImage: 0,
    finalIMAGEp1,
    finalIPwPORT,
    finalIMAGE: '',
    }),
  computed: {
    aShowMe () {
      return this.$store.state.gShowMe;
    }  
  },  
  mounted () {
    this.alertm = false;
    this.$store.dispatch("gShowMeAct", false)
    // this.keyShowCard = false
  },

  created () {
   // this.$refs.formref.reset()
    // console.log("localshowme in createpage: " + localShowMe)
  },

  methods: {   
    checkPic (finimag) {
      this.keyShowCard += 1;
      const axiosGet = axios.create({
        defaults: {
          headers: {
            get: { Accept: acceptStr, acctlMeths: restTypes, ctType: appJson },
            common: { acctlOrig: "*" }
          },
        },
      });
      const retry = require('retry');
      const operation = retry.operation({
        retries: 10,
        factor: 3,
        minTimeout: 500,
        maxTimeout: 40000,
      });

      operation.attempt(async (currentAttempt) => {
        console.log('sending request: ', currentAttempt, ' attempt');
        try {
          await axiosGet.get(finimag);
        } catch (err) {
          if (operation.retry(err)) { return; }
        }
        let opAttempts = operation.attempts()
        console.log("retries: " + opAttempts)
        this.resetImage += 1;
        // if (opAttempts < 15) {
        //   this.showme = true
        // }
      }) 
    }, 
    axiosPost(baseurl) {
      const axiosi = axios.create({
        defaults: {
          headers: {
            post: { Accept: acceptStr, acctlMeths: restTypes, ctType: appJson },
            common: { acctlOrig: "*" }
          },
        },
      });
      try {
        console.log("inside axiosPost: " + baseurl);
        (async () => {
          let response = await axiosi({
            url: baseurl,
            method: "post"
          });
        })();
      } catch (e) {
        console.log(e);
      }
      this.$refs.formref.reset()
      console.log(`The plot Url is: ${this.finalIMAGE}`);

    },
    makePlot(a_inp, d_inp, b_inp, c_inp, e_inp_lg) {  // order changed moved d to b
      let e_inp = e_inp_lg.toString().substring(2,4)   // the percent string ie: 0.2%
      console.log("e_inp: " + e_inp)

      let fin_a_init_supply = "100,000,000"  // default start supply
      let fin_d_max_supply = "110,000,000"    // default max supply
      let fin_b_ann_infl = "1,000,000"  // default annual inflation
      let fin_c_start_time = "12"     // default start interval
      let fin_e_dis_rat = "0.2%"     // default

      fin_a_init_supply = a_inp.toString(); 
      fin_d_max_supply = d_inp.toString(); 
      fin_b_ann_infl = b_inp.toString(); 
      fin_c_start_time = c_inp.toString(); 
      fin_e_dis_rat = e_inp.toString(); 

      let safeTenPercent = fin_a_init_supply.toNumber / 10
      if (fin_d_max_supply < fin_a_init_supply)
        fin_d_init_supply = fin_a_init_supply.toNumber + safeTenPercent
      
      if (fin_b_ann_infl > fin_a_init_supply.toNumber /3)
        fin_b_ann_infl = safeTenPercent
      console.log(`InitSupply is ${fin_a_init_supply}; anninf is ${fin_b_ann_infl}; startinf is ${fin_c_start_time}; /
        StopInflation/MaxSupply is ${fin_d_max_supply}; Disinflation is ${fin_c_start_time};`);

      const gDate = Date.now().toString().substring(7,13);
      console.log(`gDate makePlot: ${gDate}`);

      let aw = '&initsup=' + fin_a_init_supply.replace(/,/g, '');
      let dw = '&stopinf=' + fin_d_max_supply.replace(/,/g, '');  // still send in old order
      let bw = '&anninf=' + fin_b_ann_infl.replace(/,/g, '');
      let cw = '&startinf=' + fin_c_start_time;
      let ew = "&disinf=" + fin_e_dis_rat;
      // need to remove comma's twice from fin_a_init_supply, fin_b_ann_infl, fin_d_max_supply
      let requestVars = aw + bw + cw + dw + ew + `&timestp=${gDate}`;

      this.finalIMAGE = `${this.finalIMAGEp1}${gDate}.svg`
      let pyReq = `${this.finalIPwPORT}/getpy?${requestVars}`;    // either

      console.log('The this.finalIPwPORT is: ' + this.finalIPwPORT);
      console.log(`The finalIMAGEp1 is: ${this.finalIMAGEp1}`);      
      console.log(`The pyReq is: ${pyReq}`);
      console.log(`The plot Url is: ${this.finalIMAGE}`);

      this.axiosPost(pyReq);  // all locations
      this.keyShowCard = true
      this.checkPic(this.finalIMAGE)
    },
    resetc() {
      console.log("resetting form");
      this.$refs.formref.reset() 
      // alert("You have reset the form")
    },
    keepplot() {
      console.log("in keepplot");
      // this.alert=true
    },
  }
}
 // let aw = "&initsup=100000000"; // let bw = "&anninf=5000000" // let cw = "&startinf=24" // let dw = "&stopinf=210000000" // let ew = "&disinf=4" // let dw = "&stopinf=210000000";
</script>
<style src="@/assets/styles/mystyle.css">
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital@1&display=swap');

.creategreygrad {
    background-image: linear-gradient(306deg, #3A5765 0%, #476472 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}
.vue-numeric-input .btn-decrement .btn-icon:before .numeric-input {
      background-color: #ffffff!important;
}

.boxshadeorig {
      box-shadow: 0px 3px 5px -1px rgba(147, 90, 201, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}

</style>
 