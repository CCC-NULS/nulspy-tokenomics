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
                      v-bind="chipprops"
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
                      :value="initsupply[0]"
                      :placeholder="initsupply[0]"                     
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
                      :value="aninflation[0]"
                      :placeholder="aninflation[0]"
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
                      :value="inflatervals[0]"                   
                      :placeholder="inflatervals[0]"
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
                      label="Stop Inflation "
                      :value="stopinflation[0]"
                      :placeholder="stopinflation[0]"                      
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
          v-bind="plotpad"
        >
          <component 
            :is="pcard" 
          />
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

import Vue from "vue";
import axios from "axios";
import { mapState, mapMutations, mapActions, mapGetter } from "vuex";
import TopWords from "@/views/dashboard/components/TopWords";
import AsyncCard from "@/views/dashboard/components/AsyncCard";
import EmptyComp from "@/views/dashboard/components/EmptyComp";

import axiosRetry from "axios-retry";
const acceptStr =
  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
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
    }
  }
});
var juststarting = 0;

const plotpad = {
  class: "padplot pl-2",
  raised: true,
  'elevation-24': true,
  'min-height': "22",
  'min-width': "222",
}
var plotlist = [];

export default {
  name: "CreateGraph",
  components: {
    TopWords,
    EmptyComp,
    AsyncCard
  },
  data: () => ({
    datestr: 'g',
    chipprops: {
      class: "v_chip_small",
      small: true,
      dark: false
    },
    pcard: '',
    plotpad,
    resetform: 0,
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
  created(){
    this.pcard = false
    setTimeout(()=>{
      this.alert=false
    },100)
  },
  mounted() {
    this.juststarting = 0;
    console.log("in mounted: juststarting: " + this.juststarting);
  },
  methods: {
    asyncRequestPython(baseurl) {
      try {
        console.log("inside asyncRequestPython: " + baseurl);
        (async () => {
          let response = await axiosi({
            url: baseurl,
            method: "post"
          });
        })();
      } catch (e) {
        console.log(e);
      }
      return 1
    },
    makePlot(a, b, c, d, e) {
      let ddte = Date.now().toString()
      var tdate = ddte.substring(7,13)
      this.$store.dispatch('gSessionStrAct', tdate)
   
      console.log(`tdate makePlot: ${tdate}\njuststarting: ${this.juststarting}`)

      console.log("a: " + a + " b: " + b + " d: " + d);
      let aw = '&initsup=' + a.replace(/,/g, '')
      let bw = '&anninf=' + b.replace(/,/g, '')
      let cw = '&startinf=' + c
      let dw = '&stopinf=' + d.replace(/,/g, '')
      let ew = "&disinf=" + e;
      // need to remove comma's twice from a, b, d
      let results = 0

      let requestVars = aw + bw + cw + dw + ew + `&timestp=${tdate}`;
      // let baseUrl = "http://0.0.0.0:8084";  // 8084 is the flask_app
      //let baseUrl = "http://westteam.nulstar.com:8084";
      let baseUrl = "http://localhost:8084";

      let pythonUrl = `${baseUrl}/getpy?${requestVars}`;
      let mainplot = `${baseUrl}/static/plot${tdate}.svg`;
      console.log("juststarting before request: " + this.juststarting);
      try {
        let results = this.asyncRequestPython(pythonUrl);
      } catch (e) {
        console.log(e);
      }
      console.log(`The plot Url is: ${mainplot}`);
      this.juststarting = +1;
      console.log("results: " + this.results);
    },
    resetc() {
      console.log("resetting form");
      this.resetform +=1;
      this.alert = true
    },
    keepplot() {
      console.log("in keepplot")
      this.pcard = "AsyncCard"

    }
  }
};
//      // let aw = "&initsup=100000000"; // let bw = "&anninf=5000000" // let cw = "&startinf=24" // let dw = "&stopinf=210000000" // let ew = "&disinf=4" // let dw = "&stopinf=210000000";

</script>
<style src="@/assets/styles/mystyle.css">
</style>
