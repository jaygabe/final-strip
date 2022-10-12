import { useState } from 'react'

export const FormDateElement = ({ 
    setValue,
    placeholder,
    labelText,
    elementName
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<string>>,  
        placeholder: string,
        labelText: string,
        elementName: string
    }) => {
    
    
    // keep label from covering the input when filled in
    // also keeps the text black when date is entered
    const [className, setClassName]  = useState<string>('')

    function onChange(entry:string) {
        setValue(entry)
        if (entry != '') {
            setClassName('jumped')
        }else{
            setClassName('')
        }
    }    

    return(
        <div className='form-input'>
            <input 
                id='dateInput'
                name={elementName}
                type='date' 
                className={className}
                placeholder={placeholder}
                onChange={e => onChange(e.target.value)}
            />
            <label className={className} htmlFor='dateInput'>{labelText}</label>
        </div>
    )
}