<template>
  <v-img
    :src="ploturl"
    :key="chgdate"
  />
</template>

<script>
  // import realstr from '../../../constants.js'
  // console.log("bstr: " + bstr)
  // const bstr = 'http://localhost:8084/static/plot'
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  export default {
    name: 'FullCard',
    data: () => ({
      dataloaded: false,
    }),

    computed: {
      chgdate () { 
        return this.$store.state.gSessionStr 
      },
      ploturl () { 
        let svgst = ".svg"
        let ddate = this.$store.state.gSessionStr 
        let ptwo = ddate + svgst
        let theurl = `http://localhost:8084/static/plot${ptwo}`
        return theurl
      }
    },
    
    watch: {
      '$store.state.gSessionStr'(value, oldValue) {
      },
    },     
    
    mounted () {
        console.log("mounted FullCard")
    },    
 }
</script>
