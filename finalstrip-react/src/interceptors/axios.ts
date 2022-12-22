import axios from "axios";


axios.defaults.baseURL = "http://localhost:8000/";
axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

let refresh = false;

axios.interceptors.response.use(resp => resp, async error => {
    if ((error.response.status === 401 && !refresh) || (error.response.status === 500 && !refresh)) {
        refresh = true;
        console.log('interceptor refreshing')
        const response = await axios.post('api/auth/refresh');

        if (response.status === 200) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;

            return axios(error.config);
        }else{
            console.log("interceptor failed")
        }
    }
    refresh = false;
    return error;
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