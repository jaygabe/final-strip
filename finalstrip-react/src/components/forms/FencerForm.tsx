import {useState, SyntheticEvent, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
// import { SearchUSAFencing } from './form elements/SearchUSAFencing';
import { SearchUSAFencing } from './form elements/SearchUSAFencing';
import { FormTextElement } from './form elements/FormTextElement';
import { FormRatingElement } from './form elements/FormRatingElement';
import { FormSelectElement } from './form elements/FormSelectElement';
import { RATING_NUMBER_CHOICES, REGION_CHOICES, HAND_CHOICES, GRIP_CHOICES, REF_RATING_CHOICES, USAF_RATING_CHOICES } from '../../constants/VarOptions';
import { CSRF } from './form elements/CSRF';
import { getNewRefreshToken} from '../../hooks/utils';


export const FencerForm = () => {

    const [usaFencingInfo, setUSAFencingInfo] = useState<string>('')
    const [firstName, setFirstName] = useState<string>('')
    const [lastName, setLastName] = useState<string>('')
    const [club, setClub] = useState<string>('')
    const [club2, setClub2] = useState<string>('')
    const [school, setSchool] = useState<string>('')
    const [division, setDivision] = useState<string>('')
    const [region, setRegion] = useState<string>('')
    const [nationality, setNationality] = useState<string>('')
    const [handed, setHanded] = useState<string>('')
    const [grip, setGrip] = useState<string>('')
    const [ratingEpee, setRatingEpee] = useState<string>('')
    const [ratingSabre, setRatingSabre] = useState<string>('')
    const [ratingFoil, setRatingFoil] = useState<string>('')
    const [refRatingEpee, setRefRatingEpee] = useState<string>('')
    const [refRatingSabre, setRefRatingSabre] = useState<string>('')
    const [refRatingFoil, setRefRatingFoil] = useState<string>('')
    const [customRating, setcustomRating] = useState<string>('')
    const [timing, setTiming] = useState<string>('')
    const [distance, setDistance] = useState<string>('')
    const [footwork, setFootwork] = useState<string>('')
    const [bladework, setBladework] = useState<string>('')
    const [endurance, setEndurance] = useState<string>('')
    const [strength, setStrength] = useState<string>('')
    const [tacticDescript, setTacticDescript] = useState<string>('')
    const [favActions, setFavActions] = useState<string>('')
    const [notes, setNotes] = useState<string>('')

    // Send form to the backend to be processed
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault()  // prevents page from reloading.
        
        await getNewRefreshToken()

        const {data} = await axios.post('/api/fencers/create/', {

            'first_name': firstName,
            'last_name': lastName,
            club,
            club2,
            school,
            division,
            region,
            nationality,
            handed,
            'primary_grip': grip,
            'usaf_rating_epee': ratingEpee,
            'usaf_rating_sabre': ratingSabre,
            'usaf_rating_foil': ratingFoil,
            'ref_rating_epee': refRatingEpee,
            'ref_rating_sabre': refRatingSabre,
            'ref_rating_foil': refRatingFoil,
            'custom_rating': customRating,
            'tactical_description': tacticDescript,
            'favorite_actions': favActions,
            notes,
            
        }, {withCredentials: true})
    }

    
    let [x, setX] = useState('untest')
    function test(){
        if (x === 'untest'){
            x = 'testing'
        }else{
            x = 'untest'
        }
        console.log('triggered')
        console.log('x is now: ', x)
    }
    
    return(
        <>
            <h1 className='h1'>New Fencer</h1>
            <br />
            <SearchUSAFencing />
            <hr />
            <p>or</p>
            <h1>Custom Profile</h1>
            <br />
            <form onSubmit={submit}>
                <CSRF/>
                <FormTextElement setValue={setFirstName} elementName='first' placeholder='' labelText='First Name'/>
                <FormTextElement setValue={setLastName} elementName='last' placeholder='' labelText='Last Name'/>
                <FormSelectElement setValue={setHanded} elementName='handed' selectOptions={HAND_CHOICES} placeholder='' labelText='Handedness' />
                <FormSelectElement setValue={setGrip} elementName='grip' selectOptions={GRIP_CHOICES} placeholder='' labelText='Grip Preference' />
                <FormTextElement setValue={setClub} elementName='club' placeholder='' labelText='Club'/>
                <FormTextElement setValue={setClub2} elementName='club2' placeholder='' labelText='Secondary Club'/>
                <FormTextElement setValue={setSchool} elementName='school' placeholder='' labelText='School'/>
                <FormTextElement setValue={setDivision} elementName='division' placeholder='' labelText='Division'/>
                <FormSelectElement setValue={setRegion} elementName='region' selectOptions={REGION_CHOICES} placeholder='' labelText='Region' />
                <FormTextElement setValue={setNationality} elementName='nationality' placeholder='' labelText='Nationality'/>
                <FormSelectElement setValue={setRatingEpee} elementName='ratingEpee' selectOptions={USAF_RATING_CHOICES} placeholder='' labelText='Epee Rating'/>
                <FormSelectElement setValue={setRatingSabre} elementName='ratingSabre' selectOptions={USAF_RATING_CHOICES} placeholder='' labelText='Sabre Rating'/>
                <FormSelectElement setValue={setRatingFoil} elementName='ratingFoil' selectOptions={USAF_RATING_CHOICES} placeholder='' labelText='Foil Rating'/>
                <FormSelectElement setValue={setRefRatingEpee} elementName='refRatingEpee' selectOptions={REF_RATING_CHOICES} placeholder='' labelText='Epee Referee Rating'/>
                <FormSelectElement setValue={setRefRatingSabre} elementName='refRatingSabre' selectOptions={REF_RATING_CHOICES} placeholder='' labelText='Sabre Referee Rating'/>
                <FormSelectElement setValue={setRefRatingFoil} elementName='refRatingFoil' selectOptions={REF_RATING_CHOICES} placeholder='' labelText='Foil Referee Rating'/>
                <FormTextElement setValue={setcustomRating} elementName='customRating' placeholder='' labelText='Custom Rating'/>
                {/* <FormRatingElement setValue={setTiming} elementName='timing' labelText='Timing'/>
                <FormRatingElement setValue={setDistance} elementName='distance' labelText='Distance'/>
                <FormRatingElement setValue={setFootwork} elementName='footwork' labelText='Footwork' />
                <FormRatingElement setValue={setBladework} elementName='bladework' labelText='Bladework' />
                <FormRatingElement setValue={setStrength} elementName='strength' labelText='Strength' /> */}
                <FormTextElement setValue={setTacticDescript} elementName='tacticalDescription' placeholder='' labelText='Tactical Description'/>
                <FormTextElement setValue={setFavActions} elementName='favActions' placeholder='' labelText='Favorite Actions'/>
                <FormTextElement setValue={setNotes} elementName='notes' placeholder='' labelText='Notes'/>

                <button className='submit-button' type='submit'>Add Fencer</button>
            </form>
        </>  
    )}