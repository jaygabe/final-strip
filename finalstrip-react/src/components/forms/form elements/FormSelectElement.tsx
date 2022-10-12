import { useState } from 'react'


export const FormSelectElement = ({
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
    

    const [className, setClassName]  = useState<string>('')

    function onChange(entry:string) {
        setValue(entry)
        if (entry != '') {
            setClassName('jumped')
        }else{
            setClassName('')
        }
    } 

    let tournaments = {
        'Intergalactic': 'Intergalactic',
        'Interplanetary': 'Interplanetary'
    }
    
    return (
        <div className='form-input'>
            <select id='eventLevelInput'
                onChange={e => onChange(e.target.value)}
                name={elementName}
            >
                <option value=''>{placeholder}</option>

                {Object.entries(tournaments).map(([key, value]) => (
                    <option key={key} value={key}>{value}</option>
                ))}

                <option value="Local">Local</option>
                <option value="Regional">Regional</option>
                <option value="National">National</option>
                <option value="World">World</option>
            </select>
            <label className={className} htmlFor='eventLevelInput'>{labelText}</label>
        </div>
    )
}