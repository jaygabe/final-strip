import axios from 'axios'
import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';

import {setAuth} from '../../../redux/authSlice'
import {RootState} from '../../../redux/store'

import {PushNote} from '../../PushNote';


export const Home = () => {
    const [message, setMessage] = useState('You are not Logged In')
    const dispatch = useDispatch()
    const auth = useSelector((state: RootState) => state.auth.value)

    useEffect(() => {
        (async () => {
            try {
                const {data} = await axios.get('api/auth/user');
                setMessage(`Hi ${data.first_name} ${data.last_name}`);
                dispatch(setAuth(true))
            } catch (e) {
                setMessage('You are not authenticated');
                dispatch(setAuth(false))
            }
        })()
    }, [message])


    return (
        <div className='container text-center'>
            <h3 className='test'>{auth ? message : 'You are not authenticated'}</h3>
            
            <h2>To do list</h2>
            <ul>
                <li>figure out python dependency issue</li>
                <li>Fix auth that may be related to dependency issue</li>
                <li>tourn and event forms need to add user before save, pass into parent serializer?</li>
                <li>fix transparent mobile menu and make bottom sticky</li>
                <li>migrate to postgres</li>
                <li>add stripe</li>
                <li>add docker and deploy</li>
                <li>get logo and icons</li>
                <li>clean up auth and redirects in Login.tsx and LoginForm.tsx</li>
                <li></li>
                <br />
                <li>create a card framework for tourns, events, and bouts with delete and edit buttons</li>
                <li>button to return to top of the page</li>
                <li>move types and constants to one folder</li>
                <li>cards should be counted not bool</li>
                <li>make usfa fencer data linked</li>
                <br />
                <li>Journal component could be a footer bar for mobile display</li>
                <li>views repeat a lot create a custom abstract model to handle it better</li>
                <li>clean up paranthesis and make single over entire project (mostly auth)</li>
                <li>build out public profile pages</li>
                
                <br />
                <li>make referee data linkable</li>
                <li>web links to tournament</li>
                <li>video links to bouts</li>
                <li>robot.txt with honeypot</li>
                <li>front and backend testing</li>
                <li></li>
            </ul>
            <h4>best practices</h4>
            <ul>
                <li>useRef for forms</li>
                <li>use function form of useState to increment data</li>
                <li></li>
                <li></li>
            </ul>

            <h4>Other links</h4>
            <ul>
                <li>not sure why I am saving this one: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218959</li>
                <li>scientific fencing papers:  https://scholar.google.com/scholar?hl=en&as_sdt=0%2C7&as_vis=1&q=fencing+journal+&btnG=</li>
                <li>PWA service worker:  https://medium.com/delivus/creating-pwa-with-react-in-typescript-2174ac4a89a2</li>
                <li>referee database to scrape:  https://member.usafencing.org/referees/search?page=2</li>
                <li></li>
            </ul>

            <h4>Welcome to the home page!</h4>
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