//selectiong our h1 using the element id
console.log(document.getElementById("main-heading"))

//selecting the content of our h1 using the element id
document.getElementById("main-heading").textContent

//change h1 content
document.getElementById("main-heading").textContent ="JavaScript DOM is interesting"

//creating new content for paragraph page with id sports
let sports= "<ul><li>football</li><li>cricket</li><li>basketball</li>"
document.getElementById("sports").innerHTML = sports 

document.title = "Break time soon"

//changing style of h1 using element id
let h1=document.getElementById("main-heading");

h1.style.color="yellow"

/* if we were in the css file
h1{
color : yellow
}
*/

//changing image

let image= document.getElementsByClassName("image-change")[0]
console.log(image)

image.setAttribute("src","../images/CSD 4.jpeg")


let button=document.getElementById("change-me")
button.addEventListener("click", function(){
//alert("This button has been clicked");
image.setAttribute("src","/images/project 1.jpg")
})
button.addEventListener("dblclick", function(){
    image.setAttribute("src", "/images/project 4.jpg")
})


//form Validation

let fullName=document.getElementById("name").value.trim();
let age=document.getElementById("age").value;
let email=document.getElementById("email").value.trim();
let message=document.getElementById("message");
let messageAction=document.getElementById("message-actions");
let form=document.getElementById("form-reg")
let mymessages=document.getElementById("messageinaction");

//this will give us the value of our input tag with the id name
console.log(fullName);


form.addEventListener("submit",(event) =>{ // || function(event) {
    //}
    event.preventDefault();
    let fullName=document.getElementById("name").value.trim();
    let age=document.getElementById("age").value;
    let email=document.getElementById("email").value.trim();
    let message=document.getElementById("message").value.trim();
    let messageAction=document.getElementById("message-actions");
    let mymessages=document.getElementById("messageinaction");
    let form=document.getElementById("form-reg")

    if(fullName==="" ){
        messageAction.textContent="Please enter your full name";
        messageAction.style.color="red";
        return;
    }if(age===""|| isNaN(age)){
        messageAction.textContent="Age must be between 18 and 60";
        messageAction.style.color="yellow";
        return;
    }if(email===""){ 
        messageAction.textContent="Please enter a valid email";
        messageAction.style.color="red"; 
        return;
    }if(message.length > 50){  
            messageAction.textContent="Message must be less than 50 characters long";
            messageAction.style.color="red";  
            return;
    }else{
        mymessages.textContent="Form submitted successfully!";
        mymessages.style.color="green";                      

    }
})



//work to be done
//write code to perform the message check for less than 50 characters
