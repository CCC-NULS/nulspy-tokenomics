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
        md="11"
      >
        <v-card
          color="grey darken-3"
          elevation-24
          raised
          width="100%"
          height="92px"
          class="d-flex align-center justify-center"
        >
          <span 
            :style="`font-family:Montserrat,sans-serif;font-size:52px;color:white;`"
          >
            All About Tokenomics
          </span>
        </v-card>

        <div 
          class="display-2 font-weight-light"
        >
          {{ mat1 }} 
        </div>
        <div 
          class="display-2 font-weight-light"
        >
          {{ mat2 }} 
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-card
        id="vcard2"
        color="blue-grey lighten-5"
        align="center"
        class="grey--text text-darken-3 pr-9 pl-9 py-t pb-12 mb-12 ml-9 mr-12"
        elevation-24
        :style="`font-size:24px;`"
      >
        <v-card
          vcard2
          color="teal lighten-5"
          width="70%"
          class="d-flex align-self-center text-center pl-10 pr-24 mx-10"
        >
          {{ tsubtitle }}
        </v-card>

        <Childc 
          v-for="(stuf, i) in biglist"
          slot
          :key="i"
          name="Childc"
          :lead="stuf.lead"             
          :parag="stuf.parag"             
        />
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
  import colors from 'vuetify/lib/util/colors'
  import Childc from './childc'

  // const tHeader = 'About NULS'
  const mat1 = 'NULS: Open-Source, Enterprise-Grade - Adaptive'
  
  var mat2 = 'NULS - A Fast-track business solution for developers offering a ' +
    'new industry standard in streamlining blockchain adoption.';
  
  const tsubtitle = 'When designing a blockchain - you may want to experiment with the ' +
    'economics of it over time. Below is a short dictionary of the choices.'
  
  const biglist = [
      {
      lead: 'Total Supply',
      parag: 'is the initial total token supply that will be created for the new blockchain. ' +
        'There are many variables to consider when selecting an initial total token supply including valuation, ' +
        'funding strategy, consensus node rewards, application use case(s), number/size of transactions, number of users, ' +
        'use case road map and community incentive programs.',
    },
      {
      lead: 'Decimal',
      parag: '8 is the maximum needed. 8 decimal places are used by large public blockchain projects such as ' +
        'Bitcoin and Ethereum.',
    },
      {
      lead: 'Inflation',
      parag: 'is the number and rate of new tokens that will be created and primarily used as rewards ' +
      'to incentivize the blockchain network to create, pack and validate blocks.',
      },
    {
      lead: 'Initial Inflation',
      parag: 'is the fixed number of new tokens that will be generated to incentivize the blockchain ' +
      'network.',
      },
    {
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
      lead: 'Inflation Starting Time',
      parag: 'is the calendar date the inflation begins.',
      },
    {
      lead: 'Disinflation Ratio',
      parag: 'is the rate at which the creation of new tokens (inflation) will be decreased at a ' +
      'set point and interval of time. (example: 0.4 %).',
      },
    {
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
      Childc,
    },
    data () {
      return {  
        tsubtitle,
        biglist,
        }
      },
  };
</script>
<style>
  .montser {
    font-family: 'Montserrat', sans-serif !important;
  }

</style>
