<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1>Пользователи</h1>
      </v-col>
      <v-col v-for="user in users" :key="user.id" cols="4">
        {{ user.username }}
      </v-col>
      <v-col cols="12">
        {{ userInfo }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    middleware: 'auth',
    data() {
      return {
        users: [],
        userInfo: null
      }
    },
    created() {
      this.$axios.get('auth/user/list/').then((response) => {
        this.users = response.data
      })
    }
  }
</script>

<style></style>
