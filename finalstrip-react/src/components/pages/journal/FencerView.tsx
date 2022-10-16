import { useParams } from "react-router-dom"



export const FencerView = () => {

    const { slug } = useParams()

    return(
        <>
            {slug}
        </>
    )
}