export default function ({ $axios, redirect }) {
  $axios.get('base/user/checking/').then((response) => {
    if (response.status === 200) {
      return redirect('/')
    }
  })
}
