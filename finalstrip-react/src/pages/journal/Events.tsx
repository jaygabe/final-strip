import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"

import axios from 'axios';

import { EventForm } from "../../components/forms/EventForm";
import { tournamentType, eventType } from "../../constants/VarTypes";


export const Events = () => {

    const [dataReceived, setDataReceived] = useState<boolean>(false)
    const { tournamentSlug } = useParams()
    const [tournament, setTournament] = useState<tournamentType>({
        'id':99,
        'slug': '',
        'name': '',
        'location': '',
        'date': '',
        'url': '',
        'notes': ''
    });
    const [events, setEvents] = useState<[eventType] | []>([]);

    const getData = async () => {
        if (dataReceived === false) {
            const result = await axios.get('api/events/all/' + tournamentSlug, {withCredentials: true})
            setDataReceived(true)
            setTournament(result.data[0].tourn_info)
            console.log('data: ', result.data)
            setEvents(result.data.map((value: any, key: number) => {
                return {
                    id: key,
                    slug: value.slug,
                    name: value.name,
                    date: value.date,
                    weapon: value.weapon,
                    eventLevel: value.event_type,
                    notes: value.notes
                }
            }))
        }
        
        
    }
    getData()

    const tournamentDetail = () => {
        
        return(
            <div className='container'>
                {tournament.name ? <h1>{tournament.name}</h1> : <></>}
                {tournament.location ? <p className="detail">{tournament.location}</p> : <></>}
                {tournament.date ? <p className="detail">{tournament.date}</p> : <></>}
                {tournament.url ? <p className="detail">{tournament.url}</p> : <></>}
                {tournament.notes ? <p className="detail">{tournament.notes}</p> : <></>}

                <h4 className='test'>{tournamentSlug}</h4>
            </div>
        )
    }


    return(
        <>
            {tournamentDetail()}

            {Object.entries(events).map(([key, value]) => (
                
                <div key={key} className='container'>
                    <a href={'/journal/bouts/' + value.slug}>
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