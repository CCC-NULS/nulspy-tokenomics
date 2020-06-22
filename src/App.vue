<template>
  <router-view />
</template>

<script>
  import store from './store'

  let d = Date.now().toString()
  var adate = d.substring(7,13)

  store.dispatch('gSessionStrAct', adate)
  
  export default {
    name: 'App',
  }
</script>
