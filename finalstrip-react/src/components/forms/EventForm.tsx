import {useState, SyntheticEvent} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { FormTextElement } from './form elements/FormTextElement';
import { FormDateElement } from './form elements/FormDateElement';
import { FormSelectElement } from './form elements/FormSelectElement';
import { EVENT_CHOICES, WEAPON_CHOICES } from '../../constants/VarOptions';
import { CSRF } from './form elements/CSRF';
import { getNewRefreshToken} from '../../hooks/utils';


export const EventForm = () => {

    const {tournamentSlug} = useParams()
    const [eventName, setEventName] = useState<string>('')
    const [date, setDate] = useState<string>('')
    const [eventLevel, setEventLevel] = useState<string>('')
    const [notes, setNotes] = useState<string>('')
    const [weapon, setWeapon] = useState<string>('')

    

    // Send form to the backend to be processed
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        await getNewRefreshToken()

        const {data} = await axios.post('api/events/create/', {
            'tournament_slug': tournamentSlug,
            'name': eventName,
            date,
            weapon,
            'event_level': eventLevel,
            notes,
            
        }, {withCredentials: true});
    }

    return(
        <>
            <form onSubmit={submit}>
                
                <h1 className='h1'>New Event</h1>

                <CSRF/>
                <FormTextElement setValue={setEventName} elementName='event' placeholder='' labelText='Event Name'/>
                <FormDateElement setValue={setDate} elementName='date' placeholder='' labelText='Date' />
                <FormSelectElement setValue={setWeapon} elementName='weapon' selectOptions={WEAPON_CHOICES} placeholder='' labelText='Weapon' />
                <FormSelectElement setValue={setEventLevel} elementName='event-level' selectOptions={EVENT_CHOICES} placeholder='' labelText='Event Level'/>
                <FormTextElement setValue={setNotes} elementName='host' placeholder='' labelText='Notes'/>

                <button className='submit-button' type='submit'>Add Event</button>
            </form>
        </>  
    )}