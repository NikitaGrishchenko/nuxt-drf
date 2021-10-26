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
              v-model.trim="user.lastName"
              label="Имя"
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="user.firstName"
              label="Фамилия"
              type="text"
            ></v-text-field>
            <v-text-field
              v-model.trim="user.email"
              label="E-mail"
              type="email"
            ></v-text-field>
            <v-text-field
              v-model.trim="user.password"
              label="Пароль"
              type="password"
            ></v-text-field>
            <v-text-field
              v-model.trim="user.passwordConfirmation"
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
        user: {
          lastName: '',
          firstName: '',
          email: '',
          password: '',
          passwordConfirmation: ''
        },
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

        this.$axios
          .post('auth/user/create/', this.user)
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
