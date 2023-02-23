import { useState, useEffect } from "react";
import ToDoItem from './components/ToDoItem'
import ToDoForm from './components/ToDoForm'
import axios from './axios'

interface ToDoItem {
  id: string,
  title: string,
  detail: string,
  created_at: string
  updated_at: string
};

function App() {

  const [toDoList, setToDoList] = useState<ToDoItem[]>([]);

  const fetchData = async () => {
    const response = await axios.get('/todo');
    console.log(response.data)
    setToDoList(response.data);
    return response;
  }

  const handleSubmit = async (title: string, detail: string) => {
    const response = await axios.post('/todo', {
      title: title,
      detail: detail
    });
    console.log(response.data)
    fetchData()
  }

  const handleDelete =  async (id: string) => {
    const response = await axios.delete(`/todo/${id}`);
    console.log(response.data)
    fetchData()
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
      <div className="w-[70%] mx-auto my-10">
        <ToDoForm handleSubmit={(title: string, detail: string) => {handleSubmit(title, detail)}} />
        <div>
          {toDoList.map((item, index) => {
            return <ToDoItem key={index} id={item.id} title={item.title} detail={item.detail} created_at={item.created_at} handleDelete={(id: string) => {handleDelete(id)}} />
          })}
        </div>
      </div>
    );
}

export default App;
