import { useState, useEffect } from 'react'


export const FormTextElement = ({ 
    setValue,
    placeholder,
    labelText,
    elementName,
    // startingValue
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<string>>,  
        placeholder: string,
        labelText: string,
        elementName: string,
        // startingValue: string
    }) => {

    
    // keep label from covering the input when filled in
    const [className, setClassName]  = useState<string>('')
    // const [inputValue, setInputValue] = useState<string>(startingValue ? startingValue : '')

    // update the child component if the startingValue changes
    // useEffect(() => { setInputValue(startingValue ? startingValue : '') }, [startingValue]);

    function onChange(entry:string) {
        setValue(entry)
        // setInputValue(entry)
        if (entry != '') {
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
                type='text' 
                placeholder={placeholder}
                onChange={e => onChange(e.target.value)}
                // value={inputValue}
            />
            <label className={className} htmlFor='nameInput'>{labelText}</label>
        </div>
    )
}