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
                  submitform
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
        <v-card
          id="plotcard"
          color="success"
          min-height="300px"
          min-width="600px"
        >
          <div 
            v-for="(data, key) in imgURL" 
            :key="key"
          >
            <ImgComp :url="data" />
          </div>
        </v-card>
        <v-card
          id="buttoncard"
          color="success"
          class="padbotcard"
          elevation-24
          raised
        >
          <v-btn
            id="redobtn"
            @click="resetc"
          >
            Redo
          </v-btn>
          <v-alert 
            type="success" 
            :value="alert"
          >
            You have reset the values
          </v-alert>
          <v-btn
            id="savebtn"
            color="purple"
            @click="keepplot"
          >
            Show Plot
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

    <!-- # # # #  # #  # # # #  # # # # # # #  # #  # # # # # # # # -->
<script>
// beware: arrow functions cause problems with 'this'

// import Vue from "vue";
const rax = require('retry-axios');

import axios from "axios";
// import store from "@/store";
import { mapState, mapMutations, mapActions, mapGetter } from "vuex";
import TopWords from "@/views/dashboard/components/TopWords";
import ImgComp from "@/views/dashboard/components/ImgComp"
const acceptStr ="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
const restTypes = "GET, POST, HEAD, UPDATE, PUT";
const acctlMeths = "Access-Control-Allow-Methods";
const acctlOrig = "Access-Control-Allow-Origin";
const appJson = "application/json";
const ctType = "Content-Type";
const axiosi = axios.create({
  defaults: {
    headers: {
      post: { Accept: acceptStr, acctlMeths: restTypes, ctType: appJson },
      get: { Accept: acceptStr, acctlMeths: restTypes, ctType: appJson },
      common: { acctlOrig: "*" }
    },
  },
});
var self = this
var plott = "777777";  // not in store
var pythonHost= "http://127.0.0.1:8084/"
var cubepath = `${pythonHost}static/plot${plott}.svg`;
console.log("cubepath: " + cubepath);

var juststarting = 0;
const chooseDefault = "Choose";
var vari = '777779'
// const plotpad = {
//   class: 'padplot pl-2',
//   raised: true,
//   'elevation-24': true,
//   'min-height': '22',
//   'min-width': '222',
// }

var plotlist = [];
console.log("this2: " + this)

export default {
  name: "CreateGraph",
  components: {
    TopWords,
    ImgComp,
  },
  data: () => ({
    "imgURL": {
      test1: "777777",  // base empty
      test2: vari,
    },
    chooseDefault,
    // plotpad,
    chipprops: {
      class: "v_chip_small",
      small: true,
      dark: false
    },
    cubepath,  // not real plot
    resetform: 0,
    globDate: "777777",
    alert: false,
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
  
  computed: {
    plotpath2: function ()  {
      // http://127.0.0.1:8084/static/plot766080.svg
      var pythHost= "http://127.0.0.1:8084/"
      let ptwo = this.globDate  // 
      var plottwo = `${pythHost}static/plot${ptwo}.svg`;  // reading from here

      console.log("computed date: " + ptwo)
      //var ptwo = "cube2.svg" ;        // replace this one with real plot 
      console.log("plottwo: " + plottwo)
      return plottwo
    }
  },

  created() {
    this.getLink();
  },
 
  mounted() {
    this.juststarting = 0;
    console.log("in mounted: juststarting: " + this.juststarting);
  },
  methods: {     
    read_plot () {
    if (el.length) {
        // Do something with el
      } else {
        setTimeout(pollDOM, 300); // try again in 300 milliseconds
      }
    },
    getRealImg(baseurl) {
      try {
        console.log("inside getRealImg: " + baseurl);
        (async () => {
          let response = await axiosi({
            url: baseurl,
            method: "get"
          });
        })();
      } catch (e) {
        console.log(e);
      }
      // this.showme = true
    },
   arPython(baseurl) {
      try {
        console.log("inside arPython: " + baseurl);
        (async () => {
          let response = await axiosi({
            url: baseurl,
            method: "post"
          });
        })();
      } catch (e) {
        console.log(e);
      }
      // this.showme = true
    },
    async getLink(newvar){
      let response = await cksame({
        imgURL : this.url
    })
    console.log(response.data)
    this.link = response.data
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

      console.log(`a is ${a} ${a.length}`);
      console.log(`b is ${b} ${b.length}`);
      console.log(`d is ${d} ${d.length}`);

      let ddte = Date.now().toString();
      var tdate = ddte.substring(7,13);
      this.$store.dispatch('gSessionStrAct', tdate);
      this.globDate = tdate
      // console.log("this6 : " + this);
      console.log(`tdate makePlot: ${tdate}  juststarting: ${this.juststarting}`);

      console.log("a: " + a + " b: " + b + " d: " + d);
      let aw = '&initsup=' + a.replace(/,/g, '');
      let bw = '&anninf=' + b.replace(/,/g, '');
      let cw = '&startinf=' + c;
      let dw = '&stopinf=' + d.replace(/,/g, '');
      let ew = "&disinf=" + e;
      // need to remove comma's twice from a, b, d
      let results = 0;

      let requestVars = aw + bw + cw + dw + ew + `&timestp=${tdate}`;
      var pythonIPport = "http://127.0.0.1:8084"

      let pythonUrl = `${pythonIPport}/getpy?${requestVars}`;
      let createdGraph = `${pythonIPport}/static/plot${tdate}.svg`;
      console.log("juststarting before request: " + this.juststarting);
      this.arPython(pythonUrl);

      console.log(`The plot Url is: ${createdGraph}`);
      this.juststarting = +1;

      // console.log("results: " + this.results);
    },
    resetc() {
      console.log("resetting form");
      // this.resetform += 1;
      // this.alert = true;
    },
    keepplot() {
      console.log("in keepplot");
    }
  }


//      // let aw = "&initsup=100000000"; // let bw = "&anninf=5000000" // let cw = "&startinf=24" // let dw = "&stopinf=210000000" // let ew = "&disinf=4" // let dw = "&stopinf=210000000";

</script>
<style src="@/assets/styles/mystyle.css">
</style>
