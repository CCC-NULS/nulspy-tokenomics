<template>
  <div
    id="firstdiv"
    shaped
    class="displaynmstwo font-weight-light"
  >
    <v-chip
      color="transparent"
      large
      class="mb-1"
    >
      <span 
        class="vchip2 orange--text text--lighten-5"
      > 
        {{ titlewords }}  </span>
    </v-chip>
    
    <ul>
      <li>
        Initial Supply: &nbsp; 100,000,000   	&#8195;	&#8195;	&#8195;   Max Supply: &emsp;&emsp; 210,000,000<br>
      </li>
      <li>
        Inflation begins in 24 intervals
        <br>
      </li>
      <li>
        Annual Inflation: &nbsp; 5,000,000   &#8195;	&#8195;	&#8195; &#8195;	&#8195;	&#8195; &#8195;	&#8195;	&#8195;   Disinflation ratio: 0.4% &emsp;&emsp;(  0 to .9% )  <br><br>
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
  /* .vchipontent {
      font-size: 12px!important; 
      font-style: italic;
  } */
  .vchip2 {
      font-size: 22px!important;
      text-shadow: 2 2 2 #FFFFFF;
      font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
      font-weight: 700;
      
  }
</style>
