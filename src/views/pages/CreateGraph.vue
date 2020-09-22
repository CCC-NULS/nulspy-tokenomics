<template>
  <v-container
    id="create-graph"
    fluid
    tag="section"
  >
    <v-row
      class="d-flex flex-align-start"
      no-gutters
    >    
      <v-col 
        cols="12"
        md="10"
        xs="12"
      >
        <v-card
          id="maincard"
          height="auto"
          color="switchlightgrey3"
          class="pb-3 mb-2 ml-0 pl-1 mr-0"
        >
          <v-row
            no-gutters
            class="d-flex flex-column align-center"
          >           
            <template v-for="(stuf, i) in items">
              <span 
                slot
                :key="i"
                name="newslot"
                :style="stuf.sty"
                :class="stuf.clss"              
              >
                {{ stuf.thewords }} <br>
              </span>
            </template>     
          </v-row> 
          <!-- FORM ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <!--        # # #   -->
          <!-- FORMcard ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - FORM - ^^^^^^^^^^ -->
          <v-row> 
            <v-card
              id="vcardforform"
              ref="formrefc"
              width="100%"
              flat
              class="transparent d-flex flex-inline-row justify-around pl-3 py-1 ml-3 mt-1" 
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
                  <v-col :class="colstwelvsix">
                    <childcardm :slotwords="slotonewords">
                      <template v-slot:slotone>
                        <span style="color:switchdarkgrey5;font-weight:900;">                      
                          {{ slotonewords.s1 }} <br>  {{ slotonewords.s2 }}
                        </span>
                      </template>
                      <template v-slot:slottwo>                 
                        <vue-autonumeric
                          v-model="vmd1"
                          :options="vmd1opts"
                          :style="vmdInputBox"
                        />                
                      </template>
                    </childcardm>
                  </v-col>
                  <!-- Max Supply: 2  # # # # Max Supply: 2  # # # #  # # # #  -->
                  <v-col :class="colstwelvsix">           
                    <childcardm :slotwords="slottwowords">
                      <template v-slot:slotone>
                        <span style="color:switchdarkgrey4;font-weight:900;">                      
                          {{ slottwowords.s1 }} <br>  {{ slottwowords.s2 }}
                        </span>
                      </template>
                      <template v-slot:slottwo>                    
                        <vue-autonumeric
                          id="vmd2auto"
                          v-model="vmd2"
                          :placeholder="vmdHold"
                          :options="vmd2opts"
                          :style="vmdInputBox" 
                        />         
                      </template>
                    </childcardm>    
                  </v-col>          
                </v-row>            
                <!--3   annual inflation:  3  # # # #  # # # #  # # # #  -->
                <v-row>
                  <v-col :class="colstwelvsix">              
                    <childcardm>
                      <template v-slot:slotone>
                        <span style="color:switchdarkgrey4;font-weight:900;">                      
                          {{ slotthreewords.s1 }} <br>  {{ slotthreewords.s2 }}
                        </span>
                      </template>
                      <template v-slot:slottwo> 
                        <vue-autonumeric
                          id="vmd3auto"
                          v-model="vmd3"
                          :options="vmd3opts"
                          :style="vmdInputBox" 
                        />
                      </template>
                    </childcardm>  
                  </v-col>       
                  <!-- 4  inflatervals Inflation Interval:  4  # # # #  # # # #  # # # #  -->         
                  <v-col :class="colstwelvsix"> 
                    <childcardm>
                      <template v-slot:slotone>
                        <span style="color:switchdarkgrey4;font-weight:900;">                      
                          {{ slotfourwords.s1 }} <br>  {{ slotfourwords.s2 }}
                        </span>
                      </template>
                      <template v-slot:slottwo> 
                        <vue-numeric-input 
                          id="vmd4id"
                          v-model="vmd4" 
                          v-bind="fourprops"
                          :value="vmd4"
                        />                
                      </template>
                    </childcardm>
                  </v-col>       
                </v-row>
                <!--  5  5  Disinflation ratio:    5  5  # # # #  # # # #  # # # #  -->
                <v-row>
                  <v-col :class="colstwelvsix">
                    <childcardm>
                      <template v-slot:slotone>
                        <span style="color:switchdarkgrey4;font-weight:900;">                      
                          {{ slotfivewords.s1 }} <br>  {{ slotfivewords.s2 }}
                        </span>
                      </template>
                      <template v-slot:slottwo> 
                        <vue-numeric-input
                          id="vmd5id"
                          v-model="vmd5" 
                          v-bind="numericinp"
                          :value="vmd5"
                        />
                        <span style="font-size:14px"> % </span>
                      </template>
                    </childcardm> 
                  </v-col>
                  <!-- # # # # # # #  *-* *-* *-* *-* *-* *-*  -->
                  <v-col :class="colstwelvsix">                 
                    <template v-for="(stuf, i) in notes">
                      <span 
                        slot
                        :key="i"
                        name="newslot"
                        style="font-size:14px;"
                        :style="stuf.sty"
                        :class="stuf.clss"              
                      >
                        {{ stuf.thewords }} <br><br>
                        Watch for graph below<br>
                        Right click on plot to Save

                      </span>
                    </template>     
                  </v-col>
                </v-row>

                <v-row>
                  <v-card
                    id="submit-btn-card"
                    v-bind="subcardprops"
                  >
                    <!-- submit button *-* *-* *-* *-* *-* *-*  -->
                    <v-btn
                      id="submitmain"
                      v-bind="subbtn"
                      submit-btn-card
                      @submit.prevent
                      @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5)"
                    >
                      <h1>{{ subbtn.twords }}</h1>
                    </v-btn>
                  </v-card> 
                </v-row>                                                       
              </v-form>                
            </v-card>
          </v-row>
        </v-card>
      </v-col>
      <v-col 
        cols="2"
        md="2"
        xs="d-none"
        class="d-xs-none d-md-flex"
      > 
        <!-- rocket Nuls graphic shows up here # # # # # # # -->
        <v-card
          v-if="bigs"
          id="rockcard"
          :key="bigs"
          flat
          color="transparent"
          width="224"
          height="233"
          class="ml-6"
        >
          <v-img 
            src="@/assets/images/nulsrocket.jpg"
          />
        </v-card>
      </v-col>       
    </v-row>
    <!-- plot shows up here # # # # # # # -->
    <v-row>
      <v-col
        cols="12"
      >
        <!-- <v-card
          id="spacercard"
          flat
          height="5px"
          width="90%"
          color="transparent"
        /> -->
        <v-img
          :key="resetImage"
          :src="finalIMAGE"
          contain
        />    
        <br><br>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # 691.2  922 or 400 x 533 # # # # # -->
<script>
import Vue from 'vue'
import https from 'https'

import { acceptstretc, getpostetc, accessmethods, accesscontrol, plaintext, contenttype, finalPOST, 
  aclh, aclhlist, maxage, maxageval, finalGET } 
  from "./CreateVars.js"
// beware: arrow functions cause problems with 'this'
import axios from "axios";
import AutoNumeric from 'autonumeric'
import VueAutonumeric from '../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';
import VueNumericInput from 'vue-numeric-input'
import Childc from './childc'
import Childcardm from './childcardm'

const subbtn = {
  type: 'submit',
  width: '220',
  height: '50px',
  'min-width': '105px',
  class: 'white--text hover elevation-6 teal justify-center mb-2',
  twords: 'make graph',
  style: "text-transform:lowercase;margin-top:0px",
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
  style: 'font-size:20px; height:23px; width: 110px; color:#ffffff;',
}

const fourprops = {
  min: 0, 
  max: 100,
  step: 1,
  precision: 0,
  size: '20px',
  'controls-type': 'updown',
  align: 'center',
  style: 'font-size:20px; height:23px; width: 110px; color:#ffffff;'
}

const subcardprops = {
  width: '90%',
  'min-width': 'window.outerWidth < 960 ? 175 : 240',
  class: 'd-flex flex-row transparent justify-center align-center mx-1 mt-0 mb-4',
  flat: true,
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

const vmdInputBox = 'width:140px; font-size:20px; font-weight:700; \
  line-height:29px; text-align:right; \
  padding-left:2px; padding-right:2px; \
  padding-bottom:2px; padding-top:2px; \
  margin-bottom:1px; margin-left:2px; margin-right:2px; \
  margin-top:2px; color:#000; background-color:transparent;border-bottom-color:#FF0000;'

const items = [
  {
    thewords: 'TokenLife Design Tool',
    sty: 'font-family:Roboto, sans-serif;font-size:72px; font-weight:900; margin-left:2px;',
    clss: 'info--text'
  },
  {
    thewords: "Input numbers - Watch tokens grow",
    sty: "font-family:'montserrat',font-weight:700;font-size:24px;sans-serif font-size:24px;color:#424242;line-height:32px;",
    clss: 'primary--text'
  },
]

const notes = [
  {
    thewords: "Note: Disinflation begins one interval after Inflation starts",
    sty: "font-size:16px;font-family:'Roboto',sans-serif;color:#424242;line-height:20px;",
    clss: 'primary--text'
  }
]
const arrowvuenumeric = "font-size:20px; height:23px; width: 110px; color:#ffffff; text-align:center!important;"
const vmdHold = 'numbers only'
var flexlist = "d-flex flex-column flex-shrink-1 justify-center align-center justify-space-around"
const cardclass = flexlist +  " px-1 pt-1 pb-1 ma-1"

const slotonewords = {
  s1: "Initial Token Supply - Min 10,000",
  s2: "Suggestion: 100,000,000"
}
const slottwowords = {
  s1: "Total supply @ inflation end - min: 20k",
  s2: "Must be > Initial Supply-try 210,000,000"
}
const slotthreewords = {
  s1: "Annual Inflation - Min 1,000",
  s2: "Try: 5,000,000"
}
const slotfourwords = {
  s1: "Inflation starts in how many intervals ",
  s2: " (usually months) Try: 24"
}
const slotfivewords = {
  s1: "Disinflation Ratio:  Min 0, Max 2.0  ",
  s2: " Try: 0.4"
}

export default {
  name: "CreateGraph",
  components: {
    VueAutonumeric,
    VueNumericInput,
    childcardm: Childcardm,
  },

  data: () => ({
    items,
    fourprops,
    subcardprops,
    notes,
    flexlist,
    bigs: true,
    slotonewords,
    slottwowords,
    slotthreewords,
    slotfourwords,
    slotfivewords,
    subbtn,
    numericinp,
    cardclass,
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
    finalPOST,
    finalIMAGE: '',
    colstwelvsix: { cols: '12', md: '6' }
    }),
  computed: {
    showimg () { 
      return this.bigs ? true : false
    },
    plotwid () { 
      return this.bigs ? 922 : 461
    },
    plotheight () {  
      return this.bigs ? 691 : 345
    },
    plotcardwid () {
      return this.bigs ? 1022 : 511
    },
    plotcardheight () {
      return this.bigs ? 900 : 845
    },
    plotcardheightmax () {
      return this.bigs ? 2200 : auto
    },
  },
  mounted () {
    console.log("---window outerWidth " + window.outerWidth)
    console.log("---window innerWidth " + window.innerWidth)
    this.bigs = window.outerWidth > 960 ? true : false
  },
  // we only get the images - the plots and the rocket picture
  methods: {  
    checkPic (finimag) {
      this.keyShowCard += 1;
      const axiosGet = axios.create({    
        headers: {
          "Accept": "image/png,image/svg+xml", 
          accessmethods: getpostetc, 
          contenttype: plaintext ,
          accesscontrol: "*",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
          aclh: aclhlist,
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
      }) 
    }, 
    axiosPost(baseurl) {
      const axiosi = axios.create({
        headers: {
          "Accept": acceptstretc,
          accessmethods: getpostetc, 
          contenttype: plaintext,
          accesscontrol: "*",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
          aclh: aclhlist,
        },
        httpsAgent: new https.Agent({ keepAlive: true }),
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

      this.finalIMAGE = `${this.finalGET}${gDate}.svg`
      let pyReq = `${this.finalPOST}/getpy?${requestVars}`;    // either

      console.log('The this.finalPOST is: ' + this.finalPOST);
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

.vue-numeric-input .btn-decrement .btn-icon:before .numeric-input {
      background-color: #ffffff!important;
}
</style>
