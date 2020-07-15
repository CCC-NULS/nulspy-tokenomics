<template>
  <div>
    <br>
  </div>
</template>

<script>

  var cars = new Array("Saab", "Volvo", "BMW");
  const initsupply = '["100,000,000", "150,000,000", "175,000,000", "200,000,000", "225,000,000", "260,000,000", "300,000,000"]'

  const CreateList = {
    initsupply2: ["100,000,000", "150,000,000", "175,000,000", "200,000,000", "225,000,000", "260,000,000", "300,000,000"],
    aninflation: ["2,000,000", "3,000,000", "4,000,000", "5,000,000", "6,000,000"],
    inflatervals:["0", "1", "2", "3", "4", "6", "12", "18", "24", "36", "48"],
    stopinflation: ["50,000,000", "100,000,000", "150,000,000", "200,000,000", "250,000,000",  "310,000,000", "350,000,000", "450,000,000", "510,000,000"],
    disinflation: ["0", "0.1%", "0.2%", "0.3%", "0.4%", "0.5%", "0.6%", "0.7%"],
  }

  const insupp = CreateList.initsupply
  console.log("insupp: " + insupp)

export default {
  name: 'CreateCs',
  data: () => ({
    cars,
    initsupply,
  })
}
</script>
