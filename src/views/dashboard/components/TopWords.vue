<template>
  <div
    id="firstdiv"
    shaped
    class="displaynmstwo font-weight-light"
  >
    <v-chip
      dark
      color="tertiary"
      large
      class="mb-1"
    >
      <span class="vchip2"> {{ titlewords }}  </span>
    </v-chip>
    
    <ul>
      <li>
        Initial Supply: &nbsp; 100,000,000<br>
      </li>
      <li>
        Max Supply: &emsp;&emsp; 210,000,000<br>
      </li>
      <li>
        Inflation begins in 24 intervals
        <br>
      </li>
      <li>
        Annual Inflation: &nbsp; 5,000,000 <br>
      </li>

      <li>
        Disinflation ratio: 0.4% &emsp;&emsp;(  0 to .9% )  <br><br>
      </li>
    </ul>
  </div>
</template>

<script>

  export default {
    name: 'TopWords',
    data: () => ({
      titlewords: 'some example values . . .',
    })
  };
</script>

<style>
  .vchipontent {
      font-size: 12px!important; 
      font-style: italic;
  }
  .vchip2 {
      font-size: 19px!important;
  }
</style>
