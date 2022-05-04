<template>
  <v-row justify="center" align="center">
    <v-col> Main page </v-col>
  </v-row>
</template>
<script>
  export default {
    middleware: 'auth'
    // meta: { requiresAuth: true }
  }
</script>
