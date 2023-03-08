import { useState } from 'react';

export function FormRatingElement({
        setValue,
        labelText,
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<number>>,  
        labelText: string,
    }) {

    const [rating, setRating] = useState(0);
    const [ratingText, setRatingText] = useState('None');
    const [hover, setHover] = useState(0);
    
    const ratingObject: {
        [key: number]: string;
    } = {
        0: 'None',
        1: 'Poor',
        2: 'Fair',
        3: 'Good',
        4: 'Great',
        5: 'Excellent',
    }
  
    function onClick(entry: number): void {
        setValue(entry)
        setRating(entry)
        setRatingText(ratingObject[entry])
    }

    function onReset(){
        setRating(0)
        setRatingText('None')
        setHover(0)
    }
 

    return (
    <div>
        <div className='rating-label'>{labelText}: {ratingText}</div>
        <div className="rating">
            {[...Array(5)].map((star, index) => {
            index += 1;
                return (  
                    <button 
                        key={index}
                        type='button'
                        className={index <= (hover || rating) ? "rating-button active" : "rating-button inactive"}
                        onClick={() => onClick(index)}
                        onMouseEnter={() => setHover(index)}
                        onMouseLeave={() => setHover(rating)}
                    >       
                        <div className='star' />
                    </button> 
                )
            })}
            <button type='button' className='reset-rating' onClick={onReset}>reset</button>
        </div>
    </div>
     
    )
}