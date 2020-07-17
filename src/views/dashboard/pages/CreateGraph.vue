<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card
          color="tertiary"
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
              class="py-4"
            >
              <v-card
                id="vcardform"
                color="warning lighten-1"
                align="center"
                pr-5
                pl-5
                elevation-24
                raised
              >
                <v-row>
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <h2 
                      class="display-3 font-weight-light white--text "
                    >                  
                      Make Your Choices
                    </h2>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="12"
                    md="5"
                  >
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
                        v-model="vmd1"
                        :placeholder="vmdHold"
                        :options="vmd1opts"
                        :style="vmdInputBox" 
                      /><br>
                    </v-card>    
                  </v-col> 

                  <!--2   annual inflation:  2  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="5"
                  >
                    <v-card 
                      id="vmd2card"
                      v-bind="gcardProps"
                    >
                      <v-card-subtitle
                        :class="cardSubtitle" 
                      >                       
                        Annual Inflation
                      </v-card-subtitle>

                      <vue-autonumeric
                        v-model="vmd2"
                        :placeholder="vmdHold"
                        :options="vmd2opts"
                        :style="vmdInputBox" 
                      /><br>
                    </v-card>    
                  </v-col>
                </v-row>

                <v-row>
                  <!-- 3  inflatervals Inflation Interval:  3  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >                    
                    <v-card 
                      id="vmd3card"
                      v-bind="gcardProps"
                      class="ml-4"
                    >
                      <v-card-subtitle
                        :class="cardSubtitle" 
                      >                       
                        Disinflation Starts in
                      </v-card-subtitle>
                      <vue-autonumeric
                        v-model="vmd3"
                        :placeholder="vmdHold"
                        :options="vmd3opts"
                        :style="vmdInputBox" 
                      /><br><span>how many intervals</span>
                    </v-card>                                           
                  <!-- stop inflation: 4  # # # # stopinflation 4  # # # #  # # # #  -->
                  </v-col>

                  <v-col
                    cols="12"
                    md="4"
                  >
                    <!-- <v-select id="start 4" # # # # stop inflation  # # # ## # # #  # # # #  -->
                    
                    <v-card 
                      id="vmd4card"
                      v-bind="gcardProps"
                    >
                      <v-card-subtitle
                        :class="cardSubtitle" 
                      >                       
                        Stop Inflation
                      </v-card-subtitle>
                      <vue-autonumeric
                        v-model="vmd4"
                        :placeholder="vmdHold"
                        :options="vmd4opts"
                        :style="vmdInputBox" 
                      /><br>
                      <span style="padding-top:4px;">Max Supply</span>
                    </v-card>                                     
                  </v-col>
                  <!-- <v-select id="end 4" # # # #  # # # ## # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="3"
                  >                  
                    <v-card 
                      id="vmd5card"
                      color="teal lighten-5"
                      width="255px"
                      height="137px"
                      class="pl-3"
                    >
                      <v-card-subtitle
                        :class="cardSubtitle" 
                      >
                        Disinflation
                      </v-card-subtitle>
                      
                      <vue-autonumeric
                        v-model="vmd5"
                        :options="vmd5opts"
                        :style="vmdInputBoxSm" 
                      /><br>
                      <span>Ratio</span>
                    </v-card>                                      
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="12"
                    md="12"
                  >
                    <v-card
                      class="justify=center ml-10"
                      width="500px"
                      color="warning lighten-1"
                      flat
                    >
                      <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                      <v-btn
                        id="submitmain"
                        type="submit"
                        shaped
                        width="345px"
                        color="success"
                        class="mb-3 justify-center"
                        @submit.prevent
                        @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                      >
                        submit form
                      </v-btn>
                    </v-card>
                  </v-col>
                </v-row>
              </v-card> 
            </v-container>
          </v-form>
        </base-material-card>
        <v-alert
          v-show="false"
          id="alertm"
          v-model="alertm"
          close-text="Close Alert"
          color="orange lighten-1"
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
          :key="keyShowCard"
          color="success"
          class="justify=center ml-6 mb-5 pb-5 pt-9"
        >
          <img
            :key="resetImage"
            :src="finalIMAGE"
          >
        </base-material-card>

        <v-card
          id="buttoncard"
          color="success lighten-1"
          class="padbotcard"
          elevation-24
          raised
        >
          <v-btn
            id="redobtn"
            href="/"
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
import VueAutonumeric from '../../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';

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
  minimumValue: 1,
  decimalPlaces: 0,
  overrideMinMaxLimits: 'invalid'
}

const vmd1Val = {
  maximumValue: 10000000000000,  // 10 trillion
}
const vmd2Val = {
  maximumValue: 10000000,  // 10 billion  annual inflation
}
const vmd3Val = {
  maximumValue: 1000,  //  one thousand intervals
}
const vmd4Val = {
  maximumValue: 10000000000000,  // 10 trillion
}

const vmd1opts = { ...vmdopts, ...vmd1Val }
const vmd2opts = { ...vmdopts, ...vmd2Val }
const vmd3opts = { ...vmdopts, ...vmd3Val }
const vmd4opts = { ...vmdopts, ...vmd4Val }

const vmd5opts = {
  currencySymbol: '%',
  decimalPlacesRawValue: 2,
  minimumValue: 0,
  decimalPlaces: 2,
  maximumValue: 2,
  focus: true
}
const vmdInputBox = "font-size:16px; width:179px;font-weight: 500; justify-center; pl-2; \
  background-color:#ffffff; line-height:42px; padding-left:5px; padding-right:4px;text-align:right;margin-bottom:2px;"
const vmdInputBoxSm = 
  "font-size:16px; width:63px; font-weight:500; justify-center; pl-3; \
  ml-2; background-color:#ffffff; line-height:42px; padding-left:5px; padding-right:4px;text-align:right;"

const vmdHold = 'numbers only'
const gcardProps = {
  color: "teal lighten-5",
  width: "245px",
  height: "137px",
  class: "pa-1"
  }
const cardSubtitle = "cyan--text text--darken-2 font-weight-bold font-size=15px"

export default {
  name: "CreateGraph",
  components: {
    TopWords,
    VueAutonumeric
  },

  data: () => ({
    vmd1opts,
    vmd2opts,
    vmd3opts,
    vmd4opts,
    vmd5opts,
    vmdInputBox,
    vmdInputBoxSm,
    vmd1: 1,
    vmd2: 1,
    vmd3: 1,
    vmd4: 1,
    vmd5: null,    
    alertm: false,
    gcardProps,
    cardSubtitle,
    vmdHold,
    resetform: 0,
    keyShowCard: false,
    resetImage: 0,
    finalIMAGEp1,
    finalIPwPORT,
    finalIMAGE: '',

    }),

  mounted () {
    this.alertm = false;
    this.keyShowCard = false
  },
  created () {
    // this.$refs.formref.reset()
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
        retries: 15,
        factor: 3,
        minTimeout: 1000,
        maxTimeout: 40000,
      });

      operation.attempt(async (currentAttempt) => {
        console.log('sending request: ', currentAttempt, ' attempt');
        try {
          await axiosGet.get(finimag);
        } catch (e) {
          if (operation.retry(e)) { return; }
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
    },
    makePlot(aa, bb, cc, dd, eeee) {  
      let eee = eeee.toString()
      let ee = eee.substring(2,4)   // the percent string ie: 0.2%
      console.log("eee: " + eee)

      let a = "100,000,000"  // default
      let b = "1,000,000"  // default
      let c = "12"     // default
      let d = "110,000,000"    // default
      let e = "0.2%"     // default
      if (aa.length > 4) { a = aa; }
      if (bb.length > 4) { b = bb; }
      if (cc.length > 1) { c = cc; }
      if (dd.length > 4) { d = dd; }
      if (ee.length > 0) { e = ee; }

      console.log(`a is ${a} ${a.length} b is ${b} ${b.length} d is ${d} ${d.length}`);

      let ddte = Date.now().toString();
      const gDate = ddte.substring(7,13);
      // this.$store.dispatch('gSessionStrAct', gDate);
      console.log(`gDate makePlot: ${gDate}`);

      console.log("a: " + a + " b: " + b + " d: " + d);
      let aw = '&initsup=' + a.replace(/,/g, '');
      let bw = '&anninf=' + b.replace(/,/g, '');
      let cw = '&startinf=' + c;
      let dw = '&stopinf=' + d.replace(/,/g, '');
      let ew = "&disinf=" + e;
      // need to remove comma's twice from a, b, d
      let requestVars = aw + bw + cw + dw + ew + `&timestp=${gDate}`;

      this.finalIMAGE = `${this.finalIMAGEp1}${gDate}.svg`
      let pyReq = `${this.finalIPwPORT}/getpy?${requestVars}`;    // either

      console.log('The this.finalIPwPORT is: ' + this.finalIPwPORT);
      console.log(`The finalIMAGEp1 is: ${this.finalIMAGEp1}`);      
      console.log(`The pyReq is: ${pyReq}`);
      console.log(`The plot Url is: ${this.finalIMAGE}`);

      this.axiosPost(pyReq);  // all locations
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

.vue-numeric-input .numeric-input {
  width: 77px;
}

.numeric-input {
      background: #6fbbff!important;
    } 

.vue-numeric-input .btn-decrement .btn-icon:before {
      background-color: #6fbbff!important;
}

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
</style>
