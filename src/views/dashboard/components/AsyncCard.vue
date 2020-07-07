<template>
  <v-card
    v-if="dataloaded"
    id="asynccard"
    :key="dataloaded"
    name="asynccard"
  >
    <v-img
      :key="incomingstr"
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
        default: 'e',        
        },
    },
    data: () => ({
      bstr: "http://westteam.nulstar.com/tokenlife/plots/plot",
      svgstr: ".svg",
      dataloaded: false,
      }),
    async created() {
      await sleep(4000);
      this.dataloaded = true;
    },
  }
</script>
