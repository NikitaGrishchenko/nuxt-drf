<template>
  <div class="registration">
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Регистрация</h1>
          <hr />
        </v-col>
        <v-col cols="12">
          <v-form>
            <v-text-field
              v-model.trim="firstName"
              label="Имя"
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="lastName"
              label="Фамилия"
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="email"
              label="E-mail"
              type="email"
            ></v-text-field>
            <v-text-field
              v-model.trim="password"
              label="Пароль"
              type="password"
            ></v-text-field>
            <v-text-field
              v-model.trim="passwordConfirmation"
              label="Подтверждение пароля"
              type="password"
            ></v-text-field>
            <v-btn
              class="mr-3"
              color="primary"
              :loading="loading"
              @click="handleSubmit()"
              >Отправить</v-btn
            >
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  export default {
    layout: 'zero',
    data() {
      return {
        lastName: '',
        firstName: '',
        email: '',
        password: '',
        passwordConfirmation: '',
        loading: false
      }
    },
    methods: {
      handleSubmit() {
        // this.loading = true
        // const username = this.username
        // const password = this.password

        // if (this.$v.$invalid) {
        //   this.$v.$touch()
        //   this.loading = false
        //   return
        // }

        const data = {
          last_name: this.lastName,
          first_name: this.firstName,
          email: this.email,
          password: this.password,
          password_confirmation: this.passwordConfirmation
        }

        this.$axios
          .post('auth/user/create/', data)
          .then((response) => {
            print(this.user)
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
  }
</script>
