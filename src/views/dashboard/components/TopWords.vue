<template>
  <div
    id="firstdiv"
    shaped
    class="displaynmstwo"
  >
    <span> 
      {{ titlewords }} 
    </span>
    
    <ul>
      <li>
        Initial Supply: &nbsp; 100,000,000  	&#8195;	&#8195;   Max Supply: &emsp;&emsp; 210,000,000<br>
      </li>
      <li>
        Inflation begins in 24 intervals
        <br>
      </li>
      <li>
        Annual Inflation: &nbsp; 5,000,000    &nbsp; &nbsp; &nbsp;  Disinflation ratio: 0.4% &emsp;&emsp;(  0 to .9% )  <br><br>
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

</style>
