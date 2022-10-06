import {useState, SyntheticEvent} from 'react';
import axios from 'axios';


export const TournamentForm = () => {

    const [tournName, setTournName] = useState('')
    const [date, setDate] = useState('')
    const [location, setLocation] = useState('')
    const [eventLevel, setEvetLevel] = useState('')
    const [club, setClub] = useState('')
    
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        const {data} = await axios.post('journal/tournament/', {
            'name': tournName,
            date,
            location,
            club,
            'event_level': eventLevel
        }, {withCredentials: true});
    }

    return(
        <div className='container'>
            <form onSubmit={submit}>
                
                <h1 className='h1'>New Tournament</h1>
                <div>
                    <label htmlFor='nameInput'>Tournament Name:</label>
                    <input type='tournName' className='form-control' id='nameInput' placeholder='Tournament'
                        onChange={e => setTournName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor='dateInput'>Date:</label>
                    <input type='date' className='form-control' id='dateInput' placeholder='01-01-1900'
                        onChange={e => setDate(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor='locationInput'>Location:</label>
                    <input type='location' className='form-control' id='locationInput' placeholder='Washington, DC'
                        onChange={e => setLocation(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor='clubInput'>Club:</label>
                    <input type='string' className='form-control' id='clubInput' placeholder='USA Fencing'
                        onChange={e => setClub(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor='eventLevelInput'>Event Level:</label>
                    <input type='string' className='form-control' id='eventLevelInput' placeholder='Local'
                        onChange={e => setEvetLevel(e.target.value)}
                    />
                </div>
                <button className='submit-button' type='submit'>Add Tournament</button>
            </form>
        </div>  
    )}