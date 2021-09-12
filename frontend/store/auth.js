import axios from 'axios'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'

export const LOGOUT = 'LOGOUT'
export const LOGIN = 'LOGIN'

export const state = () => ({
  userId: null,
  payload: Cookies.get('payload') || null,
  isAuthenticated: false
})

export const getters = () => ({
  payload: (state) => state.payload,
  userId: (state) => state.userId,
  checkPayload: (state) => state.payload !== null
})

export const mutations = {
  [LOGIN](state, { payload }) {
    // state.userId = decodePayload.userId
    state.payload = payload
  },

  [LOGOUT](state) {
    // state.payload = null
    // Cookies.remove('payload')
  }
}

export const actions = {
  // login({ commit }, { username, password }) {
  //   this.$axios
  //     .post('base/login/', { username, password })
  //     .then((response) => {
  //       // commit('login', { accessToken, refreshToken })
  //     })
  //     .catch(() => {})
  // },
  login({ commit }, { username, password }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post('base/login/', { username, password })
        .then((response) => {
          const payload = response.data.payload
          const decode = jwtDecode(payload, { header: true })
          const id = decode.userId
          /* eslint-disable */
          console.log(id)

          // commit(LOGIN, { payload })
          resolve(response)
        })
        .catch((error) => {
          // commit(LOGOUT)
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
