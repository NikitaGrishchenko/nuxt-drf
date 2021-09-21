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
        <v-btn @click="refreshToken">Refresh Token</v-btn>
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
      this.$axios.get('base/users/').then((response) => {
        this.users = response.data
      })
    },
    methods: {
      refreshToken() {
        this.$axios.get('base/user/checking/').then((response) => {
          this.userInfo = response
        })
      }
    }
  }
</script>

<style></style>
