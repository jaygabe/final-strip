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

    //send regular email and password to django
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        const {data} = await axios.post("login", {
            email,
            password,
        });  //might need credentials

        props.loginData(data);
    }

    //store token in header and auth using google
    const onSuccess = async (googleUser: any) => {
        
        console.log(googleUser)
        const {status, data} = await axios.post('google-auth', {
            token: googleUser.credential
        }, {withCredentials: true});

        axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`;

        if (status === 200) {
            props.success();
        }
    }

    // alert to error if google button fails
    const onError = () => {
        console.log('Failure was an option...');
    }
    

    return(
        <>
            <form onSubmit={submit}>
                <h1 className="h1 mb-3 fw-bold">Please sign in</h1>

                <div className="form-floating">
                    <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                        onChange={e => setEmail(e.target.value)}
                    />
                    <label htmlFor="floatingInput">Email address</label>
                </div>
                <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                        onChange={e => setPassword(e.target.value)}
                    />
                    <label htmlFor="floatingPassword">Password</label>
                </div>

                <div className="mb-3">
                    <Link to={'/forgot'}>Forgot Password?</Link>
                </div>
                <button className="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
            </form>
            <br />
            <GoogleLogin  
                
                onSuccess={onSuccess}
                onError={onError}
                useOneTap
            />
        </>
        
    )
}