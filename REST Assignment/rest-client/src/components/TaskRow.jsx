import { useState } from "react";
import { Link } from "react-router-dom";

export default function TaskRow({
    task,
    isSelected,
    isEditing,
    onToggle,
    onEditStart,
    onEditCancel,
    onEditSave,
}) {
    const [form, setForm] = useState({
        title: task.title,
        priority: task.priority,
        status: task.status,
    });

    function handleChange(e) {
        setForm({ ...form, [e.target.name]: e.target.value });
    }

    return (
        <tr>
            <td>
                <input
                    type="checkbox"
                    checked={isSelected}
                    onChange={() => onToggle(task.id)}
                />
            </td>

            <td>
                {isEditing ? (
                    <input
                        name="title"
                        value={form.title}
                        onChange={handleChange}
                    />
                ) : (
                    <Link to={`/tasks/${task.id}`}>{task.title}</Link>
                )}
            </td>

            <td>
                {isEditing ? (
                    <select
                        name="priority"
                        value={form.priority}
                        onChange={handleChange}
                    >
                        <option>low</option>
                        <option>medium</option>
                        <option>high</option>
                    </select>
                ) : (
                    task.priority
                )}
            </td>

            <td>
                {isEditing ? (
                    <select
                        name="status"
                        value={form.status}
                        onChange={handleChange}
                    >
                        <option>pending</option>
                        <option>done</option>
                    </select>
                ) : (
                    task.status
                )}
            </td>

            <td>
                {isEditing ? (
                    <>
                        <button onClick={() => onEditSave(task.id, form)}>
                            Save
                        </button>
                        <button onClick={onEditCancel}>Cancel</button>
                    </>
                ) : (
                    <button onClick={() => onEditStart(task.id)}>Edit</button>
                )}
            </td>
        </tr>
    );
}
