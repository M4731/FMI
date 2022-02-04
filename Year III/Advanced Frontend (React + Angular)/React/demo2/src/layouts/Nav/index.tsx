import React from 'react';
import {Link} from 'react-router-dom'

const Nav = () => {
    return (
        <nav
            style ={{ 
                display: 'flex',
                justifyContent: 'space-evenly',
                marginBottom: '2rem',
                backgroundColor: '#cccccc',
            }}
        >
            <Link to="/get-started">Join us!</Link>
            <Link to="/welcome">Welcome page</Link>
        </nav>
    )
}

export default Nav