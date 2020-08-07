<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="3"
        md="8"
        class="justify-center"
      >
        <material-cardn
          id="basematcard"
          v-bind="basecardprops"
          class="justify-center"
        >
          <template v-slot:heading>
            <div
              id="firstdiv"
              height="100px"              
              :class="headingclss"
              :style="headstyle"
            > 
              design your graph
            </div>
          </template>
          <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <!--        # # #   -->
          <!-- FORMcard ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <v-card
            id="vcard-for-form"
            ref="formrefc"
            flat
            class="px-2 py-1 ma-1" 
            :class="flexlist"
            :style="backgrad"
          >
            <!--    # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
            <!-- form  # # # #  # # # #  # #  # # # ## #  # # # ## # #  -->
            <v-form
              id="mainform"
              ref="formref"
              :key="resetform"
              vcard-for-form
              style="flat=true"
              @submit.prevent
            >     
              <!-- card group: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->

              <v-card
                id="surroundcards"
                width="96%"
                flat="true"
                color="transparent"
                :class="flexlist"               
                class="px-3 py-1 ma-2"
              >
                <!-- chipnote card under sentence -->
                <v-card
                  id="chipnote"
                  height="62px"
                  v-bind="chipnoteprops"
                  elevated-6
                  class="py-2 pl-4 pr-7 ma-3"
                >
                  <span 
                    style="font-size:14px;font-family:'Roboto',sans-serif;color:black;" 
                  >
                    Disinflation begins <br>one interval after Inflation starts
                  </span>
                </v-card>
            
                <!-- choice card: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->

                <v-card 
                  id="vmd1card"
                  v-bind="gcprops"
                  :width="cardwidth"
                  :class="cardclass"
                >
                  <v-card-subtitle
                    id="vmd1cardsubt"
                    vmd1card
                    class="pb-1 mb-1"
                    :style="longstyle"
                  >
                    Initial Token Supply - Min 10,000,  <br>Suggestion: 100,000,000
                  </v-card-subtitle>
       
                  <v-chip 
                    id="vchip1"
                    :style="chipstyle"
                    :class="chipclass"
                  >        
                    <vue-autonumeric
                      id="vmd1auto"
                      v-model="vmd1"
                      :options="vmd1opts"
                      :style="vmdInputBox"
                      vchip1
                    />
                  </v-chip>
                </v-card>    

                <!-- Max Supply: 2  # # # # Max Supply: 2  # # # #  # # # #  -->
                <!--  "start 2" # # # # Max Supply:  # # # ## # # #  # # # #  -->
                      
                <v-card 
                  id="vmd2card"
                  v-bind="gcprops"
                  :width="cardwidth"
                  :class="cardclass"
                >
                  <v-card-subtitle
                    id="vmd2cardsubt"
                    vmd2card
                    class="pb-1 mb-1 xyz"
                    :style="longstyle"
                  >
                    Max/Total supply when inflation ends - min: 20,000<br> 
                    Must be > than Initial Supply. Try: 210,000,000
                  </v-card-subtitle>       
                  <v-chip 
                    id="vchip2"
                    :style="chipstyle"
                    :class="chipclass"
                  >                                  
                    <vue-autonumeric
                      id="vmd2auto"
                      v-model="vmd2"
                      :placeholder="vmdHold"
                      :options="vmd2opts"
                      :style="vmdInputBox" 
                    />
                  </v-chip>
                </v-card>    
                                
                <!-- <v-select id="end 2" # # # #  # # # ## # # #  # # # #  -->              
                <!--3   annual inflation:  3  # # # #  # # # #  # # # #  -->
                      
                <v-card 
                  id="vmd3card"
                  v-bind="gcprops"
                  :width="cardwidth"
                  :class="cardclass"
                >
                  <v-card-subtitle
                    id="vmd3cardsubt"
                    vmd3card
                    class="pb-1 mb-1"
                    :style="longstyle"
                  >
                    Annual Inflation - Min 1,000 <br>  Try: 5,000,000
                  </v-card-subtitle>
                  <v-chip 
                    id="vchip3"
                    :style="chipstyle"
                    :class="chipclass"
                  >
                    <vue-autonumeric
                      id="vmd3auto"
                      v-model="vmd3"
                      :options="vmd3opts"
                      :style="vmdInputBox" 
                    />
                  </v-chip>
                </v-card>    

                <!-- 4  inflatervals Inflation Interval:  4  # # # #  # # # #  # # # #  -->
                                
                <!-- wrapped to align cards-->
                <v-card 
                  id="vmd4card"
                  v-bind="gcprops"
                  :width="cardwidth"
                  :class="cardclass"
                >
                  <v-card-subtitle
                    id="vmd4cardsubt"
                    vmd4card                  
                    class="pb-1 mb-1"
                    :style="longstyle"
                  >                  
                    Inflation starts in how many intervals <br>
                    (usually months) Try: 24
                  </v-card-subtitle>
                  <v-chip 
                    id="vchip4"
                    :style="chipstyle"
                    :class="chipclass"
                  >            
                    <vue-numeric-input
                      id="vmd4id"
                      v-model="vmd4" 
                      :value="vmd4"
                      size="20px"
                      :min="0" 
                      :max="100" 
                      :step="1"
                      :precision="0"
                      vchip4
                      controls-type="updown"
                      align="center"
                      :style="arrowvuenumeric"                     
                    />                
                  </v-chip>                
                </v-card>                
                <!-- 5  5  5  # # # #  # # # #  # # # #  -->
                <!--  5  5  Disinflation ratio: font-family: Avenir, Helvetica, Arial, sans-serif;  5  5  # # # #  # # # #  # # # #  -->
                
                <v-card 
                  id="vmd5card"
                  v-bind="gcprops"
                  :width="cardwidth"
                  :class="cardclass"
                >
                  <v-card-subtitle
                    id="vmd5cardsubt"
                    vmd5card
                    class="pa-1 mb-1"
                    :style="longstyle"
                  >                  
                    Disinflation Ratio:  Min 0, Max 2.0  Try: 0.4
                  </v-card-subtitle>

                  <v-chip 
                    id="vchip5"
                    :style="chipstyle"
                    :class="chipclass"
                  >
                    <vue-numeric-input
                      id="vmd5id"
                      v-model="vmd5" 
                      v-bind="numericinp"
                      :value="vmd5"
                      :style="arrowvuenumeric"
                      vmd5card
                    />
                    <span style="font-size:14px"> % </span>
                  </v-chip>
                </v-card>   
                <!-- # # # # # # #  *-* *-* *-* *-* *-* *-*  -->

                <v-card
                  id="submit-btn-card"
                  :width="cardwidth"
                  min-width="300px"
                  color="transparent"
                  class="justify-center align-center mx-1 mb-1"
                  flat
                >
                  <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                  <v-btn
                    id="submitmain"
                    v-bind="subbtn"
                    class="justify-center rounded-tl-xl mb-3"
                    :style="`text-transform:lowercase;`"
                    @submit.prevent
                    @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                  >
                    <h1> make graph </h1>
                  </v-btn>
                </v-card>                                                        
              </v-card>
            </v-form>                
          </v-card>
        </material-cardn>
        <!-- plot shows up here # # # # # # # -->
        <v-row>
          <v-col
            cols="12"
            md="12"
          >
            <material-cardn
              v-if="keyShowCard"
              :key="resetImage"
              width="100%"
              color="teal lighten-3"
              class="justify-center mx-0 px-0 mt-1 mb-2 pb-5 pt-7"
            >
              <img
                :key="resetImage"
                :src="finalIMAGE"
              >
              <span style="align:left"> To save - right click on plot</span>
            </material-cardn>
          </v-col>
        </v-row>
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
// beware: arrow functions cause problems with 'this'
import axios from "axios";
import AutoNumeric from 'autonumeric'
import VueAutonumeric from '../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';
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

const subbtn = {
  type: "submit",
  elevation: 24,
  dark: true,
  hover: true,
  shaped: true,
  filled: true,
  width: "345px",
  color: "deep-orange lighten-1",
}
const vmdopts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  decimalPlaces: 0,
  overrideMinMaxLimits: 'invalid'
}
const numericinp = {
  min: 0.0 ,
  max: 2.0 ,
  step: .1,
  precision: 1,
  size: '30px',
  'controls-type': 'updown',
  align: 'center',
}


const vmd1opts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  minimumValue: 10000,
  rawValue: 10000,
  placeholder: 100000000,
  label: 100000000,
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

const vmdInputBox = "width:120px; font-size:16px; font-weight:500; \
  line-height:23px; text-align:right; \
  padding-left:2px;\
  padding-right:2px; \
  padding-bottom:2px;padding-top:2px;  \
  margin-bottom:2px; margin-left:2px;margin-right:2px; margin-top:5px; color:purple; background-color:white; "

const basecardprops = {
  width: "95%",
  "min-width": "400px",
  "min-height": "500px",
  "height": "1000px",
  "max-height": "1900px",
}
const chipnoteprops = {
  color: "rgba(251,233,231,1)",
  shaped: true,
  dark: true,
  raised: true,
  }





const arrowvuenumeric = "font-size:20px; height:23px; width: 110px; color:#ffffff;"

const vmdHold = 'numbers only'

var formcp = 'height="800px" max-height="2900px" min-height="700px" width="95%" flat color="transparent"'
var flexlist = "d-flex flex-column flex-shrink-1 justify-center align-center justify-around"


export default {
  name: "CreateGraph",
  components: {
    VueAutonumeric,
    VueNumericInput
  },

  data: () => ({
    longstyle: "color:#BF360C;font-family:Roboto,sans-serif;font-size:15px!important;font-weight:400",
    flexlist,
    subbtn,
    numericinp,
    basecardprops,
    chipnoteprops,
    cardclass: `${flexlist}` +  "px-2 py-1 ma-2",
    chipstyle: "border-top-right-radius:1px;border-bottom-left-radius:1px;",
    chipclass: "justify-center align-center white medium flat",
    headingclss: "display-4 font-weight-light orange--text text--lighten-5",
    headstyle: "font-family:Rubik, sans-serif;text-shadow: 1px 1px 1px black;",
    arrowvuenumeric,
    vmdInputBox,   
    vmd1opts,
    vmd2opts,
    vmd3opts,
    vmd1: 100000000,  // start supply
    vmd2: 210000000,   // max supply
    vmd3: 5000000,   // annual inflation
    vmd4: 1,    // when inflation starts
    vmd5: 0,   // Disinflation
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
    },
    backgrad () {
      var stte = ' '
      if (window.outerWidth >= 960) {
        stte = "background-image: linear-gradient(306deg, #4DB6AC, #000000)" 
      }
      return stte
    },
    backgrad2 () {
      var stte = ' '
      if (window.outerWidth >= 960) {
        stte = "background-image: linear-gradient(306deg, #E0F2F1, #D1C4E9)" 
      }
      return stte
    },
    gcprops () {
      var sp
      if (window.outerWidth < 960) {
        sp = {
          flat: true,
          shaped: false,
          raised: false,
          "elevation": 0,
          color: "#E0F2F1"
        }
      }
      else {
          sp = {
            flat: false,
            shaped: true,
            raised: true,
            "elevation": 12,
            color: "#E0F2F1",
            "min-width": "445px",              
          }
      }
      return sp
    },

    gcardWid () {
      var aaabb = this.$refs.formrefc.attributes.width
      return (.9 * aaabb)
    },

    windsmall () {
      if (window.outerWidth < 960) 
         return true
      else return false
    },
    cardwidth () {
      var finsize
      var owid = window.outerWidth
      console.log("found win size: " + owid)
      var sms
      var bigs

      if (owid < 960) {
        sms = (owid * .84);
        console.log("found small win * .84: " + sms)
        finsize = sms;
        }
      else  {
        sms = (owid * .33 );
        console.log("found big win * .33: " + sms)
        finsize = sms 
        }
      console.log("finsize: " + finsize)
      return finsize
    },

    gcardcolor () {
        if (window.outerWidth < 960) {
          console.log("window is small")
          return "transparent"; 
        }
      else return "E0F2F1";  // #E0F2F1 = teal lighten-5
    },
    
    tcolor () {
      var colr = false
      if (window.outerWidth < 960)
        colr = "transparent" 
      return colr  // #E0F2F1 = teal lighten-5
    },
    bkgstyle1 () {
      var gstyle = "transparent"
      if (window.outerWidth > 959)
        gstyle =  "`background-image: linear-gradient(306deg, #4DB6AC, #000000)`" 
      return gstyle  // #E0F2F1 = teal lighten-5
    },   
  },  
  mounted () {
    this.$store.dispatch("gShowMeAct", false)
    // this.keyShowCard = false
    console.log("---window.outerWidth " + window.outerWidth)
    console.log("---window.innerWidth " + window.innerWidth)
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
      let fin_d_max_supply = "210,000,000"    // default max supply
      let fin_b_ann_infl = "5,000,000"  // default annual inflation
      let fin_c_start_time = "24"     // default start interval
      let fin_e_dis_rat = "0.4%"     // default

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
.chipstyle {
  font-size:16px;
  font-family:'Roboto',sans-serif;
  color:black;
}
.subtstyle {
    color: #3A5765;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    margin-bottom: 4px; 
    padding-bottom: 4px;
  }
.v-card__subtitle {
    font-size: 15px!important;
}
.substyle3 {
  color:purple;
  font-family:Roboto,sans-serif;
  font-size:15px!important;
  font-weight:600;
}
.xyz {
  color:#BF360C;
  font-family:Roboto,sans-serif;
  font-size:15px!important;
  font-weight:400;
}
</style>
