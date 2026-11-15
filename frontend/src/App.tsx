
import { useEffect, useState } from 'react'
import './App.css'

type Task = {
  id: number
  title: string
  course: string
  due_date: string
}

const API_URL = 'http://localhost:8000'

function App() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [title, setTitle] = useState('')
  const [course, setCourse] = useState('')
  const [dueDate, setDueDate] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    async function loadTasks() {
      try {
        const response = await fetch(`${API_URL}/tasks/`)
        if (!response.ok) throw new Error('Could not load tasks')
        setTasks(await response.json())
      } catch {
        setError('Unable to load tasks. Please try again.')
      }
    }
    void loadTasks()
  }, [])

  async function addTask(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setError('')

    if (!title.trim() || !course.trim() || !dueDate) {
      setError('Please complete all fields.')
      return
    }

    try {
      const response = await fetch(`${API_URL}/tasks/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: title.trim(),
          course: course.trim(),
          due_date: dueDate,
        }),
      })

      if (!response.ok) throw new Error('Could not save task')

      const newTask: Task = await response.json()
      setTasks((previous) => [...previous, newTask])
      setTitle('')
      setCourse('')
      setDueDate('')
    } catch {
      setError('Unable to save task. Please try again.')
    }
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
        {error && <p role="alert">{error}</p>}
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
