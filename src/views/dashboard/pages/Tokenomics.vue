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
        <base-material-card
          color="primary"
          elevation-24
          raised
        >
          <template v-slot:heading>
            <div class="display-5 font-weight-heavy">
              NULS Blockchain
            </div>

            <div 
              class="display-4 font-weight-heavy"
              :style="`text-shadow: 3px 3px 3px 2px 3px purple darken-1`"
            >
              All About Tokenomics
            </div>
          </template>


          <v-card
            id="vcard2"
            color="primary darken-2"
            align="left"
            class="pr-9 pl-9 ml-9 mr-9"
            elevation-24
            raised
            outlined
            :style="`{ text-shadow: 3px 3px 3px 2px 3px purple darken-1}`"
          >
            <v-col
              cols="1"
              md="1"
            />
            <v-col 
              cols="9"
            />

            <!--   | | |   -->
            
            <v-row
              align="center"
              justify="center"
            >
              <div
                class="display-2"
              >
                {{ leader1 }}<br><br>
                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead2 }} 
                </v-chip>
                {{ leader2 }}<br><br>

                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead3 }}<br>
                </v-chip>
                {{ leader3 }}<br><br>

                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead4 }}<br>
                </v-chip>                
                {{ leader4 }}<br><br>
                
                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead5 }}&nbsp;&nbsp;
                </v-chip>
                {{ leader5 }}<br><br>


                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead6 }}&nbsp;&nbsp;
                </v-chip>
                {{ leader6 }}<br><br>                
                 
                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead7 }}&nbsp;&nbsp;
                </v-chip>
                {{ leader7 }}<br><br>

                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead8 }}&nbsp;&nbsp;
                </v-chip>
                {{ leader8 }}<br><br>  


                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead9 }}&nbsp;&nbsp;
                </v-chip>
                {{ leader9 }}<br><br>
              </div>
            </v-row>
          </v-card>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  // const tHeader = 'About NULS'
  const mat1 = 'NULS: Open-Source, Enterprise-Grade - Adaptive'
  
  var mat2 = 'NULS - A Fast-track business solution for developers offering a ' +
    'new industry standard in streamlining blockchain adoption.';
  
  const leader1 = 'Featuring microservices, smart contracts, cross-chain interoperability, and ' +
    'chain-building, NULS sets a new industry standard in streamlining blockchain adoption.' ;
  
  const lead2 = 'Total Supply';
  const leader2 = 'is the initial total token supply that will be created for the new blockchain. ' +
    'There are many variables to consider when selecting an initial total token supply including valuation, ' +
    'funding strategy, consensus node rewards, application use case(s), number/size of transactions, number of users, ' +
    'use case road map and community incentive programs.';
  
  const lead3 = 'Decimal';
  const leader3 = '8 is the maximum needed. 8 decimal places are used by large public blockchain projects such as ' +
   'Bitcoin and Ethereum.';
  
  const lead4 = 'Inflation';
  const leader4 = 'is the number and rate of new tokens that will be created and primarily used as rewards ' +
    'to incentivize the blockchain network to create, pack and validate blocks.';

  const lead5 ='Initial Inflation';
  const leader5 = 'is the fixed number of new tokens that will be generated to incentivize the blockchain ' +
    'network.';

  const lead6 = 'Total Inflation'
  const leader6 = 'is the Total Supply plus the Initial Amount of Inflation.' + 
    'The maximum supply of tokens for the blockchain. It cannot be changed ' +
    'in the future unless blockchain is hard-forked. The establishment of a maximum supply triggers ' +
    'the need for a disinflation rate in order to reach the maximum supply. Most blockchains opt for a maximum supply ' +
    'or a deflationary token because it creates token scarcity which may lead to an increased token value over time. ' +
    'Once a maximum supply is reached, the network will become reliant on transaction fees to incentivize its continued ' +
    'operation.'

  const lead7 = 'Inflation Starting Time';
  const leader7 = 'is the calendar date the inflation begins.';

  const lead8 = 'Disinflation Ratio';
  const leader8 = 'is the rate at which the creation of new tokens (inflation) will be decreased at a ' +
    'set point and interval of time. (example: 0.4 %).';

  const lead9 = 'Interval';
  const leader9 = '(in days): The frequency in which disinflation is enforced to decrease the creation of new tokens over time. (example 30 days)';
  
  const tchipprops = {
    color: 'primary',
    raised: true,
    medium: true,
    label: true,
    dark: true,
    'elevation-24': true,
  };

  export default {
    name: 'Tokenomics',
    data () {
      return {  
        leader1,
        leader2,
        lead2,
        leader3,
        lead3,
        leader4,
        lead4,
        leader5,
        lead5,
        leader6,
        lead6,
        leader7,
        lead7,
        leader8,  
        lead8,
        leader9,
        lead9,
        tchipprops   
        }
      }
    };
</script>
<style>
  /* .v-chip__content {
    font-size: 16px;
  } */
</style>