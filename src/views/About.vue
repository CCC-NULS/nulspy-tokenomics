<template>
  <div class="about">
    <v-container
      id="about"
      fluid
      tag="section"
    >
      <base-v-component
        heading="About"
        link="about"
      /> 
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
          </base-material-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
