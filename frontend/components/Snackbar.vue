<template>
  <v-snackbar v-model="viewSnackbar">
    {{ text }}
    <template #action="{ attrs }">
      <v-btn
        :color="color"
        fab
        x-small
        v-bind="attrs"
        @click="viewSnackbar = false"
      >
        <v-icon>{{ icon }}</v-icon>
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
  export default {
    name: 'Snackbar',
    props: {
      viewSnackbar: {
        type: Boolean,
        default: false
      },
      text: {
        type: String,
        default: ''
      },
      color: {
        type: String,
        default: 'red'
      },
      icon: {
        type: String,
        default: 'mdi-close'
      }
    }
  }
</script>
