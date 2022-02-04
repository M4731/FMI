import { useState } from 'react'

interface PropsPerson{
    personName : string;
    age ?: number;
}

const Person = ({personName, age = 20} : PropsPerson) => {
    const [clicks,setClicks] = useState(0)
    const [value,setValue] = useState('change-able string')

    const handleClick = (event:React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        setClicks(clicks+1)
    }

    const handleChange = (e:React.ChangeEvent<HTMLInputElement>) => {
        setValue(e.target.value)
    }

    return <div>

        <section>
            {`Welcome back, ${personName}!\n`}
            {`Age: ${age}`}
        </section>

        <aside>
            <h3>{`You clicked ${clicks}`}</h3>
            <button onClick={handleClick}>Click me!</button>
        </aside>
        <br/>

        <aside>
            <input value={value} onChange={handleChange}/>
        </aside>
    </div>
};

export default Person