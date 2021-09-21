// import axios from 'axios'
// import Cookies from 'js-cookie'
// import jwtDecode from 'jwt-decode'

export const LOGOUT = 'LOGOUT'
export const LOGIN = 'LOGIN'
export const GET_USER = 'GET_USER'

export const state = () => ({
  user: null,
  isAuthenticated: false
})

export const getters = {
  user: (state) => {
    return state.user
  }
}

export const mutations = {
  [LOGIN](state) {
    state.isAuthenticated = true
  },

  [LOGOUT](state) {
    state.isAuthenticated = false
  },

  [GET_USER](state, userData) {
    state.user = userData
  }
}

export const actions = {
  login({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post('base/login/', { username, password })
        .then((response) => {
          commit(LOGIN)
          resolve(response)
        })
        .catch((error) => {
          commit(LOGOUT)
          reject(error)
        })
    })
  },

  logout({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post('base/logout/')
        .then((response) => {
          commit(LOGOUT)
          resolve(response)
        })
        .catch((error) => {
          commit(LOGOUT)
          reject(error)
        })
    })
  },

  currentUserInfo({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get('base/user/info/')
        .then((response) => {
          const userData = response.data
          commit(GET_USER, userData)
          resolve(response)
        })
        .catch((error) => {
          // commit(LOGOUT)
          reject(error)
        })
    })
  }
}
