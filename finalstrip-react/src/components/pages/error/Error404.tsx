import { useNavigate, Link } from "react-router-dom"




export const Error404 = () => {

    const navigate = useNavigate();

    return(
        <div className="container">
            <h1>OH NO!</h1>
            <h3>Page not found!</h3>
            <button onClick={() => navigate(-1)}> Go Back </button>
        </ div>
    )
}