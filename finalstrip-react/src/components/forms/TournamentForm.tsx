import {useState, SyntheticEvent} from 'react';
import axios from 'axios';
import { FormTextElement } from './form elements/FormTextElement';
import { FormDateElement } from './form elements/FormDateElement';
import { FormSelectElement } from './form elements/FormSelectElement';


export const TournamentForm = () => {

    const [tournName, setTournName] = useState<string>('')
    const [date, setDate] = useState<string>('')
    const [location, setLocation] = useState<string>('')
    const [eventLevel, setEventLevel] = useState<string>('')
    const [club, setClub] = useState<string>('')

    // select options
    const eventLevelOptions = {
        'Local': 'Local',
        'Regional': 'Regional',
        'National': 'National',
        'World': 'World'
    }

    // Send form to the backend to be processed
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
        <>
            <form onSubmit={submit}>
                
                <h1 className='h1'>New Tournament</h1>

                <FormTextElement setValue={setTournName} elementName='tournament' placeholder='' labelText='Tournament Name'/>
                <FormDateElement setValue={setDate} elementName='date' placeholder='' labelText='Date' />
                <FormTextElement setValue={setLocation} elementName='location' placeholder='' labelText='Location'/>
                <FormTextElement setValue={setClub} elementName='host' placeholder='' labelText='Host Club'/>
                <FormSelectElement setValue={setEventLevel} selectOptions={eventLevelOptions} elementName='eventlevel' placeholder='' labelText='Event Level'/>

                <button className='submit-button' type='submit'>Add Tournament</button>
            </form>
        </>  
    )}