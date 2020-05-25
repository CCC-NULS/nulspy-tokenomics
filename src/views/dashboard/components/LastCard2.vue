<template>
  <div>
    <v-card
      id="vcardtwo"
      class="plotcenter"
      elevation-24
      raised
      color="success"
    >
      <plotmain />
    </v-card>
  </div>
</template>
<script>
import plotmain from '@/assets/plots/plotmain.svg'
export default {
  name: 'LastCard2',  
  components: {
    plotmain,
  },
  data: () => ({
    plotname: "plotmain.svg",
  }),
  }
</script>

