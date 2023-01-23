import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'

import axios from 'axios';

import { eventType, boutType } from '../../constants/VarTypes'



export const Bouts = () => {
    const { eventSlug } = useParams()
    const [dataReceived, setDataReceived] = useState(false)
    const [event, setEvent] = useState<eventType>({
        id: 99,
        slug:'',
        name: '',
        date: '',
        weapon: '',
        eventLevel: '',
        notes: ''
    });
    const [bouts, setBouts] = useState<[boutType] | []>([])

    const getData = async () => {
        if (dataReceived === false) {
            const result = await axios.get('api/events/detail/' + eventSlug, {withCredentials: true})
            console.log('result: ', result.data)
            setDataReceived(true)
            setEvent(result.data)
            setBouts(result.data.bouts.map((value: any, key: number) => {
                return {
                    id: key,
                    slug: value.slug,
                    winnerIsA: value.winner_is_a,
                    fencerA: value.fencer_a,
                    fencerB: value.fencer_b,
                    scoreA: value.score_a,
                    scoreB: value.score_b,
                    fencerAHand: value.fencer__a_hand,
                    fencerBHand: value.fencer_b_hand,
                    fencerAYellowCard: value.fencer_a_yellow_card,
                    fencerBYellowCard: value.fencer_b_yellow_card,
                    fencerARedCard: value.fencer_a_red_card,
                    fencerBRedCard: value.fencer_b_red_card,
                    fencerABlackCarded: value.fencer_a_black_card,
                    fencerBBlackCarded: value.fencer_b_black_card,
                    fencerAPassivity: value.fencer_a_passivity,
                    fencerBPassivity: value.fencer_b_passivity,
                    fencerAMedical: value.fencer_a_medical,
                    fencerBMedical: value.fencer_b_medical,
                    fencerAVideoUsed: value.fencer_a_video_used,
                    fencerBVideoUsed: value.fencer_b_video_used,
                    fencerAFootwork: value.fencer_a_footwork,
                    fencerBFootwork: value.fencer_b_footwork,
                    fencerABladework: value.fencer_a_bladework,
                    fencerBBladework: value.fencer_b_bladework,
                    fencerADistance: value.fencer_a_distance,
                    fencerBDistance: value.fencer_b_distance,
                    fencerATiming: value.fencer_a_timing,
                    fencerBTiming: value.fencer_b_timing,
                    fencerAEnergy: value.fencer_a_energy,
                    fencerBEnergy: value.fencer_b_energy,
                    fencerANotes: value.fencer_a_notes,
                    fencerBNotes: value.fencer_b_notes,
                    referee: value.referee,
                    boutFormat: value.bout_format,
                    round: value.round,
                    notes: value.notes,
                    public: value.public,
                    shareCoach: value.share_coach,
                    deleted: value.deleted
                }
            })) 
        }   
    }
    getData()

    function eventDetail() {     
        return(
            <div className='container'>
                {event.name ? <h1>{event.name}</h1> : <></>}
                {event.date ? <p className="detail">{event.date}</p> : <></>}
                {event.weapon ? <p className="detail">{event.weapon}</p> : <></>}
                {event.eventLevel ? <p className="detail">{event.eventLevel}</p> : <></>}
                {event.notes ? <p className="detail">{event.notes}</p> : <></>}
            </div>
        )
    }

    function boutList(){
        
        if (dataReceived === false){
            return (
                <div className="container">
                    <h1>Loading ... </h1> 
                </div>
            )
        }

        if (bouts.length === 0 && dataReceived === true){
            return <div className="container"><h3>You do not have any bouts yet.  Enter an bout below!</h3></div>
        }

        return (
            Object.entries(bouts).map(([key, value]) => (
                    
                <div key={key} className='container'>
                    <a href={'/journal/bout/' + value.slug}>
                        <h2>{value.fencerA}</h2>
                        <h2>vs.</h2>
                        <h2>{value.fencerB}</h2>
                        
                        <p><b>Score: </b>{value.scoreA} - {value.scoreB}</p>
                    </a>

                    <p><b>Notes:</b></p>
                    <p>{value.notes}</p>
                </div>
            ))
        )
    }

    return(
        <>
            {eventDetail()}
            {boutList()}
            
        </>
    )
}