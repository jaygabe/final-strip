import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'

import axios from 'axios';


type eventType = {
    id: number,
    slug: string,
    name: string,
    date: string,
    eventLevel: string,
    notes: string
}

type boutType = {
    id: number
    slug: string
    winnerIsA: boolean
    fencerA: string
    fencerB: string
    scoreA: number,
    scoreB: number,
    fencerAHand: string
    fencerBHand: string
    fencerAYellowCard: boolean
    fencerBYellowCard: boolean
    fencerARedCard: boolean
    fencerBRedCard: boolean
    fencerABlackCarded: boolean
    fencerBBlackCarded: boolean
    fencerAPassivity: boolean
    fencerBPassivity: boolean
    fencerAMedical: boolean
    fencerBMedical: boolean
    fencerAVideoUsed: number
    fencerBVideoUsed: number
    fencerAFootwork: string
    fencerBFootwork: string
    fencerABladework: string
    fencerBBladework: string
    fencerADistance: string
    fencerBDistance: string
    fencerATiming: string
    fencerBTiming: string
    fencerAEnergy: string
    fencerBEnergy: string
    fencerANotes: string
    fencerBNotes: string
    referee: string
    boutFormat: string
    round: number
    notes: string
    public: boolean
    shareCoach: boolean
    deleted: boolean
}

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
            
            setEvent(result.data.event)
            setBouts(result.data.bouts.map((value: any, key: number) => {
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

            </div>
        </>
    )
}