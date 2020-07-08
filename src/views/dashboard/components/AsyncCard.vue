<template>
  <v-card
    v-if="showing"
    id="asynccard"
    :key="dataloaded"
    name="asynccard"
  >
    <v-img
      :src="bstr + incomingstr + svgstr"
    />
  </v-card>
</template>

<script>
  import bstr from '../../../constants'
  console.log("bstr: " + bstr)
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  export default {
    name: 'AsyncCard',
    props: {
      incomingstr: {
        type: String,
        default: 'e',        
        },
      showing: {
        type: Boolean,
        default: false,        
        },
    },
    data: () => ({
      bstr,
      svgstr: ".svg",
      dataloaded: false,
    }),
    mounted () {
        console.log("mounted AsyncCard " )
    },    
    async created() {
      await sleep(3000)
      this.dataloaded = true
      console.log("in async created - dataloaded= " + this.dataloaded)
    },
  }
</script>



      // bstr: "http://westteam.nulstar.com/tokenlife/public/plots/plot",
      // bstr: "http://westteam.nulstar.com/tokenlife/static/plot",
      // bstr: "http://localhost:8084/tokenlifevue/static/plot",