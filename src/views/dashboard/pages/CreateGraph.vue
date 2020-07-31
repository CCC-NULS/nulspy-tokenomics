<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="9"
      >
        <base-material-card
          color="black lighten-2"
        >
          <template v-slot:heading>
            <div
              id="firstdiv"
              shaped
              class="displaynms font-weight-light"
            >
              <TopWords />
            </div>
          </template>
          <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <!--             v-model="formvmodel"   -->
          <v-form
            id="mainform"
            ref="formref"
            :key="resetform"
            @submit.prevent
          >
            <v-container
              id="vcontain"
              class="py-3"
            >
              <v-card
                id="vcardform"
                elevation-24
                color="#4DB6AC"
                raised
                class="d-flex flex-wrap align-content-start justify-left pa-3"
                :style="`background-image: linear-gradient(306deg, #4DB6AC, #000000)`"
              >
                <span 
                  class="display-4 font-weight-bold orange--text text--lighten-5 mb-9"
                  :style="`text-shadow: 2px 2px 2px colors.grey.base;`"
                >                  
                  &nbsp;  &emsp; design your graph
                </span>
                <v-chip
                  color="transparent"
                  class="ml-3 pa-4 elevation-24 raised white--text"
                  large
                  
                  :style="`font-size: 10px!important;`"
                >
                  <span>
                    Inflation and disinflation <br>begin at the same time
                  </span>
                </v-chip>
                <!-- choice chip: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
                <!--:items="initsupply" -->
                <v-card 
                  id="vmd1card"
                  v-bind="gcardProps"
                >
                  <v-card-subtitle
                    :class="cardSubtitle" 
                  >                       
                    Initial Token Supply
                  </v-card-subtitle>

                  <vue-autonumeric
                    id="vmd1auto"
                    v-model="vmd1"
                    :options="vmd1opts"
                    :style="vmdInputBox" 
                  /><br>
                </v-card>    

                <!-- Max Supply: 2  # # # # Max Supply: 2  # # # #  # # # #  -->
                <!--  "start 2" # # # # Max Supply:  # # # ## # # #  # # # #  -->
                   
                <v-card 
                  id="vmd2card"
                  v-bind="gcardProps"
                >
                  <v-card-subtitle
                    :class="cardSubtitle" 
                  >                       
                    Max Supply
                  </v-card-subtitle>
                  <vue-autonumeric
                    v-model="vmd2"
                    :placeholder="vmdHold"
                    :options="vmd2opts"
                    :style="vmdInputBox" 
                  /><br>
                  <span style="padding-top:4px;">
                    Level when Inflation Ends 
                    <br>
                    Must be more than Initial Supply
                  </span>
                </v-card>                                     
                <!-- <v-select id="end 2" # # # #  # # # ## # # #  # # # #  -->
               
                <!--3   annual inflation:  3  # # # #  # # # #  # # # #  -->

                <v-card 
                  id="vmd3card"
                  v-bind="gcardProps"
                >
                  <v-card-subtitle
                    :class="cardSubtitle" 
                  >                       
                    Annual Inflation
                  </v-card-subtitle>

                  <vue-autonumeric
                    v-model="vmd3"
                    :placeholder="vmdHold"
                    :options="vmd3opts"
                    :style="vmdInputBox" 
                  /><br>
                </v-card>    

                <!-- 4  inflatervals Inflation Interval:  4  # # # #  # # # #  # # # #  -->
                    
                <v-card 
                  id="vmd4card"
                  v-bind="gcardProps"
                >
                  <v-card-subtitle
                    :class="cardSubtitle" 
                  >                       
                    Disinflation Starts in
                  </v-card-subtitle>
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
                  <br>
                  <span style="padding-top:6px;">How many Invervals<br>(Usually Months)</span>                    
                </v-card>                                           
                <!-- 5  5  5  # # # #  # # # #  # # # #  -->
                <!--  5  5  Disinflation ratio:   5  5  # # # #  # # # #  # # # #  -->

                <v-card 
                  id="vmd5card"
                  v-bind="gcardProps"
                >
                  <v-card-subtitle
                    :class="cardSubtitle" 
                  >
                    Disinflation
                  </v-card-subtitle>
                      
                  <vue-numeric-input
                    id="vmd5id"
                    v-model="vmd5" 
                    :value="vmd5"
                    size="30px"
                    :min="0" 
                    :max=".9" 
                    :step=".1"
                    :precision="1"
                    vmd5card
                    controls-type="updown"
                    align="center"
                    :style="arrowvuenumeric"
                  />
                  <span style="font-size:24px"> % </span>
                  <br>
                  <span>Ratio<br>Min 0, Max .9</span>
                </v-card>                                      


                <v-card
                  class="justify-center ml-10"
                  width="500px"
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
                    shaped
                    filled="true"
                    width="345px"
                    color="grey darken-1"
                    class="mb-3 justify-center rounded-tl-xl"
                    @submit.prevent
                    @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                  >
                    <h1> make my chart </h1>
                  </v-btn>
                </v-card>
              </v-card> 
            </v-container>
          </v-form>
        </base-material-card>

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
        <base-material-card
          v-if="keyShowCard"
          :key="resetImage"
          color="secondary"
          class="justify-center ml-6 mb-5 pb-5 pt-9"
        >
          <img
            :key="resetImage"
            :src="finalIMAGE"
          >
          Right click image to save
        </base-material-card>

        <v-card
          id="buttoncard"
          color="primary"
          class="padbotcard"
          elevation-24
          raised
        >
          <v-btn
            id="redobtn"
            class="display-2"
            large
            href="/"
            color="success"
          >
            Redo - Start Over
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
import Vue from 'vue'
import { acceptStr, restTypes, acctlMeths, acctlOrig, appJson, ctType, finalIPwPORT, finalIMAGEp1 } 
  from "./CreateCars.js"

// beware: arrow functions cause problems with 'this'
import axios from "axios";
import TopWords from "@/views/dashboard/components/TopWords";
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
  initialValueOnFirstKeydown: 10000,
  decimalPlaces: 0,
  maximumValue: 10000000000000,
  overrideMinMaxLimits: 'invalid',
}
const vmd2Val = {         // max supply
  minimumValue: 10000,  // 10 thousand
  maximumValue: 10000000000,  // 10 trillion
}
const vmd3Val = {
  minimumValue: 1000,  // one thousand
  maximumValue: 10000000,  // 10 million  annual inflation
}

const vmd2opts = { ...vmdopts, ...vmd2Val }   // max supply
const vmd3opts = { ...vmdopts, ...vmd3Val }   // annual inflation

const vmdInputBox = "font-size:22px; width:179px;font-weight:500; justify:center; pl-2; \
  background-color:#ffffff; line-height:42px; padding-left:5px; padding-right:4px;text-align:right;\
  margin-bottom:2px;"

// const arrowbox = "font-size:20px; background-color:#ffffff; "

const arrowvuenumeric = "font-size:22px; height:30px; width: 127px;background-color:#ffffff;"

const vmdHold = 'numbers only'
const gcardProps = {
  color: "primary lighten-5",
  width: "295px",
  height: "127px",
  "min-height": "117px",
  "min-width": "245px",
  class: "pa-1 ma-1"

  }
const gcard5Props = {
  color: "primary lighten-5",
  width: "295px",
  height: "177px",
  "min-height": "177px",
  "min-width": "295px",
  class: "pa-1 ma-3 boxshade",
  }
const cardSubtitle = "cyan--text text--darken-3 font-weight-bold font-size=15px"

export default {
  name: "CreateGraph",
  components: {
    TopWords,
    VueAutonumeric,
    VueNumericInput
  },

  data: () => ({
    vmd1opts,
    vmd2opts,
    vmd3opts,
    arrowvuenumeric,
    vmdInputBox,
    vmd1: 10000,  // start supply
    vmd2: 10000,   // max supply
    vmd3: 1000,   // annual inflation
    vmd4: 1,    // when inflation starts
    vmd5: 0,   // Disinflation
    alertm: false,
    gcardProps,
    gcard5Props,
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
    // this.keyShowCard = false
  },

  created () {
   // this.$refs.formref.reset()
    var localShowMe =  this.$store.dispatch("gShowMeAct", true)
    console.log("localshowme in createpage: " + localShowMe)
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
      // let e_inp_lg_str = e_inp_lg.toString()
      let e_inp = e_inp_lg.toString().substring(2,4)   // the percent string ie: 0.2%
      // let e_inp = e_inp_lg_str.substring(2,4)   // the percent string ie: 0.2%
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

      // let ddte = Date.now().toString();
      const gDate = Date.now().toString().substring(7,13);
//      const gDate = ddte.substring(7,13);
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


.vmdFontStyle {
    font-size: 18px!important;
    font-weight: 700!important;
    text-align: center!important;
    line-height: 30px;
}
.vmdMarginStyle {
    margin-top: 0px!important;   
    padding-bottom: 2px!important;
    justify-content: center!important;
}
.greygrady {
  background-image: linear-gradient(306deg, #3A5765 0%, #476472 100%)!important;
}
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
.boxshade {
      box-shadow: 0px 3px 5px purple !important;
}
</style>
 