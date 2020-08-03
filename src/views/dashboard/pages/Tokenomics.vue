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
        <base-material-cardn
          color="black"
          elevation-24
          raised
        >
          <template v-slot:heading>
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
          </template>


          <!-- <template v-slot:after-heading>
            <div 
              class="display-4 font-weight-heavy"
            >              
              All About test 
            </div>
          </template> -->

          <!-- img="`linear-gradient(306deg, rgb(251, 233, 231) 0%, #4DB6AC 100%)!important;`" -->


          <v-card
            id="vcard2"
            color="deep-orange lighten-5"
            dark
            align="left"
            class="black--text pr-9 pl-9 ml-9 mr-9 rounded-tl-xl"
            shaped
            elevation-24
            raised
            filled="true"
            :style="`font-size:16px;background-image: linear-gradient(306deg, #E0F2F1 0%, #fbe9e7 100%)!important;`"
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
                class="transparent"
                :class="fontcol"
              >
                {{ leader1 }}<br><br>
                <v-chip
                  v-bind="tchipprops"
                  elevation-19
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
                  {{ lead9 }} &nbsp;&nbsp;
                </v-chip>
                {{ leader9 }} <br><br>
              </div>
            </v-row>
          </v-card>
        </base-material-cardn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import colors from 'vuetify/lib/util/colors'

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
  const leader9 = '(in days): The frequency in which disinflation is enforced to decrease the creation of new tokens over time. (example 30 days).';
  
  const fontpeach = "deep-orange lighten-4"

  const tchipprops = {
    color: 'grey lighten-4',
    textColor: 'black',
    shaped: true,
    raised: true,
    filled: true,
    medium: true,
    label: true,
    'elevation-24': true,
    class: 'montser mb-0', 
    style: "line-height:18px; box-shadow: 0px 2px 2px -1px grey"

  };

  export default {
    name: 'Tokenomics',

    data () {
      return {  
        fontpeach,
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
      },
    mounted () {
      this.$store.dispatch("gShowMeAct", false)
    },
  };
</script>
<style>

.montser {
  font-family: 'Montserrat', sans-serif !important;
}
.ortext {
  font-family: 'Montserrat', sans-serif !important;
  
}
.v-chip{
    padding-right:2px;padding-left:2px;padding-bottom:2px;padding-top:2px;

}
.v-chip__content {
    font-size: 14px!important;
    color: deep-purple--text;
  
    padding-right:2px;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif !important;

}
.theme--light.v-chip {
  color: purple;
}
 .unusedstyle {
  font-family: 'Montserrat', sans-serif;
  font-size: 42!important;
  font-weight: 700;
  color:white;
  text-shadow: 3px 4px 4px #000000;
  text-shadow: 1px 1px 1px #7F7F7F;

} 
</style>