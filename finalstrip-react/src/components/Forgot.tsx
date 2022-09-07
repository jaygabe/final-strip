import axios from "axios";
import React, {SyntheticEvent, useState} from "react";


export const Forgot = () => {
    const [email, setEmail] = useState('');
    const [notify, setNotify] = useState({
        show: false,
        error: false,
        message: ''
    })

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault()

        try{
            await axios.post('forgot', {email});
            setNotify({
                show: true,
                error: false,
                message: 'Reset email sent.  Please check your inbox.'                
            });
        } catch(e) {
            setNotify({
                show: true,
                error: true,
                message: 'There was an error.'                
            });
        } 
    }

    let info;
    if (notify.show) {
        info = <div className={notify.error ? 'alert alert-danger' : 'alert alert-success'} role='alert'>
            {notify.message}
        </div>
    }

    return (
        <main className="form-signin w-100 m-auto mt-5">
            {info}
            
            <form onSubmit={submit}>
            <h1 className="h1 mb-3 fw-bold">Please enter you email</h1>

            <div className="form-floating">
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                    onChange={e => setEmail(e.target.value)}
                />
                <label htmlFor="floatingInput">Email address</label>
            </div>
            
            <button className="w-100 btn btn-lg btn-primary" type="submit">Submit Email</button>
            </form>
        </main>
    )
}
