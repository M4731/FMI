const App = (): JSX.Element => {
    var Chance = require('chance');

    // Instantiate Chance so it can be used
    var chance = new Chance();

    // Use Chance here.
    const name = chance.name()
    
    return <div>Hello from AppComponent</div>
};

export default App; 
