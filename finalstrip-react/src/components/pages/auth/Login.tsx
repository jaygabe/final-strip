import { SyntheticEvent, useState } from "react";
import { Navigate } from "react-router-dom";
import {useDispatch} from "react-redux";
import {setAuth} from "../../../redux/authSlice";

import { LoginForm } from "../../forms/LoginForm";
// import { AuthenticatorForm } from "../../forms/AuthenticatorForm";


export const Login = () => {
    const dispatch = useDispatch();
    const [redirect, setRedirect] = useState(false);
    const [loginData, setLoginData] = useState<{
        id: number;
        secret?: string;
        otpauth_url?: string;
    }>({
        id: 0
    });

    const success = () => {
        setRedirect(true);
        dispatch(setAuth(true));

        if (redirect){
            return <Navigate to="/" />
        }
    }

    let form;
    
    if (loginData?.id === 0) {
        form = <LoginForm loginData={setLoginData} success={success} />
    } else {
        // form = <AuthenticatorForm loginData={loginData} success={success} />
        // form = <h1>You are already logged in.</h1>
        form = <Navigate to="/" />
    }

    return (
        <main className="container">
            {form}
        </main>
    )
}