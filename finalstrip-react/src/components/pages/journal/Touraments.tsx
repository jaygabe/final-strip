import axios from 'axios';
import { stringify } from 'querystring';
import {useEffect, useState} from 'react';


export const Tournaments = () => {

    const [tournaments, setTournaments] = useState([{
            id: 99,
            slug: '',
            name: '',
            time: '',
            location: '',
        }])
        

    useEffect(() => {
        const getData = async () => {
            const result = await axios.get('journal/tournament', {withCredentials: true})
            setTournaments(result.data)
        }
        getData()
        // const data = promise.then((response) => response.data)
        console.log(tournaments)
        
    }, []);

     

    return(
        <>
            <head>
                <title>Tournaments</title>
            </head>

            <h1>
                Tournaments
            </h1>

            {Object.entries(tournaments).map(([key, value]) => (
                <div className='container'>
                    <a href={'journal/tournaments/' && value.slug}> {/*this might be wrong*/}
                        <h2>{value.name}</h2>
                        <p><b>Date: </b>{value.time}</p>
                        <p><b>Location: </b>{value.location}</p>
                    </a>
                </div>
      ))}
        </>
    )
}