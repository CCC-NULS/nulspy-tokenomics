<template>
  <v-container
    id="user-profile"
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
                align="center"
                pr-5
                pl-5
                elevation-15
                raised
              >
                <v-row>
                  <v-col
                    cols="12"
                    md="6"
                  >
                    <v-chip
                      id="choicechip"
                      class="margleft"
                      elevation-14
                      raised
                    >
                      Make Your Choices:&emsp;
                    </v-chip>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <!-- choice chip: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
                    <!--:items="initsupply" -->
                    <v-card 
                      id="vmd1card"
                      v-bind="gcardProps" 
                    >                        
                      Initial Token Supply
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
                    md="4"
                  >
                    <v-card 
                      id="vmd2card"
                      v-bind="gcardProps"                   
                    >
                      Annual Inflation
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
                    >
                      <span>Disinflation Starts in</span>
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
                      <span>Stop Inflation</span>
                      <vue-autonumeric
                        v-model="vmd4"
                        :placeholder="vmdHold"
                        :options="vmd4opts"
                        :style="vmdInputBox" 
                      /><br>
                      <span>Max Supply</span>
                    </v-card>                                     
                  </v-col>
                  <!-- <v-select id="end 4" # # # #  # # # ## # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="3"
                  >                  
                    <v-card 
                      id="vmd5card"
                      v-bind="gcardProps" 
                    >
                      <span>Disinflation</span>
                      <vue-autonumeric
                        v-model="vmd5"
                        :placeholder="vmdHold"
                        :options="vmd5opts"
                        :style="vmdInputBox" 
                      /><br>
                      <span>Ratio</span>
                    </v-card>                                      
                  </v-col>
                </v-row>
                <v-card
                  width="120px"
                  flat
                >
                  <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                  <v-btn
                    id="submitmain"
                    type="submit"
                    size="large"
                    color="warning"
                    @submit.prevent
                    @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                  >
                    submit form
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
          color="success"
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

import { extend, ValidationObserver, ValidationProvider, } from 'vee-validate'
import { max,  min,  numeric,   required, } from 'vee-validate/dist/rules'
// console.log("initsupply finalIPwPORT at top: " + initsupply, finalIPwPORT +  finalIMAGEp1)
extend('max', max)
extend('min', min)
extend('numeric', numeric)
extend('required', required)
Vue.component('validation-provider', ValidationProvider)
Vue.component('validation-observer', ValidationObserver)

const vmdopts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  minimumValue: '1',
  decimalPlaces: 0,
}
const vmdopts3 = {
  currencySymbol: '%',
  minimumValue: '0.01',
  decimalPlaces: 2,
}
const vmd1Val = {
  maximumValue: '10000000000000',  // 10 trillion
}
const vmd2Val = {
  maximumValue: '10000000',  // 10 billion  annual inflation
}
const vmd3Val = {
  maximumValue: '1000',  //  one thousand intervals
}
const vmd4Val = {
  maximumValue: '10000000000000',  // 10 trillion
}
const vmd5Val = {
  maximumValue: '2',  //  one thousand intervals
}


const vmd1opts = { ...vmdopts, ...vmd1Val }
const vmd2opts = { ...vmdopts, ...vmd2Val }
const vmd3opts = { ...vmdopts, ...vmd3Val }
const vmd4opts = { ...vmdopts, ...vmd4Val }
const vmd5opts = { ...vmdopts, ...vmd5Val }

const vmdInputBox = "font-size:18px; width:179px; font-weight:500; justify-center"
const placeh = 'only number allowed'
const vmdHold = 'only number allowed'
const chooseDefault = "Choose"
const gcardProps = {
  color: "teal lighten-5",
  width: "205px",
  height: "79px",
  class: "vmdCardStyle pl-5 pt-2 cyan--text text--darken-2"
  }

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
    placeh,
    gcardProps,
    vmdHold,
    chooseDefault,
    resetform: 0,
    keyShowCard: false,
    resetImage: 0,
    finalIMAGEp1,
    finalIPwPORT,
    finalIMAGE: '',
    vmd1: 1,
    vmd2: 1,
    vmd3: 1,
    vmd4: 1,
    vmd5: 0,
    }),

  mounted () {
    this.$refs.formref.reset()
    this.alertm = false;
    this.keyShowCard = false
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

.vmdCardStyle {
    font-size: 18px!important;
    line-height: 30px;
    margin-top: 0px!important;
    font-weight: 700!important;
    
    padding-bottom: 2px!important;
    justify-content: center!important;
    text-align: center!important;
}

</style>
