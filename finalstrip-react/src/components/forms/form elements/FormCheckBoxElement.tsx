import { useState, useEffect } from 'react'


export const FormCheckBoxElement = ({ 
    setValue,
    labelText,
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<boolean>>,  
        labelText: string,
    }) => {

    const [isChecked, setIsChecked] = useState(false)

    const checkHandler = () => {
        setIsChecked(!isChecked)
        setValue(isChecked)
    }

    return (
        <div className="container">
            <label className="toggle">
                <span className="toggle-label">{labelText}</span>
                <input className="toggle-checkbox" 
                    type="checkbox" 
                    checked={isChecked}
                    onChange={checkHandler}/>
                <div className="toggle-switch" />	
            </label>
        </div>
    )
}