<template>
  <div>
    <base-material-card
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
        <plotOne />
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
  import store from '@/store'
  import { mapState } from 'vuex'  // get plot name from store
  plotpath = $store.gLocPlotPath
  import { plotOne } from 'plotpath'

  export default {
    name: 'LastCard',
    components: {
      plotOne,
    },
    data: () => ({
      placehold: 'placeholder',
    }),
  }
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
