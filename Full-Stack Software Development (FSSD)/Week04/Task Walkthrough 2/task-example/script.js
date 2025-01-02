const taskList = document.getElementById('task-list');
const addTask = document.getElementById('add-task');

// fetch data from api
fetch('https://jsonplaceholder.typicode.com/todos?_limit=5')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        displayData(data);
    })
    .catch(error => console.error(error))

function displayData(tasks) {
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        taskList.appendChild(li);
    });
}

// add task from the page
addTask.addEventListener('click', () => {
    const taskInput = document.getElementById('task-input');
    const taskText = taskInput.value;

    if (taskText) {
        const taskItem = document.createElement('li');
        taskItem.textContent = taskText;
        taskList.appendChild(taskItem);
        taskInput.value = '';
    }
})

// mark task as completed
taskList.addEventListener('click', ()=> {
    if (event.target.tagName === 'LI') {
        event.target.classList.toggle('completed');
    }
})