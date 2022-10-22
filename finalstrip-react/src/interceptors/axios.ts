import axios from "axios";


axios.defaults.baseURL = "http://localhost:8000/";
axios.defaults.withCredentials = true;

let refresh = false;

axios.interceptors.response.use(resp => resp, async error => {
    if (error.response.status === 401 && !refresh) {
        refresh = true;
        console.log('interceptor refreshing')
        const response = await axios.post('auth/refresh');

        if (response.status === 200) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;

            return axios(error.config);
        }
    }
    refresh = false;
    return error;
});