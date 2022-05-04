export default function ({ store, redirect }) {
  const prom = new Promise((resolve, reject) => {
    store
      .dispatch('auth/checkAuthUser')
      .then(() => {
        resolve()
      })
      .catch(() => {
        return redirect('/login')
      })
  })
  prom.then(() => {
    return redirect('/')
  })
}

// проверка на авторизированного пользователя
// export default function ({ $axios }, to, from, next) {
//   const prom = new Promise((resolve, reject) => {
//     $axios
//       .get('auth/user/check/')
//       .then((response) => {
//         resolve(response)
//       })
//       .catch((error) => {
//         reject(error)
//       })
//   })
//   prom.then((response) => {
//     if (response.status === 200) {
//       next({
//         name: '/login'
//       })
//     }
//   })
// }
