import { useState, SyntheticEvent } from "react";
import { Navigate, useParams } from "react-router-dom";
import axios from "axios";


export const Reset = () => {
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [redirect, setRedirect] = useState(false);
    const {token} = useParams();


    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await axios.post('reset', {
            token,
            password,
            password_confirm: passwordConfirm
        });
        setRedirect(true)
    }

    if(redirect){
        return <Navigate to="/login" />
    }
    
    return (
        <main className="form-signin w-100 m-auto mt-5">
            
            <form onSubmit={submit}>
            <h1 className="h1 mb-3 fw-bold">Reset your password</h1>

            <div className="form-floating">
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                    onChange={e => setPassword(e.target.value)}
                />
                <label htmlFor="floatingPassword">Password</label>
            </div>
            <div className="form-floating">
                <input type="password" className="form-control" id="floatingPasswordConfirm" placeholder="Password Confirm"
                    onChange={e => setPasswordConfirm(e.target.value)}
                />
                <label htmlFor="floatingPassword">Change Password</label>
            </div>
            
            <button className="w-100 btn btn-lg btn-primary" type="submit">Submit Email</button>
            </form>
        </main>
    )
}