import axios from 'axios'
import Cookies from 'js-cookie'
import jwtDecode from 'jwt-decode'

export const LOGOUT = 'LOGOUT'
export const LOGIN = 'LOGIN'

export const state = () => ({
  accessToken: Cookies.get('access_token') || null,
  isAuthenticated: false
})

export const getters = () => ({
  payload: (state) => state.payload,
  user: (state) => {
    if (state.payload) {
      return jwtDecode(state.payload, { header: true })
    }
    return null
  },
  check: (state) => state.payload !== null
})

export const mutations = {
  login(state, { accessToken, refreshToken }) {
    // const user = jwtDecode(payload, { header: true })
    // const d = new Date(0)
    // d.setUTCSeconds(user.exp)
    // state.payload = payload

    // Cookies.set('access_token', accessToken, {
    //   expires: data
    // })

    // access token
    const accessTokenPayload = accessToken.split('.')[1]
    const accessTokenPayloadDecode = jwtDecode(accessTokenPayload, {
      header: true
    })
    const dateAccess = new Date(0)
    dateAccess.setUTCSeconds(accessTokenPayloadDecode.exp)
    Cookies.set('access_token', accessToken, {
      expires: dateAccess,
      sameSite: 'strict'
    })
    // refresh token
    const refreshTokenPayload = refreshToken.split('.')[1]
    const refreshTokenPayloadDecode = jwtDecode(refreshTokenPayload, {
      header: true
    })
    const dateRefresh = new Date(0)
    dateRefresh.setUTCSeconds(refreshTokenPayloadDecode.exp)
    Cookies.set('refresh_token', refreshToken, {
      expires: dateRefresh,
      sameSite: 'strict'
    })
  },

  [LOGOUT](state) {
    state.payload = null
    Cookies.remove('payload')
  }
}

export const actions = {
  login({ commit }, { username, password }) {
    this.$axios
      .post('base/login/', { username, password })
      .then((response) => {
        // const accessToken = response.data.access.split('.')[1]
        // const payload = response.data.refresh.split('.')[1]
        const accessToken = response.data.access
        const refreshToken = response.data.refresh

        // const payloadDecode = jwtDecode(payload, { header: true })

        // const data = new Date(0)
        // data.setUTCSeconds(payloadDecode.exp)

        // console.log(payloadDecode)

        // Cookies.set('access_token', accessToken, {
        //   expires: data
        // })

        commit('login', { accessToken, refreshToken })
      })
      .catch(() => {})
  },

  refresh({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .post('auth/refresh/')
        .then((response) => {
          const payload = response.data.access.split('.')[1]
          commit(LOGIN, { payload })
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
