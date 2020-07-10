<template>
  <v-container
    id="savedgraphs"
    fluid
  >                
    <!-- %%%%%%%%%%%%%%%%% 1 %%%%%%%%%%%%%%%%%%%  PLOT 1 -->  
  </v-container>
</template>

<script>
  import axios from "axios";
  const acceptStr ="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
  const restTypes = "GET, POST, HEAD";
  const acctlMeths = "Access-Control-Allow-Methods";
  const acctlOrig = "Access-Control-Allow-Origin";
  const appJson = "application/json";
  const ctType = "Content-Type";
  const axiosi = axios.create({
    defaults: {
      headers: {
        get: { Accept: acceptStr, acctlMeths: restTypes, ctType: appJson },
        common: { acctlOrig: "*" }
      },
    },
  });


// You can chain a new promise onto the prior one, thus delaying its eventual resolution until you know the final answer. If the next answer still isn't known, then chain another promise on it and keep chaining checkStatus() to itself until eventually you know the answer and can return the final resolution. That could work like this:

  function delay(t) {
      return new Promise(function(resolve) {
          setTimeout(resolve, t);
      });
  }

  function mypromise () {
    console.log("starting in mypromise");

    let pythonIPport = "http://127.0.0.1:8084"
    let createdGraph = `${pythonIPport}/static/plot777777.svg`;
    console.log("createdGraph: " + createdGraph);
    counter = 0

    axiosi.get(createdGraph)
      .then(function (response) {
        // handle success
        console.log("success")
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log("err: " + error);
        counter += 1;
        setTimeout(() => alert('Your plot is ready to view. Press OK.'), 5000);      })
      .then(function () {
        // always executed
        console.log("done")

      });
    }

    export default {
      name: "SavedGraphs",
      data: () =>  ({
        aaa: 'loading'  
      }),
      mounted() {
        this.mypromise();
      },
      methods: {
        mypromise,
      },
    }

 
</script>
  
  