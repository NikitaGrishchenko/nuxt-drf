// import store from 'store'

export default function ({ $axios, redirect }) {
  $axios.setBaseURL('http://localhost:8000/api/v1/')

  $axios.onRequest((config) => {
    config.withCredentials = true
    // this.$store.dispatch('auth/currentUserInfo')
    // console.log(config)
    // store.dispatch('auth/currentUserInfo')
    return config
  })

  // $axios.onResponse((response) => {
  //   if (response.status === 200) {
  //     console.log(response.status)
  //     testTest()
  //     return response
  //   }
  // })
  // async function testTest() {
  //   await store.dispatch('auth/currentUserInfo')
  // }
  $axios.onResponseError((err) => {
    if (err.response.status === 401) {
      redirect('/login')
    }
  })
}
