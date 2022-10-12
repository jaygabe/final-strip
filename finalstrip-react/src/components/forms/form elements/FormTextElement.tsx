import { useState } from 'react'


export const FormTextElement = ({ 
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
    const [className, setClassName]  = useState<string>('')

    function onChange(entry:string) {
        setValue(entry)
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
            />
            <label className={className} htmlFor='nameInput'>{labelText}</label>
        </div>
    )
}