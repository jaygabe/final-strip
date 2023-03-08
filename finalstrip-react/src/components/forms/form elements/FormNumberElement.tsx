import { useState, useEffect } from 'react'


export const FormNumberElement = ({ 
    setValue,
    // placeholder,
    labelText,
    elementName,
    // startingValue
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<number>>,  
        // placeholder: number,
        labelText: string,
        elementName: string,
        // startingValue: string
    }) => {

    
    // keep label from covering the input when filled in
    const [className, setClassName]  = useState<string>('')
    // const [inputValue, setInputValue] = useState<string>(startingValue ? startingValue : '')

    // update the child component if the startingValue changes
    // useEffect(() => { setInputValue(startingValue ? startingValue : '') }, [startingValue]);

    function onChange(entry:number) {
        setValue(entry)
        // setInputValue(entry)
        if (entry != 0) {
            setClassName('jumped')
        }else{
            setClassName('')
        }
    }

    return (
        <div className='form-input'>
            <input 
                id='nameInput' 
                name={elementName}
                type='number' 
                // placeholder={placeholder}
                onChange={e => onChange(e.target.valueAsNumber)}
                // value={inputValue}
            />
            <label className={className} htmlFor='nameInput'>{labelText}</label>
        </div>
    )
}