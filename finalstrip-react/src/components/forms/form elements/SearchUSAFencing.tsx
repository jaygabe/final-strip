import { ChangeEvent, useEffect, useRef, useState, SyntheticEvent} from "react";
import axios from 'axios';

// https://www.makeuseof.com/react-search-bar-filters-data-create/


type searchListTypes = {
    name: string,
    club: string,
    usafid: string
}

export function SearchUSAFencing(){
    const searchRef = useRef<HTMLInputElement>(null);
    const fencerIdRef = useRef<HTMLInputElement>(null);
    const [fencerNames, setFencerNames] = useState<searchListTypes[]>([
        {name:'Doe, John', club:'unattached', usafid: '999999999'}
    ])
    const [searchRequested, setSearchRequested] = useState(false)
    const [searchState, setSearchState] = useState<{
        searchWord: string
        searchList: searchListTypes[]
    }>({
            searchWord: '',
            searchList: [],

    })


    // when the input string is atleast 2 characters long, request the names from the backend
    function handleChange(){
        // const targetValue = e.target.value
        let targetValue = searchRef.current?.value ? searchRef.current?.value : ''

        if(targetValue.length <= 1) setSearchRequested(false)

        if(targetValue.length == 0) {
            setSearchState({
                searchWord: targetValue,
                searchList: []
            })
            return
        }

        // retrieve data from backend
        const getData = async () => {
            if (searchRequested === false && targetValue.length >= 2) {
                axios.get('api/usaf-data/search-members/' + targetValue, {withCredentials: true})
                .then(result => {
                    setSearchRequested(true)
                    console.log('data: ', result.data)
                    setFencerNames(result.data)
                })}
            } 
        getData()
        // this second peice should probably be done with useRef
        // filter names for the search
        const filteredNames = fencerNames.filter(fencer => {
            const searchTerms = targetValue.toLowerCase().split(' ')
            return searchTerms.every(searchTerm =>
                fencer.name.toLowerCase().includes(searchTerm)
        )})

        //set the state to update the list
        setSearchState({
            searchWord: targetValue,
            searchList: filteredNames
        })

        if (filteredNames.length === 1 && fencerIdRef.current){
            fencerIdRef.current.value = filteredNames[0].usafid
        }
    }


    // sets the selected name to the search box
    function handleClick(name: string, id: string){
        if(name != null && searchRef.current && fencerIdRef.current){
            // (document.getElementById('searchUSAFencing') as HTMLInputElement).value = name
            searchRef.current.value = name
            fencerIdRef.current.value = id
            handleChange()            
    }}

    let searchItems    
    if (searchState.searchList.length === 0){ 
        searchItems = <div>Fencer not found</div>}
    else {
        searchItems = searchState.searchWord === '' ? "": searchState.searchList.slice(0,10).map(fencer => {
            return (
                <li key={fencer.usafid}>
                    <div onClick={()=>handleClick(fencer.name, fencer.usafid)}>
                        {fencer.name} - {fencer.club}
                    </div>
                </li>)
        })

        // console.log('id: ', fencerIdRef.current?.value)
    }
    
    const submit = async (e: SyntheticEvent)=>{
        e.preventDefault()
        if (!fencerIdRef.current){
            alert("Error: Please select a name from the list")
            return
        }
        const {data} = await axios.post('/api/fencers/create/', {
            'member_id': fencerIdRef.current?.value
        }, {withCredentials: true})
    }

    return(
        <>           
            <form onSubmit={submit}>
                <label htmlFor="searchUSAFencing">Search USA Fencing:</label>
                <br />
                <input id="searchUSAFencing" type="search" ref={searchRef} className="search-bar" value={searchState.searchWord} onChange={handleChange}/>
                <input id="searchUSAFencingId" type="text" ref={fencerIdRef} className="hidden"/>

                <ul className={searchState.searchWord == '' ? "hidden" : "search-options"}>
                    {searchItems}
                </ul>

                <button className='submit-button' type='submit'>Add Fencer</button>
            </form>
        </>
    )
}