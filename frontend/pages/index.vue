<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6"> Main page, hello </v-col>
  </v-row>
</template>
<script>
  export default {
    middleware: 'auth'
  }
</script>
