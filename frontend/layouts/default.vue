<template>
  <v-app dark>
    <v-navigation-drawer v-model="drawer" fixed app disable-resize-watcher>
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          link
          @click="drawer = false"
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="`Vuetify.js`" />
      <v-spacer />
      <v-toolbar-title v-if="user" class="mr-4">{{
        user.email
      }}</v-toolbar-title>
      <v-btn elevation="2" outlined @click="handleSubmit">Выйти</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        user: null,
        drawer: false,
        items: [
          {
            icon: 'mdi-apps',
            title: 'Welcome',
            to: '/'
          },
          {
            icon: 'mdi-chart-bubble',
            title: 'Inspire',
            to: '/inspire'
          },
          {
            icon: 'mdi-account',
            title: 'Users',
            to: '/users'
          },
          {
            icon: 'mdi-account',
            title: 'Login',
            to: '/login'
          }
        ]
      }
    },
    created() {
      this.getUser()
    },
    methods: {
      getUser() {
        return new Promise((resolve, reject) => {
          this.$axios
            .get('base/user/info/')
            .then((response) => {
              this.user = response.data
              resolve(response)
            })
            .catch((error) => {
              reject(error)
            })
        })
      },
      handleSubmit() {
        this.$store
          .dispatch('auth/logout')
          .then(() => {
            this.$router.push('/login')
          })
          .catch(() => {})
      }
    }
  }
</script>
