import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"

import axios from 'axios';

import { EventForm } from "../../forms/EventForm";

type tournamentType = {
    id: number
    slug: string
    name: string
    date?: string
    location?: string
}

type eventType = {
    id: number,
    slug: string,
    name: string,
    date: string,
    eventLevel: string,
    notes: string
}



export const Events = () => {

    const { tournamentSlug } = useParams()
    const [tournament, setTournament] = useState< 
        tournamentType
    >({
        id: 999,
        slug: '',
        name: '',
        date: '',
        location: ''          
    });
    const [events, setEvents] = useState<[ 
        eventType
    ]>([{
        id: 999,
        slug: '',
        name: '',
        date: '',
        eventLevel: '',
        notes: ''          
    }]);


    useEffect(() => {
        const getData = async () => {
            const result = await axios.get('journal/tournament/' + tournamentSlug, {withCredentials: true})
            
            setTournament(result.data.tournament)
            setEvents(result.data.events.map((value: any, key: number) => {
                return {
                    id: key,
                    slug: value.slug,
                    name: value.name,
                    date: value.date,
                    eventLevel: value.event_type,
                    notes: value.notes
                }
            })) 
        }
        getData()

    }, []);

    return(
        <>
            <div className='container'>
                <h1>{tournament.name}</h1>
                <h4 className='test'>{tournamentSlug}</h4>
            </div>

            {Object.entries(events).map(([key, value]) => (
                
                <div key={key} className='container'>
                    <a href={'/journal/events/' + value.slug}>
                        <h2>{value.name}</h2>
                        
                        <p><b>Date: </b>{ value.date}</p>
                    </a>
                    <p><b>Event Type: </b>{value.eventLevel}</p>
                    <p><b>Notes:</b></p>
                    <p>{value.notes}</p>
                </div>
            ))}

            <div className='container'>
                <EventForm/>
            </div>
            
        </>
    )
}