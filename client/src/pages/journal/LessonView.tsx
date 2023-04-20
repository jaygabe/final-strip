

import { useParams } from "react-router-dom"


export const LessonView = () => {

    const { slug } = useParams()

    return(
        <>
            {slug}
        </>
    )
}