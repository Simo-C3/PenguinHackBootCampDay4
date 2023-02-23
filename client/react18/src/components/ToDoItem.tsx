import { FaTrash } from "react-icons/fa"

interface ToDoItemProps {
  id: string,
  title: string,
  detail: string,
  created_at: string,
  handleDelete: any
};

const ToDoItem = (props: ToDoItemProps) => {
  return (
    <div className="px-5 py-3 rounded-xl shadow-md shadow-gray-300 my-2 relative">
      <div className="absolute top-3 right-5 text-gray-400 hover:text-gray-600" onClick={() => {props.handleDelete(props.id)}}>
        <FaTrash />
      </div>
      <div className="w-fit text-xl">{props.title}</div>
      <div className="w-fit text-gray-600 mx-2">{props.detail}</div>
      <div className="text-gray-500 text-right">{props.created_at}</div>
    </div>
  )
}

export default ToDoItem