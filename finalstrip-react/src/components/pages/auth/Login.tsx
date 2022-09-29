import { SyntheticEvent, useState } from "react";
import { Link, Navigate } from "react-router-dom";
import {useDispatch} from "react-redux";
import {setAuth} from "../../../redux/authSlice";

import { LoginForm } from "../../forms/LoginForm";
import { AuthenticatorForm } from "../../forms/AuthenticatorForm";


export const Login = () => {
    // https://getbootstrap.com/docs/5.2/examples/sign-in/
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
    }

    if (redirect){
        return <Navigate to="/" />
    }

    let form;

    if (loginData?.id === 0) {
        form = <LoginForm loginData={setLoginData} success={success} />
    } else {
        form = <AuthenticatorForm loginData={loginData} success={success} />
    }

    return (
        <main className="container">
            {form}
        </main>
    )
}