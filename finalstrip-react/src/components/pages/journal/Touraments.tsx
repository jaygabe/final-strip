import axios from 'axios';
import {useEffect, useState} from 'react';


import { TournamentForm } from "../../forms/TournamentForm";


export const Tournaments = () => {

    const [tournaments, setTournaments] = useState<[{ 
            id: number
            slug: string
            name: string
            date?: string
            location?: string
        }]>([{
            id: 999,
            slug: '',
            name: '',
            date: '',
            location: '',
        }]);
        

    useEffect(() => {
        const getData = async () => {
            const result = await axios.get('journal/tournament', {withCredentials: true})
            setTournaments(result.data)
        }

        getData()

    }, []);

    const convertDateFormat = (date: string) => {
        console.log('date: ', date)
        let newDate = date.split('-')

        console.log(newDate)
        return newDate
    }


    return(
        <>
            {Object.entries(tournaments).map(([key, value]) => (
                <div key={key} className='container'>
                    <a href={'journal/tournaments/' && value.slug}>
                        <h2>{value.name}</h2>
                        <p><b>Date: </b>{ value.date}</p>
                        <p><b>Location: </b>{value.location}</p>
                    </a>
                </div>
            ))}

            <br />
            
            <TournamentForm />
        </>
    )
}