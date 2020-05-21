<template>
  <div
    id="firstdiv"
    shaped
    class="displaynms font-weight-light"
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
        Initial Token Supply: &nbsp; 100,000,000<br>
      </li>
      <li>
        Inflation begins in how many intervals? &nbsp; 24 = 2 yrs
        <br>
      </li>
      <li>
        Inflation tokens per 12 intervals? &nbsp;5,000,000 /12 (416,666.66) <br>
      </li>
      <li>
        Inflation is turned off at: &emsp;&emsp; 210,000,000<br>
      </li>
      <li>
        De-inflation ratio: &emsp;&emsp; 0.004 ( 0.01 = 1% )  <br><br>
      </li>
    </ul>
    <v-chip
      color="info"
      medium
      raised
    >
      Inflation and de-inflation begin at the same time
    </v-chip>
  </div>
</template>

<script>

  export default {
    name: 'TopWords',
    data: () => ({
      titlewords: 'DEFAULT / PRESET VALUES',
    })
  }
</script>
