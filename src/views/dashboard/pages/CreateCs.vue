<template>
  <v-container
    id="createcs"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="12"
        md="9"
      >
        <base-material-card
          color="blue-grey"
          elevation-24
          raised
        >
          <div>
            <v-card
              id="vmd4cardff"
              width="175px"
              height="79px"
              class="vmdinps3 pa-3 cyan--text text--darken-2"
              :style="gradneww"
            >
              <span>Enter Value</span>
              <vue-autonumeric
                v-model="myValue"
                :placeholder="'Enter your value here'"
                :options="myopts"
                :style="myfont" 
              />
            </v-card>    
          </div>
          <div>
            <v-card
              id="vmd4cardgg"
              width="700px"
              height="1200px"
              class="d-flex flex-wrap align-content-start justify-space-between pa-4"
            >
              <v-card
                id="vmd4cardgg1"
                color="success"

                width="200px"
                height="200px"
                class="d-flex"
              >
                hi1
              </v-card>
              <v-card
                id="vmd4cardgg2"
                color="tertiary"
                width="200px"
                height="200px"
                class="d-flex"
              >
                hi2
              </v-card>

              <v-card
                id="vmd4cardgg3"
                color="green"
                width="200px"
                height="200px"
                class="d-flex"
              >
                hi3
              </v-card>
              <v-card
                id="vmd4cardgg4"
                color="pink"
                width="200px"
                height="200px"
                class="d-flex"
              >
                hi4
              </v-card>
              <v-card
                class="gradientnulsBG"
              >
                hidden-lg-and-down
              </v-card>
            </v-card>    
          </div>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import VueAutonumeric from '../../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';

const myopts = {
    digitGroupSeparator: ',',
    currencySymbol: '',
    // roundingMethod: 'U',
    minimumValue: '1000',
    maximumValue: '900000000000',
    decimalPlaces: 0,
}

export default {
  name: 'CreateCs',
  components: {
    VueAutonumeric
  },
  data: () => ({
    myopts,
    myfont: "font-size:18px; width:129px; justify-center",
    myValue: 5000,
    placeh: 'only number allowed'
  }),
}
</script>
<style scoped>
  .vmdinps3 {
      font-size: 16px!important;
      line-height: 30px;
      margin-top: 0px!important;

      padding-bottom: 2px!important;
      justify-content: center!important;
      text-align: center!important;
      background-image: linear-gradient(to right, #607d8b 0%, #93B0BE 100%);
      box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 
        0px 1px 18px 0px rgba(0, 0, 0, 0.12) !important;
  }


  .gradnewwg {
    background-image: linear-gradient(to right, #0acffe 0%, #495aff 100%)
  }

  .gradientdcf {
    background-image: linear-gradient(to right, rgba(33, 138, 184, 1),rgba(0, 241, 181, 1))
    }
  .gradientde {
    background-image: linear-gradient(to top, rgba(132, 110, 100, 1), rgba(101, 84, 76, 1))
    }
  .gradientnulsd {
    background-image: linear-gradient(306deg, rgba(54, 54, 54, 0.05) 0%, rgba(54, 54, 54, 0.05) 33.333%,rgba(85, 85, 85, 0.05) 33.333%, rgba(85, 85, 85, 0.05) 66.666%,rgba(255, 255, 255, 0.05) 66.666%, rgba(255, 255, 255, 0.05) 99.999%),linear-gradient(353deg, rgba(81, 81, 81, 0.05) 0%, rgba(81, 81, 81, 0.05) 33.333%,rgba(238, 238, 238, 0.05) 33.333%, rgba(238, 238, 238, 0.05) 66.666%,rgba(32, 32, 32, 0.05) 66.666%, rgba(32, 32, 32, 0.05) 99.999%),linear-gradient(140deg, rgba(192, 192, 192, 0.05) 0%, rgba(192, 192, 192, 0.05) 33.333%,rgba(109, 109, 109, 0.05) 33.333%, rgba(109, 109, 109, 0.05) 66.666%,rgba(30, 30, 30, 0.05) 66.666%, rgba(30, 30, 30, 0.05) 99.999%),linear-gradient(189deg, rgba(77, 77, 77, 0.05) 0%, rgba(77, 77, 77, 0.05) 33.333%,rgba(55, 55, 55, 0.05) 33.333%, rgba(55, 55, 55, 0.05) 66.666%,rgba(145, 145, 145, 0.05) 66.666%, rgba(145, 145, 145, 0.05) 99.999%),linear-gradient(90deg, rgb(9, 201, 186),rgb(10,64,108))
    }
  .gradnewa {
    background-image: linear-gradient(to right, #0acffe 0%, #495aff 100%)
    }
  .gradnewb {
    background-image: linear-gradient(to right, #37474F 0%, #455a63 100%)
    }
  .gradtryc   {
    background-image: linear-gradient(to right, #13547a 0%, #80d0c7 100%) 
    }
.gradientnulsBG {
  background-image: linear-gradient(306deg, rgba(54, 54, 54, 0.05) 0%, rgba(54, 54, 54, 0.05) 33.333%,rgba(85, 85, 85, 0.05) 33.333%, rgba(85, 85, 85, 0.05) 66.666%,rgba(255, 255, 255, 0.05) 66.666%, rgba(255, 255, 255, 0.05) 99.999%),linear-gradient(353deg, rgba(81, 81, 81, 0.05) 0%, rgba(81, 81, 81, 0.05) 33.333%,rgba(238, 238, 238, 0.05) 33.333%, rgba(238, 238, 238, 0.05) 66.666%,rgba(32, 32, 32, 0.05) 66.666%, rgba(32, 32, 32, 0.05) 99.999%),linear-gradient(140deg, rgba(192, 192, 192, 0.05) 0%, rgba(192, 192, 192, 0.05) 33.333%,rgba(109, 109, 109, 0.05) 33.333%, rgba(109, 109, 109, 0.05) 66.666%,rgba(30, 30, 30, 0.05) 66.666%, rgba(30, 30, 30, 0.05) 99.999%),linear-gradient(189deg, rgba(77, 77, 77, 0.05) 0%, rgba(77, 77, 77, 0.05) 33.333%,rgba(55, 55, 55, 0.05) 33.333%, rgba(55, 55, 55, 0.05) 66.666%,rgba(145, 145, 145, 0.05) 66.666%, rgba(145, 145, 145, 0.05) 99.999%),linear-gradient(90deg, rgb(9, 201, 186),rgb(96, 125, 139))
}



</style>