import { useParams } from "react-router-dom"





export const BoutView = () => {
    
    const { slug } = useParams()

    return(
        <>
            {slug}
        </>
    )
}