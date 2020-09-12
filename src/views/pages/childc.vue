<template>
  <v-card
    id="childslot"
    height="auto"
    width="97%"
    left
    elevation-4
    color="switchlightgrey4"
    class="px-12 py-6 ml-14 mr-14 mt-3 align=left"
    :style="`font-size:19px; line-height:24px; text-align:left !important;`"
  >
    <v-chip
      label
      class="montser mb-0 pr-2 ml-n7 mt-n1 grey--text text--darken1" 
      v-bind="tchipprops"
    >
      <slot name="leadd">
        replacemelead
      </slot>
    </v-chip>

    <span
      :class="themefont" 
      :style="`text-align:left!important;`"
    >
      <slot name="paragg">
        replacemeparag
      </slot>
    </span>
  </v-card>
</template>

<script>
  const tchipprops = {
    color: 'grey darken-1',
    textColor: 'white',
    dark: true,
    style: "line-height:20px; box-shadow: 1px 2px 2px -1px;",
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
