import React, {useState} from 'react';
import LoginForm from '../../modules/LoginForm';
import RegisterForm from '../../modules/RegisterForm';

const GetStartedPage = () => {
    const [showRegister, setShowRegister] = useState(false)

    const handlePageView = () => {
        setShowRegister(!showRegister)
    }

    return (
        <>
            <button onClick={handlePageView}>
                {!showRegister ? 'Get me to Register!' : 'Get me to Login!'}
            </button>

            {!showRegister && <LoginForm />}
            {showRegister && <RegisterForm />}
        </>
    ) 
}

export default GetStartedPage