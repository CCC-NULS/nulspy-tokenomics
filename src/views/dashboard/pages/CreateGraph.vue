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
                    <!-- choice chip:  # # # #  # # # #  # # # #  -->
                    <!--:items="initsupply" -->

                    <v-select
                      id="vselone"
                      v-model="vmd1"
                      class="margleft"
                      type="string"
                      label="Initial Token Supply"
                      :placeholder="chooseDefault"                      
                      :items="initsupply"
                    />
                  </v-col>

                  <!--2   annual inflation:  2  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vseltwo"
                      v-model="vmd2"
                      type="string"
                      label="Annual Inflation"
                      :placeholder="chooseDefault"                      
                      :items="aninflation"                     
                    />
                  </v-col>
                </v-row>

                <v-row>
                  <!-- 3  inflatervals Inflation Interval:  3  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselthree"
                      v-model="vmd3"
                      type="string"
                      label="# of Intervals before Inflation/Disinflation Start"
                      class="margleft"
                      :placeholder="chooseDefault"                      
                      :items="inflatervals"
                    />
                  </v-col>
                  <!-- stop inflation: 4  # # # # stopinflation 4  # # # #  # # # #  -->

                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselfour"
                      v-model="vmd4"
                      type="string"
                      label="Stop Inflation"
                      :placeholder="chooseDefault"                      
                      :items="stopinflation"
                    />
                  </v-col>

                  <v-col
                    cols="12"
                    md="3"
                  >
                    <!-- disinflation # select # five five:  # # # #  # # # #  # # # #  -->
                    <v-select
                      id="vselfive"
                      v-model="vmd5"
                      type="string"
                      label="Disinflation Ratio %"
                      class="margright"
                      :placeholder="chooseDefault"                      
                      :items="disinflation"
                    />
                  </v-col>
                </v-row>
                <v-card
                  width="120px"
                  flat
                >
                  <v-text-field
                    id="testfield"
                    v-model="vmd6"
                    type="string" 
                    label="label"                 
                  >
                    Test Field Input
                  </v-text-field>
                </v-card>
                <v-btn
                  id="submitmain"
                  type="submit"
                  size="large"
                  color="warning"
                  @submit.prevent
                  @click="makePlot(vmd1, vmd2, vmd3, vmd4, vmd5, vmd6)"
                >
                  submit form
                </v-btn>
                <div>
                  <br>
                </div>
              </v-card>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <base-material-card
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

          <!-- <v-btn
            id="savebtn"
            color="purple"
            @click="keepplot"
          >
            Save Plot           
          </v-btn> -->
        </v-card>
      </v-col>
    </v-row>
    <v-alert
      v-model="alert"
      border="left"
      close-text="Close Alert"
      color="deep-purple accent-4"
      dark
      dismissible
    >
      Your plot has been saved.
    </v-alert>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
import { initsupply, aninflation, inflatervals, stopinflation, disinflation, acceptStr,
  restTypes, acctlMeths, acctlOrig, appJson, ctType, finalIPwPORT, finalIMAGEp1 } 
  from "./CreateCars.js"
import {required, minLength, maxLength } from 'vuelidate/lib/validators' 

// import { mapState, mapMutations, mapActions, mapGetter } from "vuex";
// beware: arrow functions cause problems with 'this'
import axios from "axios";
import TopWords from "@/views/dashboard/components/TopWords";
console.log("initsupply: ", initsupply)
console.log("finalIPwPORT at top: ", finalIPwPORT)
console.log("finalIMAGEp1 at top: ", finalIMAGEp1)


export default {
  name: "CreateGraph",
  components: {
    TopWords,
  },
  data: () => ({
    showme: true,
    alert: false,
    initsupply,
    chooseDefault: "Choose",
    chipprops: {
      class: "v_chip_small",
      small: true,
      dark: false
    },
    resetform: 0,
    resetImage: 0,
    finalIMAGEp1,
    finalIPwPORT,
    finalIMAGE: '',
    vmd1: '',
    vmd2: '',
    vmd3: '',
    vmd4: '',
    vmd5: '',
    vmd6: '',
    initsupply,
    aninflation,
    inflatervals,
    stopinflation,
    disinflation
    }),
  validations: {
    testfield:  { 
      required, 
      minLength: minLength(3), 
    }             
  },
  methods: {   
    checkPic (finimag) {
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
    makePlot(aa, bb, cc, dd, eee, ff) {   
      let ee = eee.substring(2,3)
      console.log("ee: " + ee)
      console.log("ff: " + ff)

      let a = "100,000,000"  // default
      let b = "1,000,000"  // default
      let c = "12"     // default
      let d = "110,000,000"    // default
      let e = "2"     // default
      if (aa.length > 4) { a = aa; }
      if (bb.length > 4) { b = bb; }
      if (cc.length > 1) { c = cc; }
      if (dd.length > 4) { d = dd; }
      if (ee.length > 0) { e = ee; }

      console.log(`a is ${a} ${a.length} b is ${b} ${b.length} d is ${d} ${d.length}`);

      let ddte = Date.now().toString();
      const gDate = ddte.substring(7,13);
      this.$store.dispatch('gSessionStrAct', gDate);
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
      resetform += 1;
      alert("You have reset the form")
    },
    keepplot() {
      console.log("in keepplot");
      this.alert=true
    },
  }
}
 // let aw = "&initsup=100000000"; // let bw = "&anninf=5000000" // let cw = "&startinf=24" // let dw = "&stopinf=210000000" // let ew = "&disinf=4" // let dw = "&stopinf=210000000";
</script>
<style src="@/assets/styles/mystyle.css">
</style>
