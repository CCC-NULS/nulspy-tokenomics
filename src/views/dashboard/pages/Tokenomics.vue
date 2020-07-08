<template>
  <v-container
    id="tokenomics"
    fluid
    tag="section"
  >
    <base-v-component
      heading="About Tokenomics"
      link="pages/tokenomics"
    />

    <v-row
      align="center"
      justify="center"
    >
      <v-col cols="12">
        <base-material-card
          color="green"
        >
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              NULS Tokenomics Calculator
            </div>

            <div class="subtitle-1 font-weight-light">
              All About NULS
            </div>
          </template>

          <v-card-text>
            <v-container
              class="pa-0"
              fluid
            >
              <v-row
                v-for="(t, i) in typography"
                :key="i"
                align="center"
              >
                <v-col
                  cols="1"
                  md="3"
                >
                  <span
                    class="tim-note"
                    v-text="t[0]"
                  />
                </v-col>

                <v-col cols="6">
                  <component
                    :is="t[2]"
                    :class="i"
                  >
                    <template v-if="i !== 'quote'">
                      {{ t[1] }}
                    </template>
                    <p v-if="i === 'quote'">
                      {{ t[1] }}
                    </p>
                    <small v-if="i === 'quote'">Satoshi</small>

                    <template v-if="i === 'small'">
                      <br>
                      <small>Buy blockchain</small>
                    </template>
                  </component>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  const leaderShort = leader.slice(0, 105) + '...'
  const material = 'NULS is an open-source, enterprise-grade, adaptive blockchain platform'
  const mat2 = ' that offers fast-track business solutions for developers.'
  const small = 'NULS sets a new industry standard in streamlining blockchain adoption'
  const tHeader = 'About NULS'
  const leader = 'Featuring microservices, smart contracts, cross-chain interoperability, ' +
    'and instant chain-building, ' +
    'NULS sets a new industry standard in streamlining blockchain adoption.'
  const moreText = ' '

  const leader2 = 'Total Supply: This is the initial total token supply that will be created for the new blockchain. There are many variables to consider when selecting an initial total token supply including; valuation, funding strategy, consensus node rewards, application use case (s), number/size of transactions, number of users, use case road map and community incentive programs. (Example “100000000”)'

  const leader3 = 'Decimal: “8” is the maximum needed. 8 decimal places are used by large public blockchain projects such as Bitcoin and Ethereum.'

  const leader4 = 'Inflation: Is the number and rate of new tokens that will be created and primarily used as rewards to incentivize the blockchain network to create, pack and validate blocks.'

  const leader5 = 'Initial Inflation: The fixed number of new tokens that will be generated to incentivize the blockchain network. (Example “110000000”)'

  const leader6 = 'Total Inflation: Is the Total Supply plus the Initial Amount of Inflation. This will be the maximum supply of tokens for the blockchain. The maximum supply can not be changed in the future unless the code of blockchain is   “hard forked”. The establishment of a maximum supply triggers the need for a deflation rate in order to reach the maximum supply. Most blockchains opt for a maximum supply or a deflationary token because it creates token scarcity which may lead to an increased token value over time. Once a maximum supply is reached, the network will become reliant on transaction fees to incentivize its continued operations. (Example “210000000”)'

  const leader7 = 'Inflation Starting Time: The calendar date the inflation commences.'

  const leader8 = 'Deflation Ratio: Is the rate at which the creation of new tokens (inflation) will be decreased at a set interval of time. (example; “0.4” % Deflation Ration).'

  const leader9 = 'Interval (in days): The frequency which the deflation ratio is enforced to decrease the creation of new tokens over time. (example “30” days)'


  export default {
    name: 'Tokenomics',
    data () {
      return {   
        typography: {
          'display-4': [' ', tHeader, 'h1'],
          'display-3': [' ', material + mat2, 'h2'],
          'display-2': [' ', material, 'h3'],
          'display-1': [' ', material, 'h4'],
          headline: [' ', moreText, 'h5'],
          'title text-uppercase': [' ', material, 'h6'],
          '': [' ', leader, 'p'],
          blockquote: [' ', leader, leader2, leader3, leader4, leader5, leader6, leader7, leader8, 'blockquote'],
          'text--disabled': [' ', leaderShort, 'p'],
          'primary--text': [' ', leaderShort, 'p'],
          'info--text': [' ', leaderShort, 'p'],
          'success--text': [' ', leaderShort, 'p'],
          'warning--text': [' ', leaderShort, 'p'],
          'danger--text': [' ', leaderShort, 'p'],
          small: [' ', small, 'h2'],
        }
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
