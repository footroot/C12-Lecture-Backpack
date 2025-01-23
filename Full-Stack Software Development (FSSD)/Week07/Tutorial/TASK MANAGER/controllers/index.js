let tasks = []
let nextId = 1

const getHomePage = (req, res)=>{
    res.send('Hello World')
}




// Create = Create a new task in my task list
const createTask = (req, res) =>{
    const { title, description, status } = req.body

    if (!title || !description || !status) {
        return res.status(400).json({error: "Info required"})
    }

    const newTask = {
        id: nextId++,
        title: title,
        description: description,
        status: status,
        createdAt: new Date(),
        updatedAt: new Date()
    }
    tasks.push(newTask)
    res.status(201).json(newTask)

}

// Read = Retrieves all information about the tasks
const getAllTasks = (req, res)=>{
    res.json(tasks)
}

// Update = Updates an existing task in the tasks list
const updateTask = (req, res)=>{
    const taskId = parseInt(req.params.id)
    const taskIndex = tasks.findIndex(task => task.id === taskId)

    if (taskIndex === -1) {
        return res.status(404).json({error: "Task not found"})
    }

    const { title, description, status } = req.body
    if (!title || !description || !status) {
        return res.status(400).json({error: 'Provide information to update with'})
    }

    tasks[taskIndex] = {
        ...tasks[taskIndex],
        title,
        description,
        status,
        updatedAt: new Date()
    }

    res.json(tasks[taskIndex])


}

// Delete = Deletes an existing task in the tasks list
const deleteTask = (req, res)=>{
    const taskId = parseInt(req.params.id)
    const taskIndex = tasks.findIndex(task => task.id === taskId)
    if (taskIndex === -1) {
        return res.status(400).json({error: 'Task not found'})
    }

    tasks.splice(taskIndex, 1)
    res.status(204).send({message: "Successfully deleted"})
}



export {
    getHomePage,
    getAllTasks,
    createTask,
    updateTask,
    deleteTask
}