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
                      label="Inflation Interval"
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
          v-if="showme"
          color="success"
          class="justify=center ml-6 mb-5 pb-5 pt-9"
        >
          <img
            v-if="showme"
            :src="finalImgUrl"
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
// beware: arrow functions cause problems with 'this'

import axios from "axios";
import { mapState, mapMutations, mapActions, mapGetter } from "vuex";
import TopWords from "@/views/dashboard/components/TopWords";

var acceptStr ="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
var restTypes = "GET, POST, HEAD, UPDATE, PUT";
var acctlMeths = "Access-Control-Allow-Methods";
var acctlOrig = "Access-Control-Allow-Origin";
var appJson = "application/json";
var ctType = "Content-Type";

export default {
  name: "CreateGraph",
  components: {
    TopWords,
  },
  data: () => ({
    showme: false,
    alert: false,
    dimform: false,
    chooseDefault: "Choose",
    chipprops: {
      class: "v_chip_small",
      small: true,
      dark: false
    },
    resetform: 0,
    // finalImgUrl: "http://127.0.0.1:8084/static/plot155414.svg",  // for test only
    finalImgUrl: '',
    vmd1: '',
    vmd2: '',
    vmd3: '',
    vmd4: '',
    vmd5: '',
    initsupply: ["300,000,000","260,000,000","225,000,000","200,000,000", "175,000,000","150,000,000","100,000,000",],
    aninflation: ["2,000,000", "3,000,000", "4,000,000", "5,000,000", "6,000,000"],
    inflatervals: ["12", "18", "24", "36", "48"],
    stopinflation: ["510,000,000","450,000,000","350,000,000", "310,000,000", "250,000,000", "155,000,000", "120,000,000"],
    disinflation: ["0", "1", "2", "3", "4", "5"]
    }),
  methods: {   
    checkPic () {
      this.dimform = true
      const axiosGet = axios.create()
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
          await axiosGet.get(this.finalImgUrl);
        } catch (e) {
          if (operation.retry(e)) { return; }
        }
        let opAttempts = operation.attempts()
        console.log("retries: " + opAttempts)
        if (opAttempts < 15) {
          this.showme = true
        }
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
    makePlot(aa, bb, cc, dd, ee) {
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
      var gDate = ddte.substring(7,13);
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

      // var pyHostHOME = "http://127.0.0.1:8084"  // home
      var pyHostWest = "http://116.202.157.151:8084"  //westteam
      var pyHostNginx = "http://116.202.157.151"  // westteam

      // let pythonRequest = `${pyHostHOME}/getpy?${requestVars}`;  // home

      let pythonRequest = `${pyHostWest}/getpy?${requestVars}`;    // westteam

      this.axiosPost(pythonRequest);  // all locations

      // this.finalImgUrl = `${pyHostHOME}/static/plot${gDate}.svg`;   // home

      this.finalImgUrl = `${pyHostNginx}/static/plot${gDate}.svg`;  // westteam -only for viewing image
      // this.finalImgUrl = `${pyHostHOME}/static/plot155414.svg`;   // hard coded for test only

      console.log(`The plot Url is: ${this.finalImgUrl}`);
      this.checkPic()
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
