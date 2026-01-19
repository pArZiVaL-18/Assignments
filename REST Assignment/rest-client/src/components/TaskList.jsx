// import { Link } from "react-router-dom";

// export default function TaskList({ tasks, selectedIds, onToggle }) {
//     return (
//         <ul>
//             {tasks.map((task) => (
//                 <li key={task.id}>
//                     <input
//                         type="checkbox"
//                         checked={selectedIds.includes(task.id)}
//                         onChange={() => onToggle(task.id)}
//                     />

//                     <Link to={`/tasks/${task.id}`}>
//                         <strong>{task.title}</strong>
//                     </Link>

//                     <p>{task.description}</p>
//                 </li>
//             ))}
//         </ul>
//     );
// }

import { Link } from "react-router-dom";
import TaskRow from "./TaskRow";

export default function TaskList({
    tasks,
    selectedIds,
    onToggle,
    editingId,
    onEditStart,
    onEditCancel,
    onEditSave,
}) {
    return (
        <table border="1" cellPadding="8" style={{ width: "100%" }}>
            <thead>
                <tr>
                    <th></th>
                    <th>Title</th>
                    <th>Priority</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>

            <tbody>
                {tasks.map((task) => (
                    <TaskRow
                        key={task.id}
                        task={task}
                        isSelected={selectedIds.includes(task.id)}
                        isEditing={editingId === task.id}
                        onToggle={onToggle}
                        onEditStart={onEditStart}
                        onEditCancel={onEditCancel}
                        onEditSave={onEditSave}
                    />
                ))}
            </tbody>
        </table>
    );
}
