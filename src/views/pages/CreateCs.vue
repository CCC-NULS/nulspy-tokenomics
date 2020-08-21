<template>
  <v-container
    id="createcs"
    fluid
  >
    helo
  </v-container>
</template>

<script>


export default {
  name: 'CreateCs',

  data: () => ({

  }),
  mounted () {
    this.gwin()
  },
  methods: {
    gwin: function () {
      alert(window.outerWidth+' x '+ window.outerHeight);
      console.log (window.outerWidth+' x '+ window.outerHeight)
      var woutwth = window.outerWidth
      if (window.outerWidth < 960) 
        console.log("win is small")
        var nmsm = true
    }
  }
}
</script>
