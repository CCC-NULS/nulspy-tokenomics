<template>
  <v-card
    id="childslot"
    light
    v-bind="cardprops"
    :stuf="stuf"
    :class="`${cardclss}`"
  >
    <v-chip
      v-bind="tchipprops"
    >
      <slot name="leadd">
        replacemelead
      </slot>
    </v-chip>

    <span
      :class="themefont"
    >
      {{ stuf.parag }}
    </span>
  </v-card>
</template>

<script>
  const tchipprops = {
    color: 'grey darken-3',
    textColor: 'white',
    flat: true,
    dark: true,
    label: true,
    class: 'montser mb-0 pr-2 ml-n7 mt-n1', 
    style: "line-height:20px; padding-right:9px; box-shadow: 1px 2px 2px -1px grey;",
  }

const cardclss = "pr-12 pt-6 ml-14 mr-14 mt-3 py-3"

const cardprops = {
    color: "switchlightgrey4",
    dark: false,
    align: "left",
    elevation: 4,
    style: "font-size:20px; line-height:24px; padding-left:70px;",
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
      txtclss,
      cardclss,
      tchipprops,
      cardprops,
    }),
    computed: {
      themefont () {
        return this.$vuetify.dark ? "grey--text darken2" : "grey--text darken2"
      }
    },
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
