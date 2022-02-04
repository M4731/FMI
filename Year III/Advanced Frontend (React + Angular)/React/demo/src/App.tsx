import Person from "./Person";

const App = (): JSX.Element => {

    var Chance = require('chance');
    // Instantiate Chance so it can be used
    var chance = new Chance();

    const name = chance.name()
    const age = chance.age()

    return <div><Person personName={name} age={age}/></div>
};

export default App; 
