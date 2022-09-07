import {Link} from "react-router-dom";
import { useSelector } from "react-redux";
import axios from "axios"

import { RootState } from "../redux/store";


export const NavBar = () => {
    let links;
    const auth = useSelector((state: RootState) => state.auth.value)

    const logout = async () => {
        await axios.post('logout');
        axios.defaults.headers.common['Authorization'] = '';
    }

    if (auth) {
        links = <div className="text-end">
                    <Link to="/login" className="btn btn-outline-light me-2" onClick={logout}>Logout</Link>
                </div>
    } else {
        links = <div className="text-end">
                    <Link to="/login" className="btn btn-outline-light me-2">Login</Link>
                    <Link to="/register" className="btn btn-outline-light me-2">Register</Link>
                </div>
    }

    return (
        <header className="p-3 text-bg-dark">
            <div className="container">
            <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">

                <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                    <li><Link to="/" className="nav-link px-2 text-secondary">Home</Link></li>
                </ul>

                {links}
            </div>
            </div>
        </header>
    )
}

{/* <div className='d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start'>

</div> */}


