import { Link } from 'react-router-dom';


//  In the future this may be a footer menu with icons
export const Journal = () => {

    return(
        <div className='container'>
                <div >
                    <Link to="/journal/tournaments" className="navbar-link">Tournaments</Link>
                </div>
                 <br/>
                 <div >
                    <Link to="/journal/lessons" className="navbar-link">Lessons</Link>
                </div>
                <br />
                <div >
                    <Link to="/journal/fencers" className="navbar-link">Fencer Database</Link>
                </div>
                <br />
                <div >
                    <Link to="/journal/goals" className="navbar-link">Goals</Link>
                </div>
                
        </ div>
    )
}