<template>
  <v-card
    v-if="dataloaded"
    id="asynccard"
    name="asynccard"
  >
    <v-img
      :src="bstr + incomingstr + svgstr"
    />
  </v-card>
</template>

<script>
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  export default {
    name: 'AsyncCard',
    props: {
      incomingstr: {
        type: String,
        default: 'empty',        
        },
    },
    data: () => ({
      bstr: "http://westteam.nulstar.com/tokenlife/plots",
      svgstr: ".svg",
      dataloaded: false,
      }),
    async created() {
      await sleep(5000);
      this.dataloaded = true;
    },
  }
</script>
