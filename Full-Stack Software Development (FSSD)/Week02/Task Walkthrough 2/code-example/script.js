let tasks = [];

function displayTasks() {
    const taskList = document.getElementById("taskList");

    taskList.innerHTML = '';

    tasks.forEach((task, index) => {
        const taskItem = document.createElement('li');
        taskItem.textContent = task.text;

        const completedBtn = document.createElement('button');
        completedBtn.textContent = "Complete";
        completedBtn.onclick = () => markAsCompleted(index);

        taskList.appendChild(taskItem);
        taskItem.appendChild(completedBtn);

    })

}

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskText = taskInput.value.trim();

    if (taskText) {
        tasks.push({
            text: taskText,
            completed: false
        });
        taskInput.value = '';
        displayTasks();
    }
}

function markAsCompleted(index) {
    tasks[index].completed = !tasks[index].completed;
    displayTasks();
}

document.getElementById("addTaskBtn").addEventListener('click', addTask);