import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { getTaskById, updateTask } from "../api/api";

export default function TaskEditPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [task, setTask] = useState(null);

    useEffect(() => {
        getTaskById(id).then(setTask);
    }, [id]);

    async function handleSubmit(e) {
        e.preventDefault();
        await updateTask(id, task);
        navigate("/");
    }

    if (!task) return <p>Loading...</p>;

    return (
        <form onSubmit={handleSubmit}>
            <h3>Edit Task</h3>

            <input
                value={task.title}
                onChange={(e) => setTask({ ...task, title: e.target.value })}
            />

            <textarea
                value={task.description}
                onChange={(e) =>
                    setTask({ ...task, description: e.target.value })
                }
            />

            <button type="submit">Save</button>
        </form>
    );
}
