import { SyntheticEvent, useState } from "react"


export const FormTextElement = ({ 
    setValue,
    labelText
    }:{ 
        setValue: React.Dispatch<React.SetStateAction<string>>,  
        labelText: string
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
            <input type='text' id='nameInput' placeholder=''
                onChange={e => onChange(e.target.value)}
            />
            <label className={className} htmlFor='nameInput'>{labelText}</label>
        </div>
    )
}