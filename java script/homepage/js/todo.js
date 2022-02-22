const Todoform=document.getElementById("todo-form");
const TodoInput =Todoform.querySelector("input");
const Todolist=document.getElementById("todo-list");

const TODO_KEY="todos"

let toDos=[]

function saveToDos(){
    localStorage.setItem(TODO_KEY,JSON.stringify(toDos));

}

function deletToDo(event){
    const li=event.target.parentElement;
    li.remove();
    toDos=toDos.filter((todo) => todo.id !==parseInt(li.id));
    saveToDos();
}


function paintToDo(newTodo){
    const li = document.createElement("li");
    li.id=newTodo.id;
    const span = document.createElement("span");
    span.innerText=newTodo.text;
    const button = document.createElement("button");
    button.innerText="❌"
    button.addEventListener("click",deletToDo);
    li.appendChild(span);
    li.appendChild(button);
    Todolist.appendChild(li);
}


function handleTodosubmit(event){
    event.preventDefault();
    const newTodo=TodoInput.value;
    TodoInput.value="";
    const newTodoObject={
        text:newTodo,
        id:Date.now()
    };
    toDos.push(newTodoObject);
    paintToDo(newTodoObject);
    saveToDos();
    
}

Todoform.addEventListener("submit",handleTodosubmit);


const saved_todo = localStorage.getItem(TODO_KEY);


if(saved_todo!==null){
    const parsedToDos = JSON.parse(saved_todo);
    toDos=parsedToDos;
    parsedToDos.forEach(paintToDo);   
}

