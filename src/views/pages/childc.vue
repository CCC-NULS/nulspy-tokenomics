<template>
  <v-card
    id="Childc"
    slot
    name="Childc"
    v-bind="cardprops"
    :parag="parag"
    :lead="lead"
    class="shaped=false"
  >
    <v-chip
      v-bind="tchipprops"
    >
      {{ lead }}
    </v-chip>
    {{ parag }}
  </v-card>
</template>

<script>
  const tchipprops = {
    color: 'grey darken-1',
    textColor: 'white',
    dark: true,
    raised: true,
    // filled: true,
    label: true,
    'elevation-24': true,
    class: 'label montser mb-0 pr-2 ml-n7 mt-n1', 
    style: "line-height:20px; padding-right:9px; box-shadow: 1px 2px 2px -1px grey",
  }

  const cardprops = {
    color: "grey lighten-4",
    align: "left",
    class: "black--text pr-12 pt-6 ml-14 mr-14 mt-3 py-3",
    elevation: 4,
    style: "font-size:16px; line-height:24px; padding-left:70px;"
  }

  export default {
    name: 'Childc',
    props: {
      lead: {
        type: String,
        default: "Hi there lead",
      },
      parag: {
        type: String,
        default: "Hi there twords",
      },   
    },   
    data: () => ({
      tchipprops,
      cardprops,
    })
  }
</script>
<style>

  .montser {
    font-family: 'Montserrat', sans-serif !important;
  }
    
  .v-chip{
      padding-right:2px;padding-left:2px;padding-bottom:2px;padding-top:2px;
  }
  .v-chip__content {
    font-size: 20px!important;
    color: white;
    padding-left: 5px;
    padding-right: 2px;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif !important;
  }

  .theme--light.v-chip {
    color: purple;
  } 
  </style>
