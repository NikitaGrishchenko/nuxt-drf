// при загрузке/перезагрузке страницы обновлять асинхронно данные пользователя
export default async function ({ store }) {
  await store.dispatch('auth/currentUserInfo')
}
