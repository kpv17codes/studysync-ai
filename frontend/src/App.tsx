
import { useState } from 'react'
import './App.css'

type Task = {
  id: number
  title: string
  course: string
  due_date: string
}

function App() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [title, setTitle] = useState('')
  const [course, setCourse] = useState('')
  const [dueDate, setDueDate] = useState('')

  function addTask(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()

    if (!title.trim() || !course.trim() || !dueDate) return

    const newTask: Task = {
      id: Date.now(),
      title: title.trim(),
      course: course.trim(),
      due_date: dueDate,
    }

    setTasks([...tasks, newTask])
    setTitle('')
    setCourse('')
    setDueDate('')
  }

  return (
    <main className="dashboard">
      <header>
        <h1>StudySync AI</h1>
        <p>Your academic tasks, all in one place.</p>
      </header>

      <section>
        <h2>Add a Task</h2>
        <form onSubmit={addTask}>
          <label htmlFor="task-title">Task Title</label>
          <input
            id="task-title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            placeholder="e.g. Finish networking assignment"
            required
          />

          <label htmlFor="task-course">Course</label>
          <input
            id="task-course"
            value={course}
            onChange={(event) => setCourse(event.target.value)}
            placeholder="e.g. COMP 343"
            required
          />

          <label htmlFor="task-date">Due Date</label>
          <input
            id="task-date"
            type="date"
            value={dueDate}
            onChange={(event) => setDueDate(event.target.value)}
            required
          />

          <button type="submit">Add Task</button>
        </form>
      </section>

      <section>
        <h2>My Tasks ({tasks.length})</h2>
        {tasks.length === 0 ? (
          <p>No tasks yet. Add your first task above!</p>
        ) : (
          <ul>
            {tasks.map((task) => (
              <li key={task.id}>
                <strong>{task.title}</strong>
                <p>{task.course} — Due: {task.due_date}</p>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  )
}

export default App
