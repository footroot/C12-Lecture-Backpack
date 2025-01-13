import { useState } from "react";

function App() {
  const [task, setTask] = useState("");

  const [tasks, setTasks] = useState([
    {
      name: "Grocery shopping",
      completed: false,
    },
  ]);

  //Add task
  const addTask = () => {
    if (task.trim() === "") return;
    setTasks([...tasks, { name: task, completed: false }]);
    setTask("");
  };

  const handleChange = (event) => {
    setTask(event.target.value);
  };

  //Update (toggle a task to indicate it is completed)
  const updateTask = (index) => {
    console.log("Clicked")
    const updatedTask = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(updatedTask);
  };

  //Delete a task

  return (
    <>
      <div>
        <input onChange={handleChange} />
        <button onClick={addTask}>Add task</button>
      </div>
      <ul>
        {/**Display a task */}
        {tasks.map((task, index) => {
          return (
            <div>
              <button onClick={()=>updateTask(index)}>Update Task</button>
              <li style={{textDecoration: task.completed ? "line-through" : "none"}}>{task.name}</li>
              <button>Delete</button>
            </div>
          );
        })}
      </ul>
    </>
  );
}

export default App;
