<template>
  <v-container
    id="tokenomics"
    fluid
    tag="section"
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="12"
        md="9"
      >
        <v-card
          color="black"
          elevation-24
          raised
        >
          Black card
          <!-- <template v-slot:heading>
            <div 
              class="display-5 font-weight-light" 
              :style="`font-family:Montserrat,sans-serif;`"
            >
              NULS Blockchain
            </div>

            <div 
              class="display-4 font-weight-light"
            >
              All About Tokenomics 
            </div>
          </template> -->

          <v-card
            id="vcard2"
            color="green"
          >
            <v-row
              align="center"
              justify="center"
            >
              helllo
              <!-- <childc /> -->
              
              <!-- <div class="transparent">
                {{ tsubtitle }}<br><br>

                <template 
                  v-for="b in bigstruct"
                >

                  <span 
                    v-slot
                    :key="b.lead"
                    name="slotbod"
                    :style="b.sty"
                    :class="b.clss"              
                  >
                    {{ b.thewords }} <br>
                  </span>
                </template>
              </div> -->
            </v-row>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import colors from 'vuetify/lib/util/colors'
  // import childc from './childc'

  // const tHeader = 'About NULS'
  const mat1 = 'NULS: Open-Source, Enterprise-Grade - Adaptive'
  
  var mat2 = 'NULS - A Fast-track business solution for developers offering a ' +
    'new industry standard in streamlining blockchain adoption.';
  
  const tsubtitle = 'Featuring microservices, smart contracts, cross-chain interoperability, and ' +
    'chain-building, NULS sets a new industry standard in streamlining blockchain adoption.' ;
  
  const bigstruct = [
      {
      id: tsl1,
      lead: 'Total Supply',
      parag: 'is the initial total token supply that will be created for the new blockchain. ' +
        'There are many variables to consider when selecting an initial total token supply including valuation, ' +
        'funding strategy, consensus node rewards, application use case(s), number/size of transactions, number of users, ' +
        'use case road map and community incentive programs.',
    },
      {
      id: tsl2,
      lead: 'Decimal',
      parag: '8 is the maximum needed. 8 decimal places are used by large public blockchain projects such as ' +
        'Bitcoin and Ethereum.',
    },
      {
      id: tsl3,
      lead: 'Inflation',
      parag: 'is the number and rate of new tokens that will be created and primarily used as rewards ' +
      'to incentivize the blockchain network to create, pack and validate blocks.',
      },
    {
      id: tsl4,
      lead: 'Initial Inflation',
      parag: 'is the fixed number of new tokens that will be generated to incentivize the blockchain ' +
      'network.',
      },
    {
      id: tsl5,
      lead: 'Total Inflation',
      parag: 'is the Total Supply plus the Initial Amount of Inflation.' + 
        'The maximum supply of tokens for the blockchain. It cannot be changed ' +
        'in the future unless blockchain is hard-forked. The establishment of a maximum supply triggers ' +
        'the need for a disinflation rate in order to reach the maximum supply. Most blockchains opt for a maximum supply ' +
        'or a deflationary token because it creates token scarcity which may lead to an increased token value over time. ' +
        'Once a maximum supply is reached, the network will become reliant on transaction fees to incentivize its continued ' +
        'operation.',
      },
    {
      id: tsl6,
      lead: 'Inflation Starting Time',
      parag: 'is the calendar date the inflation begins.',
      },
    {
      id: tsl7,
      lead: 'Disinflation Ratio',
      parag: 'is the rate at which the creation of new tokens (inflation) will be decreased at a ' +
      'set point and interval of time. (example: 0.4 %).',
      },
    {
      id: tsl8,
      lead: 'Interval',
      parag: '(in days): The frequency in which disinflation is enforced to decrease the creation of new tokens over time.' + 
        '(example 30 days).',
    },
  ]
  

  const ctwoprops = {
    color: "grey lighten-5",
    // align: "left",
    // class: "black--text pr-9 pl-9 ml-9 mr-9 rounded-tl-xl",
    // shaped: true,
    // elevation: 24,
    // raised,
    // style: "font-size:16px"
    }

  const fontpeach = "deep-orange lighten-4"

  const tchipprops = {
    color: 'grey lighten-4',
    textColor: 'black',
    shaped: true,
    raised: true,
    filled: true,
    label: true,
    'elevation-24': true,
    class: 'label montser mb-3 pr-1', 
    style: "line-height:18px; box-shadow: 0px 2px 2px -1px grey",
  }

  export default {
    name: 'Tokenomics',
    components: { 
      // childc,
    },
    data () {
      return {  
        showme: false,
        fontpeach,
        tsubtitle,
        leader2,
        bigstruct,
        tchipprops   
        }
      },
  };
</script>
<style>

  .montser {
    font-family: 'Montserrat', sans-serif !important;
  }
  /* 
  .v-chip{
      padding-right:2px;padding-left:2px;padding-bottom:2px;padding-top:2px;
  }
  .v-chip__content {
    font-size: 14px!important;
    color: deep-purple--text;
    padding-left: 5px;
    padding-right: 2px;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif !important;
  }

  .theme--light.v-chip {
    color: purple;
  } */
</style>
