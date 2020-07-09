<template>
  <v-container
    id="tokenomics"
    fluid
    tag="section"
  >
    <!-- <base-v-component
      heading="About Tokenomics"
      link="pages/tokenomics"
    /> -->

    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="12"
        md="9"
      >
        <base-material-card
          color="blue-grey"
          elevation-24
          raised
        >
          <template v-slot:heading>
            <div class="display-5 font-weight-heavy">
              NULS Blockchain
            </div>

            <div class="display-4 font-weight-heavy">
              All About Tokenomics
            </div>
          </template>


          <v-card
            id="vcard2"
            align="left"
            class="pr-9 pl-9 ml-9 mr-9"
            elevation-24
            raised
          >
            <v-row
              align="left"
            >
              <v-col
                cols="1"
                md="1"
                align="left"
              />
              <v-col 
                cols="9"
                align="left"
              />
              <br>
      
              <v-card
                center
                flat
              >
                <v-card-title
                  class="display-2"
                >
                  {{ mat1 }}<br>
                </v-card-title>
              </v-card>
              <v-chip
                color="error"
                dark
                x-large
                label
                style="justify=center"
              >
                &nbsp;
                {{ mat2 }}
                 &nbsp;
                 &nbsp;
              </v-chip>
              <br>
              <div
                class="display-2"
              >
                {{ mat3 }}<br><br>

                {{ leader1 }}<br><br>

                <v-chip
                  v-bind="tchipprops"
                >
                  {{ lead2 }}<br>
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
                
                {{ leader5 }}<br><br>
                {{ leader6 }}<br><br>
                 
                {{ leader7 }}<br><br>
                {{ leader8 }}<br><br>
                 
                {{ leader9 }}
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
  const mat1 = 'NULS is an open-source, enterprise-grade, adaptive blockchain platform ' +
    'that offers fast-track business solutions for developers.'
  const mat2 = 'NULS sets a new industry standard in streamlining blockchain adoption'
  const leader1 = 'Featuring microservices, smart contracts, cross-chain interoperability, and instant ' +
    'chain-building, NULS sets a new industry standard in streamlining blockchain adoption.' 
  const lead2 = 'Total Supply'
  const leader2 = 'is the initial total token supply that will be created for the new blockchain. ' +
    'There are many variables to consider when selecting an initial total token supply including; valuation, ' +
    'funding strategy, consensus node rewards, application use case (s), number/size of transactions, number of users, ' +
    'use case road map and community incentive programs. (Example: 100,000,000)'
  const lead3 = 'Decimal'
  const leader3 = '8 is the maximum needed. 8 decimal places are used by large public blockchain projects such as ' +
   'Bitcoin and Ethereum.'
  const lead4 = 'Inflation'

  const leader4 = 'is the number and rate of new tokens that will be created and primarily used as rewards ' +
    'to incentivize the blockchain network to create, pack and validate blocks.'

  const leader5 = 'Initial Inflation: The fixed number of new tokens that will be generated to incentivize the blockchain ' +
    'network. (Example 110000000)'

  const leader6 = 'Total Inflation: Is the Total Supply plus the Initial Amount of Inflation.' + 
    'This will be the maximum supply of tokens for the blockchain. The maximum supply can not be changed ' +
    'in the future unless the code of blockchain is hard forked. The establishment of a maximum supply triggers ' +
    'the need for a deflation rate in order to reach the maximum supply. Most blockchains opt for a maximum supply ' +
    'or a deflationary token because it creates token scarcity which may lead to an increased token value over time. ' +
    'Once a maximum supply is reached, the network will become reliant on transaction fees to incentivize its continued ' +
    'operations. (Example 210000000)'

  const leader7 = 'Inflation Starting Time: The calendar date the inflation commences.'

  const leader8 = 'Deflation Ratio: Is the rate at which the creation of new tokens (inflation) will be decreased at a ' +
    'set interval of time. (example; 0.4 % Deflation Ration).'

  const leader9 = 'Interval (in days): The frequency which the deflation ratio is enforced to decrease the creation of new tokens over time. (example 30 days)'
  
  const tchipprops = {
    color: "blue-grey",
    raised: true,
    large: true,
    label: true,
    dark: true,
    raised: true,
    'elevation-24': true,
    style: "justify=center align=center"
  }

  export default {
    name: 'Tokenomics',
    data () {
      return {  
        mat1,
        mat2,
        leader1,
        leader2,
        lead2,
        leader3,
        lead3,
        leader4,
        lead4,
        leader5,
        leader6,
        leader7,
        leader8,       
        leader9,
        tchipprops   
        }
      }
    }
</script>

<style lang="scss">
  .tim-note {
    bottom: 10px;
    color: #c0c1c2;
    display: block;
    font-weight: 400;
    font-size: 13px;
    line-height: 13px;
    left: 0;
    margin-left: 20px;
    width: 260px;
  }
</style>
