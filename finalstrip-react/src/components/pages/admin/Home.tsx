import axios from "axios"
import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux";

import {setAuth} from '../../../redux/authSlice'
import {RootState} from '../../../redux/store'

import {PushNote} from "../../PushNote";


export const Home = () => {
    const [message, setMessage] = useState("You are not Logged In")
    const dispatch = useDispatch()
    const auth = useSelector((state: RootState) => state.auth.value)

    useEffect(() => {   //  first useEffect function cannot use async
        (async () => {
            try {
                const {data} = await axios.get('auth/user');

                setMessage(`Hi ${data.first_name} ${data.last_name}`);
                dispatch(setAuth(true))
            } catch (e) {
                setMessage('You are not authenticated');
                dispatch(setAuth(false))
            }
        })()
    }, [])

    return (
        <div className="container text-center">
            <h3>{auth ? message : 'You are not authenticated'}</h3>
            
            <h4>To do list</h4>
            <ul>
                
                <li>fix transparent mobile menu and make bottom sticky</li>
                <li>Journal component could be a footer bar for mobile display</li>
                <li>views repeat a lot create a custom abstract model to handle it better</li>
                <li>create a card framework for tourns, events, and bouts with delete and edit buttons</li>
                <li>button to return to top of the page</li>
                <li>clean up paranthesis and make single over entire project</li>
                <li></li>
            </ul>
            <p>Other links</p>
            <ul>
                <li>not sure why I am saving this one: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218959</li>
                <li>scientific fencing papers:  https://scholar.google.com/scholar?hl=en&as_sdt=0%2C7&as_vis=1&q=fencing+journal+&btnG=</li>
                <li>PWA service worker:  https://medium.com/delivus/creating-pwa-with-react-in-typescript-2174ac4a89a2</li>
                <li></li>
                <li></li>
            </ul>

            <p>Welcome to the home page!</p>
            <ul>
                <li>Keep track of progess and competitions</li>
                <li>Review past bouts and tournaments</li>
                <li>Share notes with friends</li>
                <li>analyze your progress</li>
                <li>set goals</li>
                <li>unlimited entries</li>
                <br />
                <li>https://academyoffencingmasters.com/blog/fencing-journal-a-how-to-guide/</li>
                <li>https://www.usafencing.org/american-fencing-magazine ads starts at $638</li>
            </ul>
        </div>
    )
}