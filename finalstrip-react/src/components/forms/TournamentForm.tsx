import {useState, SyntheticEvent} from 'react'
import axios from 'axios'

import { FormTextElement } from './form elements/FormTextElement'
import { FormDateElement } from './form elements/FormDateElement'
import { FormSelectElement } from './form elements/FormSelectElement'
import { CSRF } from './form elements/CSRF'

import { TOURNAMENT_LEVEL } from '../../config/VarConstants'
import { getNewRefreshToken } from '../hooks/utils'


export const TournamentForm = () => {

    const [tournName, setTournName] = useState<string>('')
    const [tournDate, setTournDate] = useState<string>('')
    const [location, setLocation] = useState<string>('')
    const [eventLevel, setEventLevel] = useState<string>('')
    const [club, setClub] = useState<string>('')
    const [url, setUrl] = useState<string>('')
    const [notes, setNotes] = useState<string>('')

    // Send form to the backend to be processed
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();  // prevents page from reloading.

        await getNewRefreshToken()

        const {data} = await axios.post('api/tournaments/create/', {
            'name': tournName,
            'date': tournDate,
            'event_level': eventLevel,
            club,
            location,
            url,
            notes
        }, {withCredentials: true})
    }

    return(
        <>
            <form onSubmit={submit}>
                
                <h1 className='h1'>New Tournament</h1>

                <CSRF/>
                <FormTextElement setValue={setTournName} elementName='tournament' placeholder='' labelText='Tournament Name'/>
                <FormDateElement setValue={setTournDate} elementName='date' placeholder='' labelText='Date' />
                <FormTextElement setValue={setLocation} elementName='location' placeholder='' labelText='Location'/>
                <FormTextElement setValue={setClub} elementName='host' placeholder='' labelText='Host Club'/>
                <FormSelectElement setValue={setEventLevel} selectOptions={TOURNAMENT_LEVEL} elementName='eventlevel' placeholder='' labelText='Event Level'/>
                <FormTextElement setValue={setUrl} elementName='url' placeholder='' labelText='URL'/>
                <FormTextElement setValue={setNotes} elementName='notes' placeholder='' labelText='Notes'/>

                <button className='submit-button' type='submit'>Add Tournament</button>
            </form>
        </>  
    )}