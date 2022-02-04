import React from 'react';
import Input from '../../components/Input'

const RegisterForm = () => {
    return (
        <form>
            <h3>Sign up</h3>

            <Input placeholder={'Full name'} />
            <Input placeholder={'Email address'}/>
            <Input placeholder={'Password'} type={'password'}/>

            <button type="submit">Sign me up!</button>
        </form>
    )
}


export default RegisterForm