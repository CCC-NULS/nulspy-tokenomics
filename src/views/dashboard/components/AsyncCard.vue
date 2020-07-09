<template>
  <v-card
    id="asynccard"
    name="asynccard"
  >
    <v-img
      :src="ploturl"
    />
  </v-card>
</template>

<script>
  // import realstr from '../../../constants.js'
  // console.log("bstr: " + bstr)
  // const bstr = 'http://localhost:8084/static/plot'
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  export default {
    name: 'AsyncCard',
    data: () => ({
      dataloaded: false,
    }),
    computed: {
      ploturl () { 
        let svgst = ".svg"
        let ddate = this.$store.state.gSessionStr 
        let ptwo = ddate + svgst
        let theurl = `http://localhost:8084/static/plot${ptwo}`
        return theurl
      }
    },
    mounted () {
        console.log("mounted AsyncCard")
    },    
  }
</script>
