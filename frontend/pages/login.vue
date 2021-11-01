<template>
  <div class="login">
    <v-container class="login-container">
      <v-row>
        <v-flex xs12 sm6 lg4 offset-lg-4 offset-sm-3>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary"> </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  v-model.trim="username"
                  label="Логин"
                  type="text"
                  :error-messages="usernameErrors"
                  @input="$v.username.$touch()"
                  @blur="$v.username.$touch()"
                  @keyup.enter="handleSubmit()"
                ></v-text-field>
                <v-text-field
                  v-model.trim="password"
                  label="Пароль"
                  type="password"
                  :error-messages="passwordErrors"
                  @input="$v.password.$touch()"
                  @blur="$v.password.$touch()"
                  @keyup.enter="handleSubmit()"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn
                class="mr-3"
                color="primary"
                :loading="loading"
                @click="handleSubmit()"
                >Отправить</v-btn
              >
              <NuxtLink to="/registration">Регистрация</NuxtLink>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  import { required } from 'vuelidate/lib/validators'
  import { Toast } from '../plugins/swal'

  export default {
    layout: 'zero',
    middleware: 'login',
    validations: {
      username: { required },
      password: { required }
    },
    data() {
      return {
        username: '',
        password: '',
        loading: false
      }
    },
    computed: {
      usernameErrors() {
        const errors = []
        if (!this.$v.username.$dirty) return errors
        !this.$v.username.required && errors.push('Это обязательное поле')
        return errors
      },
      passwordErrors() {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Это обязательное поле')
        return errors
      }
    },
    methods: {
      handleSubmit() {
        this.loading = true
        const username = this.username
        const password = this.password

        if (this.$v.$invalid) {
          this.$v.$touch()
          this.loading = false
          return
        }

        this.$store
          .dispatch('auth/login', { username, password })
          .then(() => {
            this.loading = false
            this.$router.push('/')
          })
          .catch(() => {
            this.loading = false
            return Toast.fire({
              title: 'Неверный логин или пароль',
              icon: 'error',
              timer: 3000
            })
          })
      }
    }
  }
</script>
