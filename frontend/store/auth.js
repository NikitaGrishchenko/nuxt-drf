import axios from 'axios'
// import Cookies from 'js-cookie'
// import jwtDecode from 'jwt-decode'

export const LOGOUT = 'LOGOUT'
export const LOGIN = 'LOGIN'

export const state = () => ({
  userId: null,
  isAuthenticated: false
})

export const getters = () => ({
  userId: (state) => state.userId,
  checkPayload: (state) => state.payload !== null
})

export const mutations = {
  [LOGIN](state) {
    state.isAuthenticated = true
  },

  [LOGOUT](state) {
    state.isAuthenticated = false
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
      axios
        .post('auth/delete/')
        .then((response) => {
          commit(LOGOUT)
          resolve(response)
        })
        .catch((error) => {
          commit(LOGOUT)
          reject(error)
        })
    })
  }
}
