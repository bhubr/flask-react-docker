import { useState, useEffect } from 'react';
import './App.css';

const serverUrl = process.env.REACT_APP_SERVER_URL;

function App() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);
  const [taskLabel, setTaskLabel] = useState('');
  useEffect(() => {
    fetch(`${serverUrl}/api/tasks`)
      .then(res => {
        if (!res.ok) throw new Error(res.statusText)
        return res.json()
      })
      .then(setTasks)
      .catch(setError);
  }, []);

  const onSubmit = e => {
    e.preventDefault();
    fetch(`${serverUrl}/api/tasks`, {
      method: 'POST',
      headers: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      body: `label=${encodeURIComponent(taskLabel)}`
    })
      .then(res => {
        if (!res.ok) throw new Error(res.statusText)
        return res.json()
      })
      .then(() => setTaskLabel(''))
      .catch(setError);
  };

  const onChange = ({ target: { value } }) => setTaskLabel(value);
  return (
    <div className="App">
      <h1>Hello React!</h1>
      {
        error && <p>{error.message}</p>
      }
      <h3>Add task</h3>
      <form onSubmit={onSubmit}>
        <label htmlFor="taskLabel">
          Task label
          <input id="taskLabel" value={taskLabel} onChange={onChange} />
        </label>

        <button type="submit">Add</button>
      </form>
      <ul>
      {
        tasks.map(t => (
          <li key={t.id}>{t.label}</li>
        ))
      }
      </ul>
    </div>
  );
}

export default App;
