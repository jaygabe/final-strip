import {useState} from 'react';
import axios from 'axios';
import { TournamentForm } from "../../forms/TournamentForm";


export const Tournaments = () => {

    const [dataReceived, setDataReceived] = useState<boolean>(false)
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


    if (dataReceived === false) {
        
        const getData = async () => {
            const result = await axios.get('api/tournaments/all', {withCredentials: true, })
            console.log(result)
            setTournaments(result.data)
            setDataReceived(true)
        }
    
        getData()
    }


    return(
        <>
            {Object.entries(tournaments).map(([key, value]) => (
                <div key={key} className='container'>
                    <a href={'/journal/events/' + value.slug}>
                        <h2>{value.name}</h2>
                        <p><b>Date: </b>{ value.date}</p>
                        <p><b>Location: </b>{value.location}</p>
                    </a>
                </div>
            ))}

            <br />
            
            <div className='container'>
                <TournamentForm />
            </div>
            
        </>
    )
}