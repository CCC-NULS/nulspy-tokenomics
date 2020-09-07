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
        cols="1"
      />
      <v-col 
        cols="12"
        md="10"
      >
        <v-card
          id="blackcard"
          v-bind="blackcard"
        >
          <span 
            :style="`font-family:Montserrat,sans-serif;font-size:52px;color:white;`"
          >
            All About Tokenomics
          </span>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="1"
      />
      <v-col 
        cols="12"
        md="10"
      >
        <v-card
          id="vcard2"
          v-bind="tokencardback"
          :class="bigline"
        >
          <v-card
            id="tealcard"
            vcard2
            dark
            color="teal lighten-2"
            width="70%"
            class="d-flex align-self-center align-center text-center pl-10 py-5 pr-12 mx-10"
          >
            {{ tsubtitle }}
          </v-card>

          <Childc 
            v-for="(stuf, i) in biglist"
            :key="i"
            slot
            v-bind="$attrs"
            name="Childc"
            :lead="stuf.lead"             
            :parag="stuf.parag"             
          />
        </v-card>
      </v-col>
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

  const blackcard = {
    color: "grey darken-3",
    elevation: 24,
    dark: true,
    raised: true,
    width: "90%",
    height: "92px",
    class: "d-flex align-center justify-center align-content-center",
  }

  var bigline1 = "d-flex flex-column align-center justify-center grey--text text-darken-3 "
  var bigline2 = " px-9 pb-12 mb-12 ml-9 mr-12 display-2 "
  var bigline = bigline1 + bigline2

  const tokencardback = {
    color: "bluegreylight5",
    width: "90%",
    dark: true,
    elevation: 24,
  }

  export default {
    name: 'Tokenomics',
    components: { 
      Childc,
    },
    data () {
      return {  
        bigline,
        tokencardback,
        blackcard,
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
  .bigsz {
    font-size:24px !important;
  }
</style>
