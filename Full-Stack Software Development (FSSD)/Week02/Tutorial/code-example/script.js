
document.getElementById('addTaskBtn').addEventListener('click', function () {
    const taskInput = document.getElementById("taskInput");

    const taskText = taskInput.value.trim();

    const taskList = document.getElementById("taskList");

    // const deleteElement = document.getElementById("deleteElement");

    // deleteElement.remove();

    const li = document.createElement('li');

    li.style.fontSize = "20px";

    // li.setAttribute("class", "thisclass")

    li.classList.add('task');

    li.innerHTML = `
        <span>${taskText}</span>
        <button class="deleteBtn">Delete</button>
    `

    taskList.appendChild(li);
    taskInput.value = '';

})

document.getElementById('taskList').addEventListener('click', function (event) {
    if (event.target.classList.contains('deleteBtn')) {
        const task = event.target.parentElement;
        task.remove();
    }
})