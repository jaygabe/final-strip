import { useState } from 'react'


export const FormSelectElement = ({
    setValue,
    placeholder,
    labelText,
    elementName,
    selectOptions
    }:{ 
    setValue: React.Dispatch<React.SetStateAction<string>>,  
    placeholder: string,
    labelText: string,
    elementName: string,
    selectOptions: { [key: string]: string}
}) => {
    

    // move label out of the way if the select menu is filled in
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
            <select id='eventLevelInput'
                onChange={e => onChange(e.target.value)}
                name={elementName}
            >
                {/*placeholder value to present component*/}
                <option value={placeholder}>{placeholder}</option> 

                {/*rest of the select menu options*/}
                {Object.entries(selectOptions).map(([key, value]) => (
                    <option key={key} value={key}>{value}</option>
                ))}

            </select>
            <span className='arrow'></span>
            <label className={className} htmlFor='eventLevelInput'>{labelText}</label>
        </div>
    )
}