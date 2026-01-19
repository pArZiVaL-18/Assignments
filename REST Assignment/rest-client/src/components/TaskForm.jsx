import { useState } from "react";

export default function TaskForm({ onCreate }) {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    function handleSubmit(e) {
        e.preventDefault();

        onCreate({
            title,
            description,
            status: "pending",
            priority: "medium",
        });

        setTitle("");
        setDescription("");
    }

    return (
        <form onSubmit={handleSubmit}>
            <h3>Create Task</h3>

            <input
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
            />

            <textarea
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />

            <button type="submit">Add Task</button>
        </form>
    );
}
