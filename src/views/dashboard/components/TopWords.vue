<template>
  <div
    id="firstdiv"
    shaped
    class="displaynmstwo font-weight-light"
  >
    <v-chip
      medium
      dark
      color="tertiary"
    >
      {{ titlewords }}
    </v-chip>
    <br>
    <ul>
      <li>
        One Interval = 30 days<br>
      </li>
      <li>
        Initial Supply: &nbsp; 100,000,000<br>
      </li>
      <li>
        Inflation begins in X months? &nbsp; 12 mos = 1 yr
        <br>
      </li>
      <li>
        Inflation per year: &nbsp; <br>
      </li>
      <li>
        Inflation stops at: &emsp;&emsp; 210,000,000<br>
      </li>
      <li>
        Disinflation ratio: &emsp;&emsp;(  0% to 0.7% )  <br><br>
      </li>
    </ul>
    <v-chip
      color="info"
      medium
      raised
    >
      <span class="vchipontent">
        Inflation and de-inflation begin at the same time
      </span>
    </v-chip>
  </div>
</template>

<script>

  export default {
    name: 'TopWords',
    data: () => ({
      titlewords: 'Note on Values',
    })
  };
</script>

<style scoped>
.vchipontent {
    font-size: 12px!important;
}
</style>
