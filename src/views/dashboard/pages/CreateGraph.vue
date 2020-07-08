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
                      :items="initsupply"
                      value="100,000,000"
                      placeholder="100,000,000"
                    />
                  </v-col>

                  <!-- annual inflation:  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vseltwo"
                      v-model="vmd2"
                      type="string"
                      label="Annual Inflation"
                      :items="aninflation"
                      value="1,000"
                      placeholder="1,000"
                    />
                  </v-col>
                </v-row>

                <v-row>
                  <!-- annual inflation:  # # # #  # # # #  # # # #  -->
                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselthree"
                      v-model="vmd3"
                      type="string"
                      value="12"
                      placeholder="12"
                      label="Inflation Interval"
                      class="margleft"
                      :items="inflatervals"
                    />
                  </v-col>
                  <!-- stop inflation:  # # # #  # # # #  # # # #  -->

                  <v-col
                    cols="12"
                    md="4"
                  >
                    <v-select
                      id="vselfour"
                      v-model="vmd4"
                      value="120,000,000"
                      placeholder="120,000,000"
                      type="string"
                      label="Stop Inflation "
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
                      value="1"
                      placeholder="1"                      
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
          class="padplot"
          pl-2
          elevation-24
          raised
          min-height="22"
          min-width="222"
        >
          <component 
            :is="PlotCard" 
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
            :value="alert">
            You have reset the values
          </v-alert>
          <v-btn
            id="savebtn"
            color="purple"
            @click="keepplot"
          >
            Save
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

var plotlist = [];
export default {
  name: "CreateGraph",
  components: {
    TopWords,
    PlotCard: EmptyComp,
  },
  data: () => ({
    datestr: 'g',
    chipprops: {
      class: "v_chip_small",
      small: true,
      dark: false
    },
    juststarting: 0,
    showme: false,
    globaldate: null,
    resetform: 0,
    alert: false,
    vmd1: "",
    vmd2: "",
    vmd3: "",
    vmd4: "",
    vmd5: "",
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
    setTimeout(()=>{
      this.alert=false
    },5000)
  },
  mounted() {
    // this.globaldate = this.$store.state.gSessionStr;
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
      this.showme = true
    },
    makePlot(a, b, c, d, e) {
      // let tdate = this.globaldate;
      let ddte = Date.now().toString()
      var tdate = ddte.substring(7,13)
      this.globaldate = tdate;
   
      let infoo = `tdate makePlot: ${tdate}\njuststarting: ${this.juststarting}`
      console.log(infoo)

      this.$store.dispatch('gSessionStrAct', tdate)

      console.log("a: " + a + "b: " + b + "d: " + d);
      let aw = '&initsup=' + a.replace(/,/g, '')
      let bw = '&anninf=' + b.replace(/,/g, '')
      let cw = '&startinf=' + c
      let dw = '&stopinf=' + d.replace(/,/g, '')
      let ew = "&disinf=" + e;
      // need to remove comma's twice from a, b, d

      // let aw = "&initsup=100000000"; 
      // let bw = "&anninf=5000000"   
      // let cw = "&startinf=24"  
      // let dw = "&stopinf=210000000" 
      // let ew = "&disinf=4"
      // let dw = "&stopinf=210000000";
      let requestVars = aw + bw + cw + dw + ew + `&timestp=${tdate}`;
      // let baseUrl = "http://0.0.0.0:8084";  // 8084 is the flask_app
      //let baseUrl = "http://westteam.nulstar.com:8084";
      let baseUrl = "http://localhost:8084";

      let pythonUrl = `${baseUrl}/getpy?${requestVars}`;
      let mainplot = `${baseUrl}/plots/plot${tdate}.svg`;
      console.log("juststarting before request: " + this.juststarting);
      try {
        this.asyncRequestPython(pythonUrl);
      } catch (e) {
        console.log(e);
      }
      console.log(`The plot Url is: ${mainplot}`);
      this.juststarting = +1;
      console.log("juststarting: " + this.juststarting);
    },
    resetc() {
      console.log("resetting form");
      this.resetform +=1;
      this.alert=true
    },
    keepplot() {
      console.log("in keepplot");
    }
  }
};
</script>
<style src="@/assets/styles/mystyle.css">
</style>
