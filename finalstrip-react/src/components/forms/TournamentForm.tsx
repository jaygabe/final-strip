import {useState, SyntheticEvent} from 'react';
import axios from 'axios';
import { FormTextElement } from './FormTextElement';


export const TournamentForm = () => {

    const [tournName, setTournName] = useState<string>('')
    const [date, setDate] = useState<string>('')
    const [location, setLocation] = useState<string>('')
    const [eventLevel, setEvetLevel] = useState<string>('')
    const [club, setClub] = useState<string>('')
    
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

                <FormTextElement setValue={setTournName} labelText='Tourn'/>
                
                <div className='form-input'>
                    <input type='date' id='dateInput' placeholder=''
                        onChange={e => setDate(e.target.value)}
                    />
                    <label htmlFor='dateInput'>Date</label>
                </div>
                
                <FormTextElement setValue={setLocation} labelText='Location'/>
                <FormTextElement setValue={setClub} labelText='Host Club'/>
                
                <div className='form-input'>
                    <select id='eventLevelInput'
                        onChange={e => setEvetLevel(e.target.value)}
                    >
                        <option value=""></option>
                        <option value="Local">Local</option>
                        <option value="Regional">Regional</option>
                        <option value="National">National</option>
                        <option value="World">World</option>
                    </select>
                    <label htmlFor='eventLevelInput'>Event Level</label>
                </div>

                <button className='submit-button' type='submit'>Add Tournament</button>
            </form>
        </div>  
    )}