import Cookies from 'js-cookie'

export default function ({ $axios, redirect }) {
  $axios.setBaseURL('http://localhost:8000/api/v1/')

  const csrf = Cookies.get('csrftoken')
  $axios.setHeader('X-CSRFToken', csrf)

  console.log(csrf)

  $axios.onRequest((config) => {
    config.withCredentials = true

    return config
  })
}
