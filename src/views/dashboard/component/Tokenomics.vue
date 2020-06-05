<template>
  <v-container
    id="tokenomics"
    fluid
    tag="section"
  >
    <base-v-component
      heading="About Tokenomics"
      link="styles/typography"
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
  const leader = 'Blockchain will be worth billions of dollars, ' +
    'because we understand culture.'
  const leaderShort = leader.slice(0, 105) + '...'
  // const material = 'The Life of Material Dashboard'
  const material = 'NULS is an open-source, enterprise-grade, adaptive blockchain platform'
  const mat2 = ' that offers fast-track business solutions for developers.'
  const small = 'NULS sets a new industry standard in streamlining blockchain adoption'
  const tHeader = 'About NULS'
  const moreText = 'Featuring microservices, smart contracts, cross-chain interoperability, ' +
    'and instant chain-building, ' +
    'NULS sets a new industry standard in streamlining blockchain adoption.'

  export default {
    name: 'Tokenomics',
    data: () => ({
      typography: {
        'display-4': [' ', tHeader, 'h1'],
        'display-3': [' ', material + mat2, 'h2'],
        'display-2': [' ', material, 'h3'],
        'display-1': [' ', material, 'h4'],
        headline: [' ', moreText, 'h5'],
        'title text-uppercase': [' ', material, 'h6'],
        '': [' ', leader, 'p'],
        blockquote: [' ', leader, 'blockquote'],
        'text--disabled': [' ', leaderShort, 'p'],
        'primary--text': [' ', leaderShort, 'p'],
        'info--text': [' ', leaderShort, 'p'],
        'success--text': [' ', leaderShort, 'p'],
        'warning--text': [' ', leaderShort, 'p'],
        'danger--text': [' ', leaderShort, 'p'],
        small: [' ', small, 'h2'],
      },
    }),
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
