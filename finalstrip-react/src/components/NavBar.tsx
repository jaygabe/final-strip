import {Link} from "react-router-dom";
import { useSelector } from "react-redux";
import axios from "axios"

import { RootState } from "../redux/store";
import { useState } from "react";


export const NavBar = () => {
    const [mobileLinks, setMobileLinks] = useState(false)
    let auth_links;

    const auth = useSelector((state: RootState) => state.auth.value)

    // const navLinks = () => {
    //     mobileLinks ? "nav-links mobile" : "nav-links hidden"
    // }

    const logout = async () => {
        await axios.post('api/auth/logout', {withCredentials: true});
        axios.defaults.headers.common['Authorization'] = '';
    }

    if (auth) {
        auth_links = <div className={mobileLinks ? 'navbar-account open-menu' : 'navbar-account'}>
                        <Link 
                            to="login" 
                            className={mobileLinks ? 'navbar-account-button open-menu pop' : 'navbar-account-button pop'} 
                            onClick={logout}>
                                Logout
                        </Link>
                    </div>
    } else {
        auth_links = <div className={mobileLinks ? 'navbar-account open-menu' : 'navbar-account'}>
                        <Link 
                            to="login" 
                            className={mobileLinks ? "navbar-account-button open-menu pop" : "navbar-account-button pop"}
                            onClick={() => setMobileLinks(false)}>
                                Login
                        </Link>
                        <Link 
                            to="register" 
                            className={mobileLinks ? "navbar-account-button open-menu pop" : "navbar-account-button pop"}
                            onClick={() => setMobileLinks(false)}>
                                Register
                        </Link>
                    </div>
    }

    return (
        <nav className={mobileLinks ? "navbar open-menu" : "navbar"}>
            <div className="logo">Finalstrip</div>
            
            <div className={mobileLinks ? "navbar-links open-menu" : "navbar-links"}>
                <ul>
                    <li><Link to="/" className="navbar-link" onClick={() => setMobileLinks(!mobileLinks)}>Home</Link></li>
                    <li><Link to="/journal/" className="navbar-link" onClick={() => setMobileLinks(!mobileLinks)}>Journal</Link></li>
                    <li><Link to="/journal/tournaments" className="navbar-link" onClick={() => setMobileLinks(!mobileLinks)}>Tournaments</Link></li>
                    <li><Link to="/journal/lessons" className="navbar-link" onClick={() => setMobileLinks(!mobileLinks)}>Lessons</Link></li>
                    <li><Link to="/journal/fencers" className="navbar-link" onClick={() => setMobileLinks(!mobileLinks)}>Fencers</Link></li>
                </ul>
            </div>
            
            {auth_links}

            <a href="#" className={mobileLinks ? "hamburger open-menu" : "hamburger"}  onClick={() => setMobileLinks(!mobileLinks)}>
                <span className="line"></span>
                <span className="line"></span>
                <span className="line"></span>
            </a>
        </nav>
    )
}

{/* <div className='d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start'>

</div> */}


