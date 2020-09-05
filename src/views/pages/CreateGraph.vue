<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row
      class="d-flex flex-align-start"
    >    
      <v-col
        cols="12"
        xs="12"
        md="12"
      >
        <!-- <div 
          v-for="(item, i) in toplines"
          :key="i"
          :style="item.sty"
        /> -->
        <template name="MHeadComp2">
          <slot 
            name="MHeadComp2" 
            :toplines="toplines"
          > 
            {{ toplines.nme }}
          </slot>
        </template>
        <v-row> 
          <v-col cols="9">
            <v-card
              color="red lighten-2"
              height="220"
              :style="`${cardtopmarg}`"
            >
              <template>
                inside template

                <slot name="MHeadComp2">
                  Not bound yet
                </slot>
                <!-- </MHeadComp> -->
              </template>
            </v-card>
          </v-col>
          <v-col cols="3">
            <v-img 
              width="204"
              height="211"
              src="../../assets/images/addins/nulsRocket.png" 
            />
          </v-col> 
        </v-row> 
      </v-col> 
    </v-row> 
    <v-row> 
      <v-col> 
        <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
        <!--        # # #   -->
        <!-- FORMcard ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
        <v-card
          id="vcardforform"
          ref="formrefc"
          width="100%"
          flat
          class="d-flex flex-inline-row justify-around pa-4 ma-0" 
          color="orange"
          basematcard
        >
          <!--    # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
          <!-- form  # # # #  # # # #  # #  # # # ## #  # # # ## # #  -->
          <v-form
            id="mainform"
            ref="formref"
            :key="resetform"
            vcardforform
            :style="`flat=true; width='100%'`" 
            @submit.prevent
          >     
            <!-- card group: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
            <v-row>
              <v-card
                id="surroundcards"
                width="90%"
                flat
                color="grey lighten-4"
                class="d-flex flex-row flex-wrap justify-space-between px-6 py-1 mx-0 my-0"
              >
                <!-- choice card: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
                <v-card 
                  id="vmd1card"
                  v-bind="cardprops"
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
                    v-bind="chipprops"
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
                  v-bind="cardprops"
                >
                  <v-card-subtitle
                    id="vmd2cardsubt"
                    vmd2card
                    class="pb-1 mb-1 vmd2style"
                    :style="longstyle"
                  >
                    Max/Total supply when inflation ends - min: 20,000<br> 
                    Must be > than Initial Supply. Try: 210,000,000
                  </v-card-subtitle>       
                  <v-chip 
                    id="vchip2"
                    v-bind="chipprops"
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
                  v-bind="cardprops"
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
                    v-bind="chipprops"
                  >
                    <vue-autonumeric
                      id="vmd3auto"
                      v-model="vmd3"
                      :options="vmd3opts"
                      :style="vmdInputBox" 
                    />
                  </v-chip>
                </v-card>    
                <v-divider />
                <!-- 4  inflatervals Inflation Interval:  4  # # # #  # # # #  # # # #  -->
                                
                <!-- wrapped to align cards-->
                <v-card 
                  id="vmd4card"
                  v-bind="cardprops"
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
                    v-bind="chipprops"
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
                  v-bind="cardprops"
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
                    v-bind="chipprops"
                  >
                    <vue-numeric-input
                      id="vmd5id"
                      v-model="vmd5" 
                      v-bind="numericinp"
                      :value="vmd5"
                      vmd5card
                    />
                    <span style="font-size:14px"> % </span>
                  </v-chip>
                </v-card> 
              </v-card>  
            </v-row>
            <!-- # # # # # # #  *-* *-* *-* *-* *-* *-*  -->
            <v-row>
              <v-card
                id="submit-btn-card"
                width="100%"
                min-width="240px"
                class="d-flex flex-row blue justify-center align-center mx-1 mb-1"
                flat
              >
                <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                <v-btn
                  id="submitmain"
                  v-bind="subbtn"
                  :style="`text-transform:lowercase;`"
                  @submit.prevent
                  @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                >
                  <h1> make graph </h1>
                </v-btn>
              </v-card>                                                        
            </v-row>
          </v-form>                
        </v-card>
      </v-col>
    </v-row>
    <!-- plot shows up here # # # # # # # -->
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        md="12"
        sm="12"
        align="center"
      >
        <v-card
          v-if="keyShowCard"
          :key="resetImage"
          height="imgheight"
          width="imgwid"          
          class="flat transparent ml-4 mt-1 mb-2 px-0 pb-5 pt-7 justify-center align-center"
        >
          <img
            :key="resetImage"
            :src="finalIMAGE"
            height="imgheight"
            :width="imgwid"
          >
          <span style="align:left"> To save - right click on plot</span>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # 691.2  922 or 400 x 533 # # # # # -->
<script>
import Vue from 'vue'

import { acceptStr, restTypes, acctlMeths, acctlOrig, appJson, ctType, finalIPwPORT, finalIMAGEp1 } 
  from "./CreateVars.js"
// beware: arrow functions cause problems with 'this'
import axios from "axios";
import AutoNumeric from 'autonumeric'
import VueAutonumeric from '../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';
import VueNumericInput from 'vue-numeric-input'
import MHeadComp from './MHeadComp.vue'

const subbtn = {
  type: "submit",
  width: "345px",
  height: "60px",
  "min-width": "105px",
  class: "white--text hover elevation-6 teal justify-center mb-3",
}
const vmdopts = {
  digitGroupSeparator: ',',
  currencySymbol: '',
  decimalPlaces: 0,
  overrideMinMaxLimits: 'invalid'
}
const numericinp = {
  min: 0.0,
  max: 2.0,
  step: .1,
  precision: 1,
  size: '30px',
  'controls-type': 'updown',
  align: 'center',
  style: "font-size:20px; height:23px; width: 110px; color:#ffffff;",
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

const vmdInputBox = "width:140px; font-size:16px; font-weight:500; \
  line-height:23px; text-align:right; \
  padding-left:2px; padding-right:2px; \
  padding-bottom:2px; padding-top:2px; \
  margin-bottom:2px; margin-left:2px; margin-right:2px; \
  margin-top:5px; color:#000; background-color:#FFF;"

const toplines = [
  {
    id: "item1",
    thewords: "TokenLife Design Tool",
    sty: "`font-family: 'montserrat', sans-serif;font-size:52px; font-weight:900;`",
    clss: "grey--text darken2",
  },
  {
    id: "item2",
    thewords: "Input different numbers and see tokens grow over time",
    sty: "font-family:'montserrat',sans-serif; font-size:24px;  color:#424242; line-height:32px;`",
    clss: "grey--text darken3",
  },
  {
    id: "item3",
    thewords: "Disinflation begins one interval after Inflation starts",
    sty: "font-size:16px;font-family:'Roboto',sans-serif;color:#424242;line-height:92px;",
    clss: "grey--text darken3",
  },
]

const arrowvuenumeric = "font-size:20px; height:23px; width: 110px; color:#ffffff;"
const vmdHold = 'numbers only'
var flexlist = "d-flex flex-column flex-shrink-1 justify-center align-center justify-space-around"

export default {
  name: "CreateGraph",
  components: {
    VueAutonumeric,
    VueNumericInput,
    // MHeadComp,
  },

  data: () => ({
    toplines,
    longstyle: "color:#000;font-family:Roboto,sans-serif;font-size:14px!important;font-weight:400;",
    flexlist,
    subbtn,
    numericinp,
    cardclass: `${flexlist}` +  "px-1 pt-1 pb-2 ma-1",
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
    cardprops () {
      var owid = window.outerWidth
      var wid = owid < 960 ? (owid * .84) : (owid * .33)
      var flx = "d-flex flex-column flex-shrink-1 justify-center align-center"
      return {
          class: flx + "px-1 pt-1 pb-2 ma-4",
          shaped: false,
          raised: false,
          outlined: true,
          "elevation": 2,
          color: "#FFF",
          width: wid,
          "min-width": owid < 960 ? '145' : '245',              
          "max-width": "300px", 
          "border-bottom-color": "#000",
          vcardforform: true,
        }
    },
    chipprops () {
      return {
        style: "border-bottom-color:#000;",
        class: "outlined v-chip--label justify-center align-center white medium elevation-2 pr-2",
      }
    },
    greygrad () {
      return "background-image: linear-gradient(306deg, #fbe9e7, #e0f2f1)" 
    },
    imgwid () {
      return window.outerWidth < 960 ? '533' : '922'   
    },
    imgheight () {
      return window.outerWidth < 960 ? '400' : '691'   
    },
    cardtopmarg () {
      return window.outerWidth < 960 ? 'margin-top:12px' : 'margin-top:65px'   
    },
    cardwidth () {
      return window.outerWidth < 960 ? (window.outerWidth * .84) : (window.outerWidth * .33)
    },
  },
  mounted () {
    console.log("---window.outerWidth " + window.outerWidth)
    console.log("---window.innerWidth " + window.innerWidth)
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
  }
}
 // let aw = "&initsup=100000000"; // let bw = "&anninf=5000000" // let cw = "&startinf=24" // let dw = "&stopinf=210000000" // let ew = "&disinf=4" // let dw = "&stopinf=210000000";
</script>
<style src="@/assets/styles/mystyle.css">
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital@1&display=swap');

.vue-numeric-input .btn-decrement .btn-icon:before .numeric-input {
      background-color: #ffffff!important;
}

/* .vmd2style {
  color:#BF360C;
  font-family:Roboto,sans-serif;
  font-size:15px!important;
  font-weight:500;
} */

/* // import { extend, ValidationObserver, ValidationProvider, } from 'vee-validate'
// import { max,  min,  numeric,   required, } from 'vee-validate/dist/rules'
// console.log("initsupply finalIPwPORT at top: " + initsupply, finalIPwPORT +  finalIMAGEp1)
// extend('max', max) // extend('min', min) // extend('numeric', numeric) // extend('required', required)
// Vue.component('validation-provider', ValidationProvider)
// Vue.component('validation-observer', ValidationObserver) */
/* .creategreygrad {
    background-image: linear-gradient(306deg, #3A5765 0%, #476472 100%);
    box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
} */


/* .boxshadeorig {
      box-shadow: 0px 3px 5px -1px rgba(147, 90, 201, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
      0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
} */

/* .subtstyle {
    color: #3A5765;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    margin-bottom: 4px; 
    padding-bottom: 4px;
  } */

/* .substyle3 {
  color:purple;
  font-family:Roboto,sans-serif;
  font-size:15px!important;
  font-weight:600;
} */

</style>
