<template>
  <v-container
    id="savedgraphs"
    fluid
    tag="section"
  >                
    <!-- %%%%%%%%%%%%%%%%% 1 %%%%%%%%%%%%%%%%%%%  PLOT 1 --> 

    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <v-card
          id="e1card"
          class="padplot"
          pl-2
          elevation-24
          raised
        >
          <div
            id="e1cardp"
          />

          <v-btn
            id="savebtn"
            color="purple"
            @click="svgload"
          >
            Load More
          </v-btn>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        cols="12"
        md="11"
      >
        <v-card
          id="e2card"
          class="padplot"
          pl-2
          elevation-24
          raised
        >
          <div
            id="e2cardp"
            e2card
          />
        </v-card>
      </v-col>
    </v-row>
 
  
    <!-- %%%%%%%%%%%%%%%%% TWO %%%%%%%%%%%%%%%%%%%  PLOT 2 -- 
          <v-card
            id="e2card"
          >
            <e2plot
              :key="$store.state.sCounter"
              e2card
            />
          </v-card>
          < --   %%%%%%%%%%%%%%%%%%%%%%%%%   
        </v-col>
      </base-material-card>
    </v-row>

    <v-row>
      <v-col
        cols="12"
        md="12"
      >
        <base-material-card
          id="e3and4"
          color="success"
          title="Graph"
          class="px-1 py-1"
          fluid
        >
          < -- %%%%%%%%%%%%%%%%% 3 %%%%%%%%%%%%%%%%%%%  PLOT 3 
          <v-card
            id="e3card"
          >
            <e3plot
              :key="$store.state.sCounter"
              e3card
            />
          </v-card>


          <  -- %%%%%%%%%%%%%%%%% 4 %%%%%%%%%%%%%%%%%%%  PLOT 4 
          <v-card
            id="e4card"
          >
            <e4plot
              :key="$store.state.sCounter"
              e4card
            />
          </v-card>
          < --   %%%%%%%%%%%%%%%%%%%%%%%%%    
        </base-material-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          id="e5and5"
          color="success"
          title="Graph"
          class="px-1 py-1"
          fluid
        >
          < -- %%%%%%%%%%%%%%%%% 5 %%%%%%%%%%%%%%%%%%%  PLOT 5  
          <v-card
            id="e5card"
          >
            <e5plot
              :key="$store.state.sCounter"
              e5card
            />
          </v-card>

          < -- %%%%%%%%%%%%%%%%% 4 %%%%%%%%%%%%%%%%%%%  PLOT 6  
          <v-card
            id="e6card"
          >
            <e6plot
              :key="$store.state.sCounter"
              e6card
            />
          </v-card>
          <-   %%%%%%%%%%%%%%%%%%%%%%%%%    
          -->
  </v-container>
</template>

<!--   %%%  /-%%%-/%%-/  %%%-/%%-/%%-/  %%%%-/%%%-/  %%%    -->

<script>
  // import { mapState, mapMutations, mapActions } from 'vuex'  
  var bigplot

  export default {
    name: "SavedGraphs",
    components: {
      // e1plot: () => import('@/assets/plots/pltreal.svg'),
      // e2plot: () => import('@/assets/plots/bluecube.svg'),


    },
    data: () => ({
      a: 1,
      showplt: true,
    }),
    computed: {
      myobject: function () {
        let bbb = require.context('../../../assets/plots', false, /\.svg$/)
        console.log("inside svgcomputedload")
        return bbb
      }
    },
    methods: {       
      svgload: function () {
        console.log("inside svgload")
        this.bigplot = this.myobject
        return this.bigplot
      },
      // svgloadmain: function () {
      //   const reqSvgs = require.context('@/assets/plots', false, /\.svg$/)
      //   const svgs = reqSvgs
      //     .keys()
      //     .map( path => ({ path, file: reqSvgs ( path ) }) )
      //   console.log("in svgload: ")
      //   let tlen = svgs.length
      //   console.log("in svgload tlen:" + tlen)
      //   // stackoverflow.com/questions/54059179/what-is-require-context
      //   // JSON.stringify(svgs)
      //   svgs.forEach(function(path) { console.log(path);})
      //   return svgs
      // },
      // loadone: function () {
      //   console.log("in loadonenow: ")
      // },
    //   get_name_two: function () {
    //     let myPATHARRAY = this.$store.state.gPlotPATHARRAY
    //     let save_two = myPATHARRAY[1]      
    //     console.log("in get_name_two: " + save_two)
    //   },
    // },  

    }}
   // reset everything:
    // created () {
    //   this.$vuetify.rtl = true
    //   this.$i18n.locale = 'ar'
    // },
// Call router.go() or this.$router.go()
// That will refresh the page and your state will be reset to how it was when the user first loaded the app.
</script>
<style src="@/assets/styles/mystyle.css">
</style>
