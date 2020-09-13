<template>
  <v-card
    id="childslot"
    height="auto"
    width="97%"
    left
    text-left
    elevation-4
    color="grey lighten-2"
    class="px-12 py-6 ml-14 mr-14 mt-3 text-left"
    :style="`line-height:22px; text-left!important;`"
  >
    <v-chip
      label
      class="montser mb-0 pr-2 ml-n7 mt-n1" 
      v-bind="tchipprops"
      :style="fontsz"
    >
      <slot name="leadd">
        replacemelead
      </slot>
    </v-chip>

    <span
      :class="fontsize"
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
      fontsz: ' font-size:15px;',
      bigs: true,
    }),
    computed: {
      // themefont () {
      //   return this.$vuetify.dark ? " red--text text--lighten2 " : " grey--text text--darken5"
      // },
      // need extra spaces below so they can be combined with other vars with "+"
      fontsize () {
        return this.bigs ? " font-size:19px" : " font-size:15px"
      },
   },    
    mounted () {
      console.log("---window outerWidth " + window.outerWidth)
      console.log("---window innerWidth " + window.innerWidth)
      this.bigs = window.outerWidth > 960 ? true : false
      this.fontsz = this.bigs ? " font-size:19px;" : " font-size:16px;"
    },

  }
</script>
<style>

  .montser {
    font-family: 'Montserrat', sans-serif !important;
  }
    
  .v-chip__content {
    font-size: 16px!important; 
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
