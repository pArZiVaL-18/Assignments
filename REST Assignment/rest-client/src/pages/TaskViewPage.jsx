import { useParams, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import { getTaskById } from "../api/api";

export default function TaskViewPage() {
    const { id } = useParams();
    const [task, setTask] = useState(null);

    useEffect(() => {
        getTaskById(id).then(setTask);
    }, [id]);

    if (!task) return <p>Loading...</p>;

    return (
        <div>
            <h2>{task.title}</h2>
            <p>{task.description}</p>
            <p>Status: {task.status}</p>
            <p>Priority: {task.priority}</p>

            <Link to="/">← Back</Link>
        </div>
    );
}
