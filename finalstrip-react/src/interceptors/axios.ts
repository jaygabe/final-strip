import axios from "axios";


axios.defaults.baseURL = "http://localhost:8000/";
axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


let refresh = false
let refreshTokenPromise: Promise<string | void> | null = null

const getRefreshToken = (): Promise<string | void> => {
    return axios.post('api/auth/refresh', {withCredentials: true,}
    ).then((response)=>{
        return response.data.token
    })
}

axios.interceptors.response.use(resp => resp, async error => {
  if ((error.response.status === 401 && !refresh) || (error.response.status === 500 && !refresh)) {
    console.log('interceptor')
    if (!refreshTokenPromise) {
      // if nothing is in-progress, start a new refresh token request
      refreshTokenPromise = getRefreshToken().then((token) => {
        refreshTokenPromise = null; // clear state
        return token; // resolve with the new token
      });
    }
    return refreshTokenPromise.then((token) => {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
        return axios.request(error.config);
    });
  }
  refresh = false
  refreshTokenPromise = null;
  return Promise.reject(error);
});


// // use to check response before it hits django
// axios.interceptors.request.use(function (config) {
//     // Do something before request is sent
//     console.log(config)
//     return config;
//   }, function (error) {
//     // Do something with request error
//     return Promise.reject(error);
//   });


// Old method that did not allow for multiple requests at the same time because of timing of auth tokens refreshing
// let refresh = false
// axios.interceptors.response.use(resp => resp, async error => {
//     if ((error.response.status === 401 && !refresh) || (error.response.status === 500 && !refresh)) {     
//         refresh = true;
//         const response = await axios.post('api/auth/refresh') 
//         if (response.status === 200) {
//             axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
//             console.log('interceptor authenticated')
//             return axios(error.config);
//         }else{
//             console.log("interceptor failed")
//         }
//     }
//     refresh = false;
//     return error;
// });