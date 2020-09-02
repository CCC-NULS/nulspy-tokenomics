<template>
  <v-container
    id="Home"
    fluid
  >
    <v-row
      align="center"
      justify="center"
      class="flex-d justify-center align-center"
    >
      <div 
        v-if="$store.state.gShowMe"
      >
        Parent component contents will be here
        {{ message }}

        <v-card
          color="cyan"
          class="black--text"
          height="500px"
          min-height="200px"
          :style="`font-size:36px;font-family:Montserrat,sans-serif;`"                
        >       
          NULS Tokenomics
        </v-card>
      </div>
    </v-row>
  </v-container>
</template>

<script>
  var showhome = true

  export default {
    name: "Home",
    data: function () {
      return {
        message: "hi",
      }
    },
    computed: {
      getShowMe () {
        return this.$store.state.gShowMe;
      },
      setShowMeTrue () {
        return this.$store.dispatch('gShowMeAct', true);
      },
    },
    mounted () {
      this.setShowMeTrue
    },

  }
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

</style>
