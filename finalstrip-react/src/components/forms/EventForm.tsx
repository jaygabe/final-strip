import {useState, SyntheticEvent} from 'react';
import axios from 'axios';
import { FormTextElement } from './form elements/FormTextElement';
import { FormDateElement } from './form elements/FormDateElement';
import { FormSelectElement } from './form elements/FormSelectElement';


export const EventForm = () => {

    const [eventName, setEventName] = useState<string>('')
    const [date, setDate] = useState<string>('')
    const [eventLevel, setEventLevel] = useState<string>('')
    const [notes, setNotes] = useState<string>('')

    // select options
    const EVENT_CHOICES = {
        'Y8': 'Y8',
        'Y10': 'Y10',
        'Y12': 'Y12',
        'Y14': 'Y14',
        'Cadet': 'Cadet',
        'Junior': 'Junior',
        'Senior/Open': 'Senior/Open',
        'Vet Combined': 'Vet Combined',
        'Vet40': 'Vet40',
        'Vet50': 'Vet50',
        'Vet60': 'Vet60',
        'Vet70': 'Vet70',
        'Vet80': 'Vet80',
        'Div I': 'Div I',
        'Div IA': 'Div IA',
        'Div II': 'Div II',
        'Div III': 'Div III',
        'Para': 'Para',
        'Modern Pentathlon': 'Modern Pentathlon'
    }

    // Send form to the backend to be processed
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.
        
        const {data} = await axios.post('journal/event/', {
            'name': eventName,
            date,
            notes,
            'event_level': eventLevel
        }, {withCredentials: true});
    }

    return(
        <>
            <form onSubmit={submit}>
                
                <h1 className='h1'>New Event</h1>

                <FormTextElement setValue={setEventName} elementName='event' placeholder='' labelText='Event Name'/>
                <FormDateElement setValue={setDate} elementName='date' placeholder='' labelText='Date' />
                <FormSelectElement setValue={setEventLevel} elementName='eventlevel' selectOptions={EVENT_CHOICES} placeholder='' labelText='Event Level'/>
                <FormTextElement setValue={setNotes} elementName='host' placeholder='' labelText='Notes'/>

                <button className='submit-button' type='submit'>Add Tournament</button>
            </form>
        </>  
    )}