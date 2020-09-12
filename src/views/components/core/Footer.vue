<template>
  <v-footer
    id="core-footer"
    absolute
    color="primary"
    height="auto"
    min-height="48px"
    max-height="100px"
    class="d-flex mt-2"
  >
    <v-container
      class="pa-0 ma-0"
    >
      <v-row
        align="center"
        no-gutters
      >
        <v-col
          v-for="(link, i) in links"
          :key="i"
          class="text-center mb-0 pb-0"
          cols="auto"
        >
          <a
            :href="link.href"
            class="mr-0 lighttext--text"
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
          <div class="body-1 font-weight-medium pt-0 mt-1 text-center lighttext--text">
            &copy; 2020 Made with
            <v-icon
              size="16"
              color="red darken-1"
            >
              mdi-heart
            </v-icon>
            by 
            <a 
              href="https://nuls.io" 
              style="font-weight:600!important;"
            >
              NULS
            </a> 
            for a better blockchain
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
      font-size: 14px
      font-weight: 600
      text-decoration: none
      text-transform: uppercase
</style>
