import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'

import axios from 'axios';

import { eventType, boutType } from '../../../config/VarTypes'



export const Bouts = () => {
    const { eventSlug } = useParams()
    const [event, setEvent] = useState< 
        eventType
    >({
        id: 999,
        slug: '',
        name: '',
        date: '',
        eventLevel: '',
        notes: '',          
    });
    const [bouts, setBouts] = useState<[
        boutType
    ]>([{
        id: 999,
        slug: '',
        winnerIsA: true,
        fencerA: '',
        fencerB: '',
        scoreA: 0,
        scoreB: 0,
        fencerAHand: '',
        fencerBHand: '',
        fencerAYellowCard: true,
        fencerBYellowCard: true,
        fencerARedCard: true,
        fencerBRedCard: true,
        fencerABlackCarded: true,
        fencerBBlackCarded: true,
        fencerAPassivity: true,
        fencerBPassivity: true,
        fencerAMedical: true,
        fencerBMedical: true,
        fencerAVideoUsed: 0,
        fencerBVideoUsed: 0,
        fencerAFootwork: '',
        fencerBFootwork: '',
        fencerABladework: '',
        fencerBBladework: '',
        fencerADistance: '',
        fencerBDistance: '',
        fencerATiming: '',
        fencerBTiming: '',
        fencerAEnergy: '',
        fencerBEnergy: '',
        fencerANotes: '',
        fencerBNotes: '',
        referee: '',
        boutFormat: '',
        round: 0,
        notes: '',
        public: true,
        shareCoach: true,
        deleted: true
    }])

    useEffect(() => {
        const getData = async () => {
            const result = await axios.get('journal/event/' + eventSlug, {withCredentials: true})
            
            setEvent(result.data.event.map((value: any, key: number) => {
                return {
                    id: key,
                    slug: value.slug,
                    name: value.name,
                    date: value.date,
                    eventLevel: value.event_type,
                    notes: value.notes
                }
            }))
            setBouts(result.data.event.map((value: any, key: number) => {
                return {
                    id: key,
                    slug: '',
                    winnerIsA: true,
                    fencerA: '',
                    fencerB: '',
                    scoreA: 0,
                    scoreB: 0,
                    boutFormat: '',
                    round: 0,
                    public: true,
                    shareCoach: true,
                    deleted: true
                }
            })) 
        }
        getData()

    }, []);

    return(
        <>
            <div className='container'>

            </div>
        </>
    )
}