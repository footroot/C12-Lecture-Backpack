import express from "express"
import { getHomePage, getAllTasks, createTask , updateTask, deleteTask} from "../controllers/index.js"
const routes = express.Router()


routes.get('/', getHomePage)
routes.get('/tasks', getAllTasks)
routes.post('/tasks', createTask)
routes.put('/tasks/:id', updateTask)
routes.delete('/tasks/:id', deleteTask)

export {
    routes
}