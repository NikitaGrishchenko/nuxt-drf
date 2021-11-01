import Swal from 'sweetalert2'

// общие настройки для sweet alert 2
export const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showCloseButton: true,
  showConfirmButton: false,
  timer: 7000,
  timerProgressBar: true,
  customClass: {
    title: 'custom-swal__title'
  }
})
