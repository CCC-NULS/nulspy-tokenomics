<template>
  <v-card
    id="Childc"
    slot
    name="Childc"
    label
    x-large
    :color="color"
    :parag="parag"
    :lead="lead"
  >
    <v-chip 
      x-large
    >
      {{ lead }}
    </v-chip>

    {{ parag }}
  </v-card>
</template>

<script>
  export default {
    name: 'Childc',
    props: {
      color: {
        type: String,
        default: "green",
      },
      lead: {
        type: String,
        default: "Hi there lead",
      },
      parag: {
        type: String,
        default: "Hi there twords",
      },
      
    },
    // props: {
    //   mytext: {
    //     type: String,
    //     default: "howdy doody",
    //   },
    
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
