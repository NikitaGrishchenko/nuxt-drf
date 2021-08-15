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
          }
        ]
      }
    }
  }
</script>
