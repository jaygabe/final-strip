import axios from "axios"
import { useLocation } from 'react-router-dom'

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

// get the slug from the url of a page, useParams instead
// export const useSlug = (): string => {
//   const location = useLocation()
//   const pathname = location.pathname
//   const parts = pathname.split('/')
//   const slug = parts[parts.length - 1]

//   return slug
// }