import {useState, SyntheticEvent, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { FormTextElement } from './form elements/FormTextElement';
import { FormNumberElement } from './form elements/FormNumberElement';
import { FormRatingElement } from './form elements/FormRatingElement';
import { FormSelectElement } from './form elements/FormSelectElement';
import { FormCheckBoxElement } from './form elements/FormCheckBoxElement';
import { DialogBox } from '../DialogBox';
import { HAND_CHOICES, SHAREABLE_CHOICES } from '../../constants/VarOptions';
import { fencerListType } from '../../constants/VarTypes';
import { CSRF } from './form elements/CSRF';
import { getNewRefreshToken} from '../../hooks/utils';
import { ReactComponent as EditIcon } from "../../static/edit_icon.svg"


export function BoutForm (props: {fencerList: fencerListType}){

    const {eventSlug} = useParams()
    const [winnerIsA, setWinnerIsA] = useState<null | boolean>(null)
    const [fencerA, setFencerA] = useState('')
    const [scoreA, setScoreA] = useState<number | null>(null)
    const [fencerAHand, setFencerAHand] = useState('')
    const [fencerAYellowCard, setFencerAYellowCard] = useState(false)
    const [fencerARedCard, setFencerARedCard] = useState(false)
    const [fencerABlackCard, setFencerABlackCard] = useState(false)
    const [fencerAPassivity, setFencerAPassivity] = useState(false)
    const [fencerAMedical, setFencerAMedical] = useState(false)
    const [fencerAVideoUsed, setFencerAVideoUsed] = useState<number | null>(0)
    const [fencerAFootwork, setFencerAFootwork] = useState(0)
    const [fencerABladework, setFencerABladework] = useState(0)
    const [fencerATiming, setFencerATiming] = useState(0)
    const [fencerADistance, setFencerADistance] = useState(0)
    const [fencerAEnergy, setFencerAEnergy] = useState(0)
    const [fencerANotes, setFencerANotes] = useState('')

    const [fencerB, setFencerB] = useState('')
    const [scoreB, setScoreB] = useState<number | null>(null)
    const [fencerBHand, setFencerBHand] = useState('')
    const [fencerBYellowCard, setFencerBYellowCard] = useState(false)
    const [fencerBRedCard, setFencerBRedCard] = useState(false)
    const [fencerBBlackCard, setFencerBBlackCard] = useState(false)
    const [fencerBPassivity, setFencerBPassivity] = useState(false)
    const [fencerBMedical, setFencerBMedical] = useState(false)
    const [fencerBVideoUsed, setFencerBVideoUsed] = useState<number | null>(0)
    const [fencerBFootwork, setFencerBFootwork] = useState(0)
    const [fencerBBladework, setFencerBBladework] = useState(0)
    const [fencerBTiming, setFencerBTiming] = useState(0)
    const [fencerBDistance, setFencerBDistance] = useState(0)
    const [fencerBEnergy, setFencerBEnergy] = useState(0)
    const [fencerBNotes, setFencerBNotes] = useState('')

    const [referee, setReferee] = useState('')
    const [round, setRound] = useState<number | null>(0)
    const [boutNotes, setBoutNotes] = useState('')
    const [boutFormat, setBoutFormat] = useState('')
    const [sharable, setShareable] = useState('')
    
    const [showDialogBox, setShowDialogBox] = useState(false)
    const [fencerOptions, setFencerOptions] = useState<fencerListType>({'999':'Error: No Fencers Found', '998':'Error: No Fencers Found'})

    useEffect(() => {  
        console.log('props: ', props.fencerList)    
        setFencerOptions(props.fencerList)
    },[props])
    // async function getFencers(){
    //     const {data} = await axios.get('/api/fencers/all')
    //     const processData = (data: any) => {
    //         setFencerOptions(data.response.map((fencer: any) => {
    //             return {
    //                 [fencer.slug]: fencer.first_name +', '+ fencer.last_name
    //         }}))
    //     }
    // }
    // getFencers()

    async function  sendData(){
        await getNewRefreshToken()
        const {data} = await axios.post('api/bouts/create/', {
            'event': eventSlug,
            'winner_is_a': winnerIsA,
            'fencer_a': fencerA,
            'score_a': scoreA,
            'fencer_a_hand': fencerAHand,
            'fencer_a_yellow_card': fencerAYellowCard,
            'fencer_a_red_card': fencerARedCard,
            'fencer_a_black_card': fencerABlackCard,
            'fencer_a_passivity': fencerAPassivity,
            'fencer_a_medical': fencerAMedical,
            'fencer_a_video_used': fencerAVideoUsed,
            'fencer_a_footwork': fencerAFootwork,
            'fencer_a_bladework': fencerABladework,
            'fencer_a_timing': fencerATiming,
            'fencer_a_distance': fencerADistance,
            'fencer_a_energy': fencerAEnergy,
            'fencer_a_notes': fencerANotes,
            'fencer_b': fencerB,
            'score_b': scoreB,
            'fencer_b_hand': fencerBHand,
            'fencer_b_yellow_card': fencerBYellowCard,
            'fencer_b_red_card': fencerBRedCard,
            'fencer_b_black_card': fencerBBlackCard,
            'fencer_b_passivity': fencerBPassivity,
            'fencer_b_medical': fencerBMedical,
            'fencer_b_video_used': fencerBVideoUsed,
            'fencer_b_footwork': fencerBFootwork,
            'fencer_b_bladework': fencerBBladework,
            'fencer_b_timing': fencerBTiming,
            'fencer_b_distance': fencerBDistance,
            'fencer_b_energy': fencerBEnergy,
            'fencer_b_notes': fencerBNotes,
            'referee': referee,
            'round': round,
            'bout_notes': boutNotes,
            'bout_format': boutFormat,
            'sharable': sharable,
    }, {withCredentials: true})}

    // Preprocess before submitting
    const handleClick = () => {
        // e.preventDefault();  // prevents page from reloading.
        console.log('submitting...')
        console.log('A: ', scoreA)
        console.log('B: ', scoreB)

        if (scoreA == null || scoreB == null){
            alert("score is required")
            return
        }
        // assign winner
        if (scoreA > scoreB){
            setWinnerIsA(true)
        }
        if (scoreA < scoreB){
            console.log('setting winnerIsA to false')
            setWinnerIsA(false)
        }
        console.log('scoreA = scoreB: ', scoreA, scoreB)
        console.log('winnerIsA: ', winnerIsA)
        if (scoreA == scoreB && winnerIsA === null){
            setShowDialogBox(true)
            console.log('setting showDialogBox: ', showDialogBox)
            return
        }

        console.log('sending data to backend...')
        sendData() 
    }

    function fencerADetail(){
        return(
            <section className="bout-tab-content">     
                <h2>Fencer A</h2>
                <FormSelectElement setValue={setFencerA} placeholder='' elementName='fencer-a' labelText='Select Fencer' selectOptions={fencerOptions}/>
                <FormNumberElement setValue={setScoreA} elementName='score-a' labelText='Score A'/>
                <FormSelectElement setValue={setFencerAHand} placeholder='' elementName='fencer-a-hand' labelText='Select Hand' selectOptions={HAND_CHOICES}/>               
                <FormNumberElement setValue={setFencerAVideoUsed} elementName='fencer-a-video-used' labelText='Fencer A Video Used'/>
                <FormCheckBoxElement setValue={setFencerAMedical} labelText='Fencer A Medical Timeout'/>
                <FormTextElement setValue={setFencerANotes} elementName='fencer-a-notes' placeholder='' labelText='Fencer A Notes'/>
            
                <h2>Cards:</h2>
                <FormCheckBoxElement setValue={setFencerAYellowCard} labelText='Fencer A Yellow Card'/>
                <FormCheckBoxElement setValue={setFencerARedCard}  labelText='Fencer A Red Card'/>
                <FormCheckBoxElement setValue={setFencerABlackCard} labelText='Fencer A Black Card'/>
                <FormCheckBoxElement setValue={setFencerAPassivity} labelText='Fencer A Passivity'/>
                
                <h2>Fencer Ratings:</h2>
                <FormRatingElement setValue={setFencerAFootwork} labelText='Fencer A Footwork'/>
                <FormRatingElement setValue={setFencerABladework} labelText='Fencer A Bladework'/>
                <FormRatingElement setValue={setFencerATiming} labelText='Fencer A Timing'/>
                <FormRatingElement setValue={setFencerADistance} labelText='Fencer A Distance'/>
                <FormRatingElement setValue={setFencerAEnergy} labelText='Fencer A Energy'/>   
            </section>
    )}

    function fencerBDetail(){
        return(
            <section className="bout-tab-content">
                <h2>Fencer B</h2>
                <FormSelectElement setValue={setFencerB} placeholder='' elementName='fencer-b' labelText='Select Fencer' selectOptions={fencerOptions}/>
                <FormNumberElement setValue={setScoreB} elementName='score-b' labelText='Score B'/>
                <FormSelectElement setValue={setFencerBHand} placeholder='' elementName='fencer-b-hand' labelText='Select Hand' selectOptions={HAND_CHOICES}/>               
                <FormNumberElement setValue={setFencerBVideoUsed} elementName='fencer-b-video-used' labelText='Fencer B Video Used'/>
                <FormCheckBoxElement setValue={setFencerBMedical} labelText='Fencer B Medical Timeout'/>
                <FormTextElement setValue={setFencerBNotes} elementName='fencer-b-notes' placeholder='' labelText='Fencer B Notes'/>

                <h2>Cards:</h2>
                <FormCheckBoxElement setValue={setFencerBYellowCard} labelText='Fencer B Yellow Card'/>
                <FormCheckBoxElement setValue={setFencerBRedCard}  labelText='Fencer B Red Card'/>
                <FormCheckBoxElement setValue={setFencerBBlackCard} labelText='Fencer B Black Card'/>
                <FormCheckBoxElement setValue={setFencerBPassivity} labelText='Fencer B Passivity'/>
                
                <h2>Fencer Ratings:</h2>
                <FormRatingElement setValue={setFencerBFootwork} labelText='Fencer B Footwork'/>
                <FormRatingElement setValue={setFencerBBladework} labelText='Fencer B Bladework'/>
                <FormRatingElement setValue={setFencerBTiming} labelText='Fencer B Timing'/>
                <FormRatingElement setValue={setFencerBDistance} labelText='Fencer B Distance'/>
                <FormRatingElement setValue={setFencerBEnergy} labelText='Fencer B Energy'/>
            </section>
    )}

    function boutOverallDetail(){
        return(
            <section className="bout-tab-content">
                <h2>Overall Data: </h2>              
                <FormNumberElement setValue={setRound} elementName='round' labelText='Round'/>
                <FormSelectElement setValue={setBoutFormat} placeholder='' elementName='bout-format' labelText='Bout Format' selectOptions={HAND_CHOICES}/>               
                <FormTextElement setValue={setReferee} elementName='referee' placeholder='' labelText='Referee'/>
                <FormTextElement setValue={setBoutNotes} elementName='bout-notes' placeholder='' labelText='Overall Notes'/>
                <FormSelectElement setValue={setShareable} placeholder='' elementName='shareable' labelText='Shareable' selectOptions={SHAREABLE_CHOICES}/>
            </section>
    )}

    return(
        <>
            {showDialogBox ? (
                <DialogBox
                    title={'Tied Score'}
                    message={'Please select a winner.'}
                    textActionA={'Player A'}
                    textActionB={'Player B'}
                    actionA={() => setWinnerIsA(true)}
                    actionB={() => setWinnerIsA(false)}
                    cancelAction={() => setShowDialogBox(false)}
                    submit={sendData}
                />
            ) : null}          
            <form>
                <h1 className='h1'>New Bout</h1>
                <CSRF/>
                <div className="bout-tabs">
                    <input className='bout-tab-radio' type="radio" id="overall" name="bout-info" defaultChecked/>
                    <label className='bout-tab-radio' htmlFor="overall"><EditIcon/><br/><span>Overall</span></label>
                    {boutOverallDetail()}

                    <input className='bout-tab-radio' type="radio" id="fencer-a" name="bout-info" />
                    <label className='bout-tab-radio' htmlFor="fencer-a"><EditIcon/><br/><span>Fencer A</span></label>
                    {fencerADetail()}

                    <input className='bout-tab-radio' type="radio" id="fencer-b" name="bout-info" />
                    <label className='bout-tab-radio' htmlFor="fencer-b"><EditIcon/><br/><span>Fencer B</span></label>
                    {fencerBDetail()}
                </div>        
                <button className='submit-button' type='button' onClick={() => handleClick()}>Add Bout</button>
                <button type='button' onClick={()=>setWinnerIsA(null)}>reset winner_is_a</button>
            </form>
        </>  
    )}