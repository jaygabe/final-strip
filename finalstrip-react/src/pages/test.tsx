import CSS from 'csstype'
import { useState } from 'react';
import { FormRatingElement } from '../components/forms/form elements/FormRatingElement';
import { FormTextElement } from '../components/forms/form elements/FormTextElement';


export function Test() {

    const [rating, setRating] = useState(0);
    const [hover, setHover] = useState(0);
    
    const [something, setSomething] = useState('')

    return (
    
    <> 
        <div className='container'>
          <FormTextElement setValue={setSomething} elementName='tournament' placeholder='' labelText='Tournament Name'/>
          <FormRatingElement setValue={setSomething} elementName='tournament' labelText='Tournament Name'/>

        </div>

        <br />

        <div className="container">
          <div className='rating test'>
            <button className="rating-button active"><div className="star"/></button>
            <button className="rating-button inactive"><div className="star"/></button>
            <button className="rating-button inactive"><div className="star"/></button>
          </div>
        </div>
        
    </>
    )
}