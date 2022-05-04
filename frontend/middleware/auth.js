// при загрузке/перезагрузке страницы обновлять асинхронно данные пользователя
export default async function ({ store, route, redirect }) {
  // if (
  //   (route.fullPath === '/login' || route.fullPath === '/registration') &&
  //   store.getters['auth/isAuthenticated']
  // ) {
  //   redirect('/')
  // } else if (
  //   (route.fullPath === '/login' || route.fullPath === '/registration') &&
  //   !store.getters['auth/isAuthenticated']
  // ) {
  //   console.log('!')
  // } else {
  await store
    .dispatch('auth/currentUserInfo')
    .then(() => {
      route.fullPath === '/login' && redirect('/')
      route.fullPath === '/registration' && redirect('/')
      console.log(store.getters['auth/isAuthenticated'])
    })
    .catch(() => {})

  // !store.getters['auth/isAuthenticated'] && redirect('/login')
}
