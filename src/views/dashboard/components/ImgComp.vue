import Vue from 'vue'

<template>
  <div>{{ link }} </div>
</template>
 
<script>

  export default {
    name: "ImgComp",
    props: {
      url: {
        type: String, 
        required: true 
        }
      },
    data: () =>  ({
      link: 'loading'  
    }),
    created() {
      this.getLink();
    },
    methods: {
      getLink() {
        setTimeout(() => {
          this.link = 'response url for link: ' + this.url
        }, 1000)
      }
    },
  }

 
</script>
  
  