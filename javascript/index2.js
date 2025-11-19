//Javascript Objects

/* for javascript objects

keyword variableName = {
key : value ,
key2 : value2 , 
}
*/

let person1 = {
    name : 'John',
    age : 27 ,
    isStudent :  true
}
console.log(person1);
console.log(person1.name);
console.log(person1.age);
console.log(person1.isStudent); 
//accessing object properties

//updating object properties
person1.age = 28;
console.log(person1.age);

//console.
person1.name = 'Doe';
console.log(person1.name);

//name,brand,yearOfRegistration,color
let car1 = {
    name : 'BMW',
    brand : 'X5',
    yearOfRegistration : 2020,
    color : 'Black',
    "lastMaintenanceDate" : '2024-05-15'
}
console.log(car1["name"]);

//adding new properties to object
car1.numberOfTyres = 4 
console.log(car1);
delete car1.name;
console.log(car1);


//conditional statements with objects
//if, if-else,if-else if-else

/* if (condition==true){
statement that take place when condition is true
}
*/

noBreak=false
if (noBreak){
    alert("We will all remain in class happily")    
}
//comparison operators
if(10==10){//this is a false condition
    console.log("10 is truly equal to 10")
}
if(10<10){
    console.log("10 is truly equal to 10")
}else{
    console.log("10 is not greater than 10")
}

//if else if
//dayOfTheWeek=prompt("Enter day of the week")
//if(dayOfTheWeek=="Monday"){
//  console.log("Monday is the first day of the week")
// }else if(dayOfTheWeek=="Tuesday"){
//     console.log("Tuesday is the second day of the week")
// }else if(dayOfTheWeek=="Wednesday"){
//     console.log("Wednesday is the third day of the week")
// }else if(dayOfTheWeek=="Thursday"){
//     console.log("Thursday is the fourth day of the week")
// }else if(dayOfTheWeek=="Friday"){
//     console.log("Friday is the fifth day of the week")
// }else if(dayOfTheWeek=="Saturday"){
//     console.log("Saturday is the sixth day of the week")
// }else if(dayOfTheWeek=="Sunday"){
//     console.log("Sunday is the seventh day of the week")
// }else{
//     console.log("Invalid day entered")
// }

/*function nameOfFunction
Function Statements
}
*/
//function definitions
function greet(){
    console.log("Welcome to the afternoon class")
}

//calling the function greet
greet()
greet()
greet()
greet()

//function with parameters
/*
function nameOfFunction(parameters){
what should happen when function is called
}
*/
function morningGreeting(userName){
    console.log(`Good morning, ${userName}!`)

}
//morningGreeting()won't give you the result you want
morningGreeting("Kwame")
morningGreeting("Ama")
morningGreeting("Kofi")
morningGreeting("Esi")


function addNumbers(num1,num2){
    let sum=num1+num2;
    console.log("This is the addition result: " + sum);

}
addNumbers(5,10);
addNumbers(20,30);
addNumbers(-5,15);



//number1=prompt("Enter first number: ");
//number2=prompt("Enter second number: ");
//addNumbers(Number(number1), Number(number2));

areaRectangle=(length,breadth)=>{
    let area=length*breadth;
    console.log("The area of the rectangle is: " + area);
    return area;
}
areaRectangle(5,10);
areaRectangle(7,4);


//function with return types
/*
function nameOfFunction(parameters){
what should happen

return ...
}
*/

let area=areaRectangle(2,5)
console.log(area, "This is the area of the rectangle function no return keyword")

function areaRectangleWithReturn(length,breadth){
    let areaRectangle=length*breadth;
    return areaRectangle;
}
    //Any code after return won't be executed

    let areaReturn =areaRectangleWithReturn(3,6);
    console.log("areaReturn, This has the keyword area Rec")
//afternoon greeting function
function afternoonGreeting(userName){
    return `Good afternoon, ${userName}!`
}

kofi=afternoonGreeting("John")

//loops

//while, for, do-while

/*
for(initializer;condition;iterator){

//what loops should do
}
*/


//counting 1 to 5

for(let i=1;i<=5;i++){
    console.log(i);
}

//Second version of counting to 5 in a for loop
//              this means not equal to              this incresease count by 1
for(let count=1;count!=6;                            count++){
    console.log("Counting", count);
}

//while loop
/*
while(condition{
//what the code should do

iterator}
*/
count=1;

while(count<=5){
    alert(count);
    count++;
}




console.log("end of program ")