import { useState, ChangeEvent } from "react";

interface ToDoItem {
  title: string,
  detail: string,
};

interface props {
  handleSubmit: any
}

const ToDoItem = (props: props) => {

  const [title, setTitle] = useState('');
  const [detail, setDetail] = useState('');

  const handleTitleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTitle(event.target.value)
  };

  const handleDetailChange = (event: ChangeEvent<HTMLInputElement>) => {
    setDetail(event.target.value)
  };

  const buttonClassHandler = () => {
    if (title !== '' && detail !== '') {return 'pointer-events-auto'}
    else {return 'pointer-events-none opacity-30'}
  }

  return (
    <div className="px-5 py-3 rounded-xl shadow-md shadow-gray-300 my-2 relative flex flex-col items-center">
      <label>
        title : 
        <input className="mx-3" type="text" name="title" value={title} onChange={handleTitleChange} />
      </label>
      <label>
        detail : 
        <input className="mx-3" type="text" name="detail" value={detail} onChange={handleDetailChange} />
      </label>
      <button className={`px-5 py-3 my-3 rounded-lg shadow-md w-fit ${buttonClassHandler()}`} onClick={() => {props.handleSubmit(title, detail); setTitle(''); setDetail('')}}>投稿</button>
    </div>
  )
}

export default ToDoItem