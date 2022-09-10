import axios from "axios"
import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux";

import {setAuth} from '../redux/authSlice'
import {RootState} from '../redux/store'

import {PushNote} from "./PushNote";


export const Home = () => {
    const [message, setMessage] = useState("You are not Logged In")
    const dispatch = useDispatch()
    const auth = useSelector((state: RootState) => state.auth.value)

    useEffect(() => {   //  first useEffect function cannot use async
        (async () => {
            try {
                const {data} = await axios.get('user');

                setMessage(`Hi ${data.first_name} ${data.last_name}`);
                dispatch(setAuth(true))
            } catch (e) {
                setMessage('You are not authenticated');
                dispatch(setAuth(false))
            }
        })()
    }, [])

    return (
        <div className="container mt-5 text-center">
            <h3>{auth ? message : 'You are not authenticated'}</h3>

            <PushNote />

        </div>
    )
}