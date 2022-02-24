
const loginForm=document.querySelector("#login-form");
const loginInput=document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");



const HIDDEN_CLASSNAME="hidden";
const USER_NAME="username";

function onsubmit(event){
  event.preventDefault();
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  localStorage.setItem(USER_NAME,username);
  paintGreetion(username);
  

}

function paintGreetion(username){
  greeting.innerText="hello " + username;
  greeting.classList.remove(HIDDEN_CLASSNAME);

}


//loginForm.addEventListener("submit",onsubmit);

const savedUsername = localStorage.getItem(USER_NAME);

if(savedUsername===null){
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit",onsubmit);

}else{
  paintGreetion(savedUsername);


}