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
                class="creategreygrad"
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
                        :max="2" 
                        :step=".01"
                        :precision="2"
                        vmd5card
                        controls-type="updown"
                        align="center"
                        :style="arrowvuenumeric"
                      />
                      <span style="font-size:24px"> % </span>
                      <br>
                      <span>Ratio<br>Min 0, Max 2</span>
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
                      color="transparent"
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
          :key="resetImage"
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
// const vmdInputBoxSm = 
//   "font-size:16px; width:63px; font-weight:500; justify-center; pl-3; \
//   ml-2; background-color:#ffffff; line-height:42px; padding-left:5px; padding-right:4px;text-align:right;"

const arrowbox = "font-size:20px; background-color:#ffffff; "

const arrowvuenumeric = "font-size:26px; height:30px; width: 127px;background-color:#ffffff;"

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
    VueAutonumeric,
    VueNumericInput
  },

  data: () => ({
    vmd1opts,
    vmd2opts,
    vmd3opts,
    vmd4opts,
    vmd5opts,
    arrowvuenumeric,
    vmdInputBox,
    vmd1: 1,
    vmd2: 1,
    vmd3: 1,
    vmd4: 1,
    vmd5: 0,    
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
    // this.keyShowCard = false
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
        retries: 19,
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
    },
    makePlot(a_inp, b_inp, c_inp, d_inp, e_inp_lg) {  
      let e_inp_lg_str = e_inp_lg.toString()
      let e_inp = e_inp_lg_str.substring(2,4)   // the percent string ie: 0.2%
      console.log("e_inp: " + e_inp)

      let final_a = "100,000,000"  // default
      let final_b = "1,000,000"  // default
      let final_c = "12"     // default
      let final_d = "110,000,000"    // default
      let final_e = "0.2%"     // default
      // if (a_inp.length > 0) { final_a = a_inp; }
      // if (b_inp.length > 0) { final_b = b_inp; }
      // if (c_inp.length > 0) { final_c = c_inp; }
      // if (d_inp.length > 0) { final_d = d_inp; }
      // if (e_inp.length > 0) { final_e = e_inp; }

      final_a = a_inp.toString(); 
      final_b = b_inp.toString(); 
      final_c = c_inp.toString(); 
      final_d = d_inp.toString(); 
      final_e = e_inp.toString(); 

      console.log(`InitSupply is ${final_a}; anninf is ${final_b}; startinf is ${final_c}; /
        StopInflation/MaxSupply is ${final_d}; Disinflation is ${final_c};`);

      let ddte = Date.now().toString();
      const gDate = ddte.substring(7,13);
      console.log(`gDate makePlot: ${gDate}`);

      let aw = '&initsup=' + final_a.replace(/,/g, '');
      let bw = '&anninf=' + final_b.replace(/,/g, '');
      let cw = '&startinf=' + final_c;
      let dw = '&stopinf=' + final_d.replace(/,/g, '');
      let ew = "&disinf=" + final_e;
      // need to remove comma's twice from final_a, final_b, final_d
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
.creategreygrad {
    background-image: linear-gradient(306deg, #3A5765 0%, #476472 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
}
.vue-numeric-input .btn-decrement .btn-icon:before .numeric-input {
      background-color: #ffffff!important;
}
.vuenumeric {
  font-size:26px; 
  height: 30px;
  width: 127px;
}
.arrowpercent {
  font-size: 30px;
}


</style>
  // padding-right: 5px !important;
  // padding-left: 5px !important;
// /* 
//   #style1.vue-numeric-input.updown {
//     padding-top: 1.5rem;
//     padding-bottom: 1.5rem;
//   }
//   #style1.vue-numeric-input.updown .numeric-input {
//     padding-right: 5px !important;
//     padding-left: 5px !important;
//   } 
//   #vmd3id.button.btn.btn-decrement {
//     background-color: #45857f !important;
//   }
//   #vmd3id.vue-numeric-input.updown .btn {
//     background: #45857f !important;
//   }
//   #style1.vue-numeric-input.updown .btn-increment {
//     height: 1.5rem;
//     width: 100%;
//     right: 0 !important;
//     left:0 !important;
//     top: 0 !important;
//     bottom: auto !important;
//   }
//   #style1.vue-numeric-input.updown .btn-decrement {
//     height: 1.5rem;
//     width: 100%;
//     left: 0 !important;
//     right: 0 !important;
//     top: auto !important;
//     bottom: 0 !important;
//    */


