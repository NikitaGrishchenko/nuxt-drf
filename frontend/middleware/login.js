// проверка на авторизированного пользователя
export default function ({ $axios, redirect }) {
  $axios.get('auth/user/check/').then((response) => {
    if (response.status === 200) {
      return redirect('/')
    }
  })
}
