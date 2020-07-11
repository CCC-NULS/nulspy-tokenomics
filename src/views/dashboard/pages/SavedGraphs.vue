<template>
  <v-container
    id="savedgraphs"
    fluid
  >               
    <v-card
      v-if="showme"
      color="teal"
    >
      <img
        :src="myurl" 
      >
    </v-card>

  <!-- %%%%%%%%%%%%%%%%% 1 %%%%%%%%%%%%%%%%%%%  PLOT 1 -->  
  </v-container>
</template>

<script>
  import axios from "axios";
  const axiosobj = axios.create()
  const myurl = 'http://127.0.0.1:8084/static/plot777777.svg'
    
  const retry = require('retry');

  const operation = retry.operation({
    retries: 10,
    factor: 3,
    minTimeout: 1 * 1000,
    maxTimeout: 40 * 1000,
  });

  export default {
    name: "SavedGraphs",
    data: () =>  ({
      showme: false,
      myurl,
    }),
    mounted() {
      console.log("starting in mounted")
      operation.attempt(async (currentAttempt) => {
        console.log('sending request: ', currentAttempt, ' attempt');
        try {
          await axiosobj.get(myurl);
        } catch (e) {
          if (operation.retry(e)) { return; }
        }
        let rtos = operation.attempts()
        console.log("retries: " + rtos)
        if (rtos < 11) {
          this.showme = true
        }
      });   
    },
    methods: {
      operation,
    }
  }

</script>
