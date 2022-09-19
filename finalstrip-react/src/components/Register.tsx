import { SyntheticEvent, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios"

export const Register = () => {
    
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirm, setPasswordConfirm] = useState("");
    const [redirect, setRedirect] = useState(false);
    const [usafNumber, setUsafNumber] = useState("");

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        await axios.post("register", {
            first_name: firstName,
            last_name: lastName,
            usaf_number: usafNumber,
            email,
            password,
            password_confirm: passwordConfirm

        });

        setRedirect(true);
    }

    if (redirect){
        return <Navigate to="auth/login" />
    }

    return (
        <main className="container">
            <form onSubmit={submit}>
                <h1 className="h1 mb">Please Register</h1>

                <label htmlFor="email">Email address: </label>
                <input type="email" className="" id="email" placeholder="name@example.com"
                    onChange={e => setEmail(e.target.value)} required
                />
            
                <label htmlFor="password">Password: </label>
                <input type="password" className="form-control" id="password" placeholder="Password"
                    onChange={e => setPassword(e.target.value)} required
                />
            
                <label htmlFor="passwordConfirm">Confirm Password: </label>
                <input type="password" className="form-control" id="passwordConfirm" placeholder="Password Confirm"
                    onChange={e => setPasswordConfirm(e.target.value)} required
                />
                
                <label htmlFor="firstName">First Name: </label>
                <input type="text" className="form-control" id="firstName" placeholder="First Name"
                    onChange={e => setFirstName(e.target.value)}
                />
                
                
                <label htmlFor="lastName">Last Name: </label>
                <input type="text" className="form-control" id="lastName" placeholder="Last Name"
                    onChange={e => setLastName(e.target.value)}
                />
                
                <label htmlFor="fencingNumber">USA Fencing Number: </label>
                <input type="text" className="form-control id-field" id="fencingNumber" placeholder="100000000"
                    onChange={e => setUsafNumber(e.target.value)}
                />

                <button className="submit-button" type="submit">Sign in</button>
            </form>
        </main>
    )
}