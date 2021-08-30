<template>
  <div class="login">
    <div class="v-container">
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                v-model.trim="username"
                label="username"
                type="text"
              ></v-text-field>
              <v-text-field
                v-model.trim="password"
                label="Password"
                type="password"
                @keyup.enter="handleSubmit()"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="handleSubmit()">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </div>
  </div>
</template>

<script>
  // import jwtDecode from 'jwt-decode'
  // import Cookies from 'js-cookie'

  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },

    methods: {
      handleSubmit() {
        const username = this.username
        const password = this.password
        // this.$store.dispatch('auth/login', { username, password })
        this.$axios.post(
          'base/login/',
          { username, password },
          { withCredentials: true }
        )
      }
    }
  }
</script>

<style></style>
