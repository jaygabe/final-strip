import axios from "axios"


export const getNewRefreshToken = (): Promise<void> => {
    return axios.post('api/auth/refresh').then((response) => {
      if (response.status === 200) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
        console.log('refresh success')
      } else {
        console.log('refresh failed')
      }
    })
  }