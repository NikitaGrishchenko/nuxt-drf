<template>
  <v-container>
    <v-row>
      <h1>Пользователь {{ id }}</h1>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    validate({ params }) {
      // Must be a number
      return /^\d+$/.test(params.id)
    },
    computed: {
      id() {
        return this.$route.params.id
      }
    }
  }
</script>

<style></style>
