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
                    <Link to="/login" className="find-me" onClick={logout}>Logout</Link>
                </div>
    } else {
        links = <div className="text-end">
                    <Link to="/login" className="find-me">Login</Link>
                    <Link to="/register" className="find-me">Register</Link>
                </div>
    }

    return (
        <header className="header-fixed">
            <div className="header-class">
            <div className="header-contents">

                <ul className="home-button">
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


