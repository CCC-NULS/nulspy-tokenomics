<template>
  <v-container
    id="savedgraphs"
    fluid
  >               
    <v-card
      v-if="showme"
      color="teal"
    />
  </v-container>
</template>
  <!-- %%%%%%%%%%%%%%%%% 1 %%%%%%%%%%%%%%%%%%%   -->  

<script>
  // const myurl = 'http://127.0.0.1:8084/static/plot777777.svg'
    

  export default {
    name: "SavedGraphs",
    data: () =>  ({
      showme: false,
    }),
   
  }

</script>
