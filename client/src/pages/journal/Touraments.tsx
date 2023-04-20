import {useEffect, useState} from 'react'
import axios from 'axios'
import { TournamentForm } from "../../components/forms/TournamentForm"
import { tournamentType } from '../../constants/VarTypes'


export const Tournaments = () => {

    const [dataReceived, setDataReceived] = useState<boolean>(false)
    const [tournaments, setTournaments] = useState<[tournamentType] | []>([])
    const [previousPage, setPreviousPage] = useState<string>('')
    const [currentPage, setCurrentPage] = useState<string>('api/tournaments/all')
    const [nextPage, setNextPage] = useState<string>('')


    function getData(data_url:string){
        // gets data from api
        // not sure why dataReceived prevents infinite loop
        if (dataReceived === false) {  
            (async () => {
                const result = await axios.get(data_url, {withCredentials: true, })
                setTournaments(result.data.results)
                setDataReceived(true)
                setPreviousPage(result.data.previous)
                setNextPage(result.data.next)
    
            })()
        }
    }
    getData(currentPage)


    function goToNextPage() {
        console.log('next')
        setCurrentPage(nextPage)
        setDataReceived(false)
        getData(currentPage)
        window.scrollTo(0, 0)
    }

    function goToPreviousPage() {
        console.log('previous')
        setCurrentPage(previousPage)
        setDataReceived(false)
        getData(currentPage)
        window.scrollTo(0, 0)
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

            {tournaments.length === 0 && (
                <div className='container'><h1>You do not have any tournaments</h1></div>
            )}
            
            <div className='pagination-buttons'>
                <button className={previousPage ? 'previous-button' : 'hidden'} onClick={() => goToPreviousPage()}>Previous</button>
                <button className={nextPage ? 'next-button' : 'hidden'} onClick={() => goToNextPage()}>Next</button>
            </div>
            
            <div className='container'>
                <TournamentForm />
            </div>
            
        </>
    )
}