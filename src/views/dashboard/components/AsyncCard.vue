<template>
  <v-card
    v-if="dataloaded"
    id="asynccard"
    name="asynccard"
  >
    <v-img
      :src="bstr + incomingstr + svgstr"
    />

    bstr passed in: {{ bstr }}
  </v-card>
</template>

<script>

  const bstr = "http://westteam.nulstar.com:8001/plots"
  const svgstr = ".svg"
  
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
    },

    data: () => ({
      bstr,
      svgstr,
      dataloaded: false,
      titlewords: 'abc',
      }),
    

    async created() {
      await sleep(4000);
      this.dataloaded = true;

    },
  }
</script>
