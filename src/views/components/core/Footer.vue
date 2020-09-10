<template>
  <v-footer
    id="core-footer"
    absolute
    color="teal lighten-4"
  >
    <v-container>
      <v-row
        align="center"
        no-gutters
      >
        <v-col
          v-for="(link, i) in links"
          :key="i"
          class="text-center mb-sm-0 mb-4"
          cols="auto"
        >
          <a
            :href="link.href"
            class="mr-0 grey--text text--darken-3"
            rel="noopener"
            target="_blank"
            v-text="link.text"
          />
        </v-col>

        <v-spacer class="hidden-sm-and-down" />

        <v-col
          cols="12"
          md="auto"
        >
          <div class="body-1 font-weight-medium pt-1 pt-md-0 mt-1 text-center">
            &copy; 2020 Made with
            <v-icon
              size="18"
              color="red darken-1"
            >
              mdi-heart
            </v-icon>
            by <a href="https://nuls.io">NULS</a> for a better blockchain
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
  export default {
    name: 'CoreFooter',

    data: () => ({
      links: [
        {
          href: 'https://nuls.io',
          text: 'NULS',
        },

        {
          href: 'https://bbs.nuls.io/',
          text: 'Community',
        },
        {
          href: 'https://gov.nuls.io/',
          text: 'Community Governance',
        },

        {
          href: 'https://nuls.io',
          text: 'Contact Us',
        },
      ],
    }),
  }
</script>

<style lang="sass">
  #core-footer
    a
      font-size: .825rem
      font-weight: 600
      text-decoration: none
      text-transform: uppercase
</style>
