const returnAPromise = function(data){
    return new Promise(function(resolve, reject){
        if(typeof data === 'string'){
            resolve(data+" este string");
        }
        else{
            reject(data+" nu este string");
        }
    });
};

//ES5 -- bad practice
returnAPromise("TEST")
    .then(function(response){
        console.log(response);
})
    .catch(function(error){
        console.log(error);
});

returnAPromise(1).
    then(function(response){
        console.log(response);
})
    .catch(function(error){
        console.log(error);
});

//ES6 async await
async function testPromise(data){
    try{
        const response = await returnAPromise(data);
        //const response2 = await altPromise(response);
        console.log(response);
    } catch(error){
        console.log(error);
    }
}

testPromise("string test");
testPromise(23.2);