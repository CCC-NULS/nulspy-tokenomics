<template>
  <div>
    <base-material-card
      id="plotcardlast"
      name="LastCard"
      color="warning lighten-1"
      text="Your Plot"
      class="fontchg"
    >
      <v-card
        id="vcardtwo"
        class="mr-2 mt-1 pa-2 plotcenter"
        elevation-24
        raised
        color="success"
      >
        <div 
          class="align-center" 
        >
          <LastCard2 
            is="LastCard2" 
          /> 
        </div>
      </v-card>

      <v-card class="padbot">
        <v-btn id="redobtn">
          Redo
        </v-btn>
        <v-btn
          id="savebtn"
          color="purple"
        >
          Save
        </v-btn>
      </v-card>
    </base-material-card>
  </div>
</template>

<script>
  // import store from '@/store'
  // import vuex from 'vuex'
  // // import LastCard2 from '@/views/dashboard/components/LastCard2'
  // import { mapState } from 'vuex';  // get plot name from store

  // iconPath(dynamicValue) {
  //   return require(`./${dynamicValue}.svg`)
  // }

  // export default {
  //   name: 'LastCard',
  //   props: {
  //     fname: {
  //       type: String,
  //       default: 'PLOTNAME GOES HERE',
  //     },
  //   },
  //   data: () => ({
  //     ffname: 'plottwo.svg',
  //     placehold: 'placeholder',
  //   }),

   
    // watch: {
    //   gLocPlotGet () {
    //   // Do something
    // },
    // computed: {
    //   ...mapGetters(['gLocPlotPathGet']),
    //   import myplot from gLocPlotPathGet
    // },
 
  // function have their own 'this' instance so when you call this you get the instance of the function your inside in and not the vue instance. The typical solution to this in vanilla javascript is to create a temporary variable outside the function then use it inside the function. 
  //e.g var self = this; register: function () { self.$store.commit(); }
</script>

<style>
  .plotcenter {
    display: flex;
    align-items: center;
    justify-content: center;
}
  .pcenter {
    margin-bottom: 22px;
  }
  .fontchg {
    font-size: 32px;
    font-weight: 300;
  }
  .pclass {
    margin-bottom: 22px;
  }
  .padbot {
    padding-top: 5px;
    padding-bottom: 7px;
    display: flex;
    justify-content: center;
  }
</style>
