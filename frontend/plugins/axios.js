export default function ({ $axios, redirect }) {
  $axios.setBaseURL('http://localhost:8000/api/v1/')

  $axios.onRequest((config) => {
    config.withCredentials = true
    return config
  })

  $axios.onResponseError((err) => {
    if (err.response.status === 401) {
      redirect('/login')
    }
  })
}
