import * as types from '../constants'

export const state = () => ({
  user: null,
  isAuthenticated: false
})

export const getters = {
  user: (state) => {
    return state.user
  },
  isAuthenticated: (state) => {
    return state.isAuthenticated
  }
}

export const mutations = {
  [types.LOGIN](state) {
    state.isAuthenticated = true
  },

  [types.LOGOUT](state) {
    state.isAuthenticated = false
  },

  [types.GET_USER](state, userData) {
    state.user = userData
  }
}

export const actions = {
  login({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post('auth/login/', { username, password })
        .then((response) => {
          commit(types.LOGIN)
          resolve(response)
        })
        .catch((error) => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  },

  logout({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post('auth/logout/')
        .then((response) => {
          commit(types.LOGOUT)
          resolve(response)
        })
        .catch((error) => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  },

  currentUserInfo({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get('auth/user/info/')
        .then((response) => {
          const userData = response.data
          commit(types.GET_USER, userData)
          resolve(response)
        })
        .catch((error) => {
          commit(types.LOGOUT)
          reject(error)
        })
    })
  }
}
