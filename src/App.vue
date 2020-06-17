<template>
  <router-view />
</template>

<script>
  import store from './store'
  let d = Date.now().toString()
  var sdate = d.substring(7,13)

  store.dispatch('gSessionStrAct', sdate)


  export default {
    name: 'App',
  }
</script>
