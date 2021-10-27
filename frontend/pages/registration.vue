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
            <v-row>
              <v-col cols="4">
                <v-text-field
                  v-model.trim="firstName"
                  label="Имя"
                  type="text"
                  :error-messages="firstNameErrors"
                  @input="$v.firstName.$touch()"
                  @blur="$v.firstName.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model.trim="lastName"
                  label="Фамилия"
                  type="text"
                  :error-messages="lastNameErrors"
                  @input="$v.lastName.$touch()"
                  @blur="$v.lastName.$touch()"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4">
                <v-text-field
                  v-model.trim="email"
                  label="E-mail"
                  type="email"
                  :error-messages="emailErrors"
                  :loading="loadingCheckEmail"
                  @input="$v.email.$touch()"
                  @blur="$v.email.$touch()"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4">
                <v-text-field
                  v-model.trim="password"
                  label="Пароль"
                  :type="showPassword ? 'text' : 'password'"
                  :error-messages="passwordErrors"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="showPassword = !showPassword"
                  @input="$v.password.$touch()"
                  @blur="$v.password.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-text-field
                  v-model.trim="passwordConfirmation"
                  label="Подтверждение пароля"
                  type="password"
                  :error-messages="passwordConfirmationErrors"
                  @input="$v.passwordConfirmation.$touch()"
                  @blur="$v.passwordConfirmation.$touch()"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn
                  class="mr-3"
                  color="primary"
                  :loading="loading"
                  @click="submitForm()"
                  >Отправить</v-btn
                >
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'
  export default {
    layout: 'zero',
    validations: {
      firstName: { required },
      lastName: { required },
      email: { required, email },
      password: { required, minLength: minLength(8) },
      passwordConfirmation: { required, sameAsPassword: sameAs('password') }
    },
    data() {
      return {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        passwordConfirmation: '',
        loading: false,
        showPassword: false,
        loadingCheckEmail: false
      }
    },
    computed: {
      firstNameErrors() {
        const errors = []
        if (!this.$v.firstName.$dirty) return errors
        !this.$v.firstName.required && errors.push('Это обязательное поле')
        return errors
      },
      lastNameErrors() {
        const errors = []
        if (!this.$v.lastName.$dirty) return errors
        !this.$v.lastName.required && errors.push('Это обязательное поле')
        return errors
      },
      emailErrors() {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.required && errors.push('Это обязательное поле')
        !this.$v.email.email && errors.push('Некорректный E-mail')
        return errors
      },
      passwordErrors() {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Это обязательное поле')
        !this.$v.password.minLength &&
          errors.push('Пароль должен содержать минимум 8 символов')
        return errors
      },
      passwordConfirmationErrors() {
        const errors = []
        if (!this.$v.passwordConfirmation.$dirty) return errors
        !this.$v.passwordConfirmation.required &&
          errors.push('Это обязательное поле')
        !this.$v.passwordConfirmation.sameAsPassword &&
          errors.push('Пароли не совпадают')
        return errors
      }
    },
    watch: {
      email(val) {
        const email = val
        if (!this.$v.email.email || email === '') {
          return
        }
        this.loadingCheckEmail = true
        return new Promise((resolve, reject) => {
          this.$axios
            .post('auth/user/email-check/', { email }, { progress: false })
            .then((response) => {
              console.log(response)
              this.loadingCheckEmail = false
              resolve(response)
            })
            .catch((error) => {
              this.loadingCheckEmail = false
              reject(error)
            })
        })
      }
    },
    methods: {
      submitForm() {
        this.loading = true

        if (this.$v.$invalid) {
          this.$v.$touch()
          this.loading = false
          return
        }

        const data = {
          last_name: this.lastName,
          first_name: this.firstName,
          email: this.email,
          password: this.password,
          password_confirmation: this.passwordConfirmation
        }
        return new Promise((resolve, reject) => {
          this.$axios
            .post('auth/user/create/', data)
            .then((response) => {
              this.cleanInputData()
              this.loading = false
              console.log(response)
              resolve(response)
            })
            .catch((error) => {
              this.loading = false
              reject(error)
            })
        })
      },
      cleanInputData() {
        this.lastName = ''
        this.firstName = ''
        this.email = ''
        this.password = ''
        this.passwordConfirmation = ''
        this.showPassword = false
        this.$v.$reset()
      }
    }
  }
</script>
