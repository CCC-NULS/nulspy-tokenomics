<template>
  <!-- choice card: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
  <v-card 
    v-bind="cardprops"
    color="pink"
    height="200px"
    width="500px"
  >
    <v-card-subtitle
      class="pb-1 mb-1"
      :style="longstyle"
    >
      <slot 
        name="slotone" 
        default="slotonewords"
      >
        {{ slotonewords.led1 }} <br>  {{ slotonewords.led2 }}
      </slot>
    </v-card-subtitle>

    <v-chip 
      v-bind="chipprops"
    >        
      <slot name="slottwo">
        replaceme
      </slot>
    </v-chip>
  </v-card>
</template>

<script>

  export default {
    name: 'Childcardm',
    props: {
      slotonewords: {
      led1: {
        type: String,
        default: "Initial Token Supply - Min 10,000,",
      },
      led2: {
        type: String,
        default: "Suggestion: 100,000,000",
      },   
    },   

    data: () => ({
      longstyle: "color:#000;font-family:Roboto,sans-serif;font-size:14px!important;font-weight:400;",

    }),
    computed: {
      cardprops () {
        var owid = window.outerWidth
        var wid = owid < 960 ? (owid * .84) : (owid * .33)
        var flx = "d-flex flex-column flex-shrink-1 justify-center align-center"
        return {
            class: flx + "px-1 pt-1 pb-2 ma-4",
            shaped: false,
            raised: false,
            outlined: true,
            "elevation": 2,
            // color: "#FFF",
            // width: wid,
            // "min-width": owid < 960 ? '145' : '245',              
            // "max-width": "300px", 
            // "border-bottom-color": "#000",
            vcardforform: true,
          }
      },

      chipprops () {
        return {
          style: "border-bottom-color:#000;",
          class: "outlined v-chip--label justify-center align-center white medium elevation-2 pr-2",
        }
      },
    }
  }
</script>
<style>

  .montser {
    font-family: 'Montserrat', sans-serif !important;
  }
    
  .v-chip__content {
    font-size: 19px!important;
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
