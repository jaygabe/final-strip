import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"

import axios from 'axios';

import { EventForm } from "../../components/forms/EventForm";
import { tournamentType, eventType } from "../../constants/VarTypes";
import { useConfirmAuth } from "../../hooks/utils";


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
            const result = await axios.get('api/tournaments/detail/' + tournamentSlug, {withCredentials: true})
                setDataReceived(true)
                setTournament(result.data)
                console.log('data: ', result.data)
                setEvents(result.data.events.map((value: any, key: number) => {
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

    // this was giving me a state warning before but seems better now... be suspicious
    // hopefully use Query is better by the time I have to fix this 
    useConfirmAuth(dataReceived)
    

    function tournamentDetail() {     
        return(
            <div className='container'>
                {tournament.name ? <h1>{tournament.name}</h1> : <></>}
                {tournament.location ? <p className="detail">{tournament.location}</p> : <></>}
                {tournament.date ? <p className="detail">{tournament.date}</p> : <></>}
                {tournament.url ? <p className="detail">{tournament.url}</p> : <></>}
                {tournament.notes ? <p className="detail">{tournament.notes}</p> : <></>}
            </div>
        )
    }

    function eventList(){
        
        if (dataReceived === false){
            return (
                <div className="container">
                    <h1>Loading ... </h1> 
                </div>
            )
        }

        if (events.length === 0 && dataReceived === true){
            return <div className="container"><h3>You do not have any events yet.  Enter an event below!</h3></div>
        }

        return (
            Object.entries(events).map(([key, value]) => (
                    
                <div key={key} className='container'>
                    <a href={'/journal/bouts/' + value.slug}>
                        <h2>{value.name}</h2>
                        
                        <p><b>Date: </b>{ value.date}</p>
                    </a>
                    <p><b>Event Type: </b>{value.eventLevel}</p>
                    <p><b>Notes:</b></p>
                    <p>{value.notes}</p>
                </div>
            ))
        )
    }


    return(
        <>
            {tournamentDetail()}

            {eventList()}

            <div className='container'>
                <EventForm/>
            </div>
            
        </>
    )
}