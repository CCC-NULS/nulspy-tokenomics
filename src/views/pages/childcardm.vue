<template>
  <!-- choice card: 1  # # # #  # # # #  # #  # # # ## #  # # # ## # # #  -->
  <v-card 
    v-bind="cardprops"
    color="switchlightgrey3"
    flat
    height="125px"
    width="window.outerWidth < 960 ? 200 : 390"
    min-width="200px"              
    max-width="470px"
    min-height="70px"              
    max-height="270px"  
    :style="`padding-top:1px!important;margin-top:1px;`"
  >
    <v-card-subtitle
      class="pb-0 mb-0 mt-0 pt-0"
      :style="longstyle"
    >
      <slot 
        name="slotone" 
        slotwords="slotwords"
      />
    </v-card-subtitle>

    <v-chip
      width="200px"
      max-width="250px"
      min-width="window.outerWidth < 960 ? 145 : 150"             
      max-height="90px" 
      v-bind="chipprops"
      medium
      label
      color="white"
      :class="chipprops.clss"
      :style="chipprops.stle"
    >
      <slot name="slottwo">
        replaceme
      </slot>
    </v-chip>
  </v-card>
</template>

<script>
  const chipprops = {
      stle: "border-bottom-color:#000;",
      clss: "outlined v-chip--label justify-center align-center white medium elevation-2 pr-2 mt-1",
  }
  const ld1 = "words"
  const ld2 = "words"

  export default {
    name: 'Childcardm',
    data: () => ({
      longstyle: "padding-top:1px;font-family:Montserrat,sans-serif;font-size:16px!important;font-weight:500;",
      slotonewords: [ ld1, ld2],
      chipprops,
    }),
    computed: {
      cardprops () {
        var owid = window.outerWidth
        var wid = owid < 960 ? (owid * .84) : (owid * .33)
        var flx = "d-flex flex-column flex-xs-shrink-1 flex-md-shrink-0 justify-center align-center"
        return {
            class: flx + " px-1 pb-0 pt-0 mx-1 my-0",
            shaped: false,
            raised: false,
            outlined: false,
            // "elevation": 2,
            // color: "info",
            // width: wid,
            // "border-bottom-color": "#000",
            vcardforform: true,
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
