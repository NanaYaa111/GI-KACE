console.log("Hello, World!");

//Data types in JavaScript

/* It is ideal to use camelCase while naming variables in JavaScript */

const isFoodGreat=true;

let numberOfBananas;

//const numberOfApples;//This connot be done
//String data type
let ourStringVariable= "";

console.log("This is the data type of ourStringVariable: " ,
    typeof (ourStringVariable));

    let age;

    age=100;
    console.log(typeof (age));
    age="Hundred";

    //Write a program to ask people for their age

    //age2 =prompt("please enter your age: ");

   //"The antelope";+ "gallops" = "The antelopegallops"

   console.log("The antelope "+ "gallops");

   console.log("Today we will break at "+ "4 pm");

   //Number
   console.log(typeof(34324523));

   console.log(typeof(34.324523));

   console.log(2+3)

   let number1=5;
    let number2=8;

    let result=number2-number1;

    console.log(result)

    //multiplication
    multiResult=number2*4;
    console.log(multiResult+ " Multiplication result");

    //division
    let divResult=10/2;
    console.log(divResult+" Division result");// 5-> "5"+ " Division result"

    //exponentiation
    console.log(2**3,"This is an exponent operation");

    //null data type
    let breakTime=null;

    let isItTrue=true;

    let isItReallyTrue=false;
    console.log(typeof(isItReallyTrue));"Boolean data type "

    //undefined data type
    let declaredVariable;

    divResult=undefined;

    //Array data type

    /* Generally a collection of various items in a list*/

    //Empty Stationary array
    let stationaryArray=[];             

    console.log(stationaryArray)

    let school=["Prempeh", "Hope College", "Adisadel", "Mfantsipim", "St. Peters"];

    //n-1 where n=number of items in the list 

    //getting Prempeh from the list
    
    school[0];

console.log( `  ${school[4]} is the school we wish to attend`); // `${}`

school[0]

console.log(`${school[0]} is the school we wish to attend`)

// String methods and array methods

console.table(school)

let string123= 'the game is bias'

string123.toUpperCase

//alert(string123.toUpperCase())

// first name, last name, contact, email, password

//firstName= prompt('Enter the first name');
//lastName= prompt('Enter the last name') .toUpperCase();
//contact= prompt('Kindly fill in your contact information');
//email= prompt('Provide your email address');
//password= prompt('What is the password');

//congratulationsMessage=`Congrats ${firstName} ${lastName} for registring \n Thank you`

//console.log(congratulationsMessage)

simpleMessage= 'hello world'

// Changing message to title case

splitWords= simpleMessage.split(' ')

let word1= splitWords[0] .slice(0,1) .toUpperCase() + splitWords[0] .slice(1,) 

let word2= splitWords[1] .slice(0,1) .toUpperCase() + splitWords[1] .slice(1,)

let finalWord= [word1, word2].join(' ')

console.log(splitWords[0] .slice(0,1) .toUpperCase() + splitWords[0] .slice(1,))

console.log(splitWords[1] .slice(0,1) .toUpperCase() + splitWords[1] .slice(1,))

// join them

console.log(finalWord)

numberArray= [1,2,3,4]

firstName= prompt('Enter the first name');
lastName= prompt('Enter the last name') .toUpperCase();
contact= prompt('Kindly fill in your contact information');
email= prompt('Provide your email address');
password= prompt('What is the password');

congratulationsMessage=`Congrats ${firstName} ${lastName} for registring \n Thank you`

console.log(congratulationsMessage)

let userRegistration=[]

userRegistration[0] = firstName
userRegistration[1] = lastName
userRegistration[2] = contact
userRegistration[3] = email
userRegistration[4] = password

// array methods

let arrayMethodTest = []

arrayMethodTest.push(1)
arrayMethodTest.push('Let down')

console.log(arrayMethodTest)