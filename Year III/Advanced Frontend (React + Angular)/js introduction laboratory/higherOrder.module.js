// map filter find reduce (any every)

const obj = {
    name:"Ionel",
    age:"71"
}

// console.log(obj.name) // Ionel
// console.log(obj.age) // 71

const arrayObj = [
    {
        name: "Gigel",
        matematica: 5    
    },
    {
        name: "Ionica",
        matematica: 8    
    },
    {
        name: "Marian",
        matematica: 6    
    },
    {
        name: "Elena",
        matematica: 9    
    }
];

// for(let i=0;i<arrayObj.length;i++){
//     arrayObj[i].matematica += 1;
// }

//clonare a unui array de obiecte
const clonearrayObj = JSON.parse(JSON.stringify(arrayObj));

const newArrayMap = clonearrayObj.map(function(currentElement, index, initialArray){
    currentElement.matematica += 1;
    return currentElement;
}) 

// console.log(newArrayMap);
// console.log(arrayObj);


const clonearrayObj2 = JSON.parse(JSON.stringify(arrayObj));

const lessThan8 = (currentElement) => currentElement.matematica <= 8;
const newArrayFiltered = clonearrayObj2.filter(lessThan8);
const newArrayFind = clonearrayObj2.find(lessThan8);

console.log(newArrayFiltered)
console.log(newArrayFind)

const sum = clonearrayObj2.reduce((accumulator,currentElement, index, initialArray)=>{
    accumulator += currentElement.matematica;
    return accumulator;
},0) //0 este initializarea accumulator-ului

console.log("Suma tuturor notelor la matematica: "+sum)