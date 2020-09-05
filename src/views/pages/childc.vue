<template>
  <v-container>
    <template slot:header>
      Here might be a page title 
      {{ vmdInputBox }} 
    </template>
    <div class="header">
      <!-- We want header content here -->
      <slot 
        name="header"
      />
    </div>
  </v-container>
</template>

<script>
export default {
  name: childc,
}
</script>
