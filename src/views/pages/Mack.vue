<template>
  <a
    :href="url"
    class="display-1"
  >
    <slot />
  </a>
</template>

<script>

  const toplines = [
    {
      id: "item1",
      thewords: "TokenLife Design Tool",
      sty: "`font-family: 'montserrat', sans-serif;font-size:52px; font-weight:900;`",
      clss: "grey--text darken2",
    },
    {
      id: "item2",
      thewords: "Input different numbers and see tokens grow over time",
      sty: "font-family:'montserrat',sans-serif; font-size:24px;  color:#424242; line-height:32px;`",
      clss: "grey--text darken3",
    },
    {
      id: "item3",
      thewords: "Disinflation begins one interval after Inflation starts",
      sty: "font-size:16px;font-family:'Roboto',sans-serif;color:#424242;line-height:92px;",
      clss: "grey--text darken3",
    },
  ]

  export default {
    name: "Mack",
    props: {
      url: {
        type: String,
        default: "abc.com"
      }
    },
    data: function () {
      return {
        toplines,
        mmessage: "hi from IMPORTED component Mack.",
      }
    },
  }
</script>
