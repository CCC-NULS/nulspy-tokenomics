<template>
  <v-chip
    id="Childc"
    name="Childc"
  />
</template>

<script>
  export default {
    name: 'Childc',
    props: '',
    // props: {
    //   mytext: {
    //     type: String,
    //     default: "howdy doody",
    //   },
    // },
    data: () => ({
      tchipprops: { 
        color: 'grey lighten-4',
        textColor: 'black',
        'elevation-24': true,
        class: 'label montser mb-3 pr-1', 
        style: "line-height:18px; box-shadow: 0px 2px 2px -1px grey",
      }
    })
  }
</script>
