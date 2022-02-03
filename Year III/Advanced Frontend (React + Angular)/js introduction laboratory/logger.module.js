//let var const

//ES5 
function log(message) {
    console.log(message);
};

const log = function(message) {
    console.log(message);
};


//ES6

const log =  message => console.log(message);