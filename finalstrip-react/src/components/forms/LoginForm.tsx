import { SyntheticEvent, useState } from "react";
import { Link} from "react-router-dom";
import axios from "axios"
import { GoogleLogin } from '@react-oauth/google';


export const LoginForm = (props: {
    loginData: Function
    success: Function
}) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");


    //send email and password to django for JWT
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        const {data} = await axios.post("auth/login", {
            email,
            password,
        }, {withCredentials: true});  //credentials might be added in the interceptor
        if (data == undefined) {
            return 
        }
        props.loginData(data);
    }


    // authorizes token from Google and stores in the header
    const onSuccess = async (googleUser: any) => {
        
        // console.log(googleUser)
        const {status, data} = await axios.post('auth/google-auth', {
            token: googleUser.credential
        }, {withCredentials: true});

        axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`;

        if (status === 200) {
            props.success();
        }
    }

    // alert to error if google button fails
    const onError = () => {
        console.log('Turns out failure was an option...');
    }
    

    return(
        <>
            <form className='auth-form' onSubmit={submit}>
                
                <h1 className="h1">Please sign in</h1>

                <label htmlFor="floatingInput">Email address</label>
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                    onChange={e => setEmail(e.target.value)}
                />

                <label htmlFor="floatingPassword">Password</label>
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                    onChange={e => setPassword(e.target.value)}
                />

                <div className="mb">
                    <Link to={'/forgot'}>Forgot Password</Link>
                </div>
                <button className="submit-button" type="submit">Sign in</button>
            </form>
            
            <br />
            
            <div className="google-login">
                <GoogleLogin  
                    onSuccess={onSuccess}
                    onError={onError}
                    useOneTap
                    theme="filled_blue"
                />
            </div>
            
        </>
        
    )
}