



<template v-for="(item, i) in mylines">
  <span
    :style="`${item.sty}`"
    :class="`${item.clss}`"
  >
    {{ item.nme }}
  </span>
</template>





<script>
const mylines = [
   item1 = {
     nme: "TokenLife Design Tool",
     sty: "`font-family: 'montserrat', sans-serif;font-size:52px; font-weight:900;`",
     clss: "grey--text darken2",
   },
   item2 = {
     nme: "Input different numbers and see tokens grow over time",
     sty: "font-family:'montserrat',sans-serif; font-size:24px;  color:#424242; line-height:32px;`",
     clss: "grey--text darken3",
   },
   item3 = {
     nme: "Disinflation begins one interval after Inflation starts",
     sty: "font-size:16px;font-family:'Roboto',sans-serif;color:#424242;line-height:92px;",
     clss: "grey--text darken3",
   }]


export default {
  name: 'CreateCs',

  data: () => ({
    mylines,
  }),
  mounted () {
    // this.gwin()
  },
  methods: {
    // gwin: function () {
    //   alert(window.outerWidth+' x '+ window.outerHeight);
    //   console.log (window.outerWidth+' x '+ window.outerHeight)
    //   var woutwth = window.outerWidth
    //   if (window.outerWidth < 960) 
    //     console.log("win is small")
    //     var nmsm = true
    // }
  }
}
</script>
