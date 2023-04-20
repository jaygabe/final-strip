import axios from "axios"
import { useLocation } from 'react-router-dom'

// useConfirmAuth imports
import {setAuth} from '../redux/authSlice'
import { useDispatch } from 'react-redux';
import { useEffect } from "react";

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

export function useConfirmAuth(confirm: boolean){
  const dispatch = useDispatch()
  useEffect(() => {
    if (confirm){
      dispatch(setAuth(true))
    }
  }, [confirm])
  
  
}

// get the slug from the url of a page, useParams instead
// export const useSlug = (): string => {
//   const location = useLocation()
//   const pathname = location.pathname
//   const parts = pathname.split('/')
//   const slug = parts[parts.length - 1]

//   return slug
// }