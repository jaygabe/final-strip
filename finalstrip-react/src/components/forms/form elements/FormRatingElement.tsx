import { useState } from 'react';

export function FormRatingElement({
        setValue,
        labelText,
        elementName
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<string>>,  
        labelText: string,
        elementName: string
    }) {

    const [rating, setRating] = useState(0);
    const [ratingText, setRatingText] = useState('none');
    const [hover, setHover] = useState(0);
    
    const ratingObject: {
        [key: number]: string;
    } = {
        0: 'none',
        1: 'poor',
        2: 'fair',
        3: 'good',
        4: 'great',
        5: 'excellent',
    }
  
    function onClick(entry: number): void {
        setValue(ratingObject[entry])
        setRating(entry)
        setRatingText(ratingObject[entry])
    }

    function onReset(){
        setRating(0)
        setRatingText('none')
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
                        className={index <= (hover || rating) ? "rating-button active" : "rating-button inactive"}
                        onClick={() => onClick(index)}
                        onMouseEnter={() => setHover(index)}
                        onMouseLeave={() => setHover(rating)}
                    >       
                        <div className='star' />
                    </button> 
                )
            })}
            <button className='reset-rating' onClick={onReset}>reset</button>
        </div>
    </div>
     
    )
}