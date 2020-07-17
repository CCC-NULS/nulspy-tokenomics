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
              id="vmd4card"
              color="teal lighten-5"
              width="175px"
              height="79px"
              class="vmdinps3 pa-3 cyan--text text--darken-2"
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
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import VueNumeric from 'vue-numeric'
import VueAutonumeric from '../../../../node_modules/vue-autonumeric/src/components/VueAutonumeric';
// E:\wsvue\tokenlifevue/node_modules/vue-autonumeric/src/components/VueAutonumeric.vue
//                 :style="{'font-size': '18px'}" 
//   myfont: "font-size:18px",

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
  }
  .my18font {
    font-size:  '18px',
  }
</style>