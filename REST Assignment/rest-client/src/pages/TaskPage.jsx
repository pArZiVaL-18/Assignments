import { useEffect, useState } from "react";
import {
    getTasks,
    deleteMultipleTasks,
    createTask,
    updateTask,
} from "../api/api";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";
import { useNavigate } from "react-router-dom";
import Clock from "../components/Clock";

export default function TasksPage() {
    const [tasks, setTasks] = useState([]);
    const [selectedIds, setSelectedIds] = useState([]);
    const [editingId, setEditingId] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        loadTasks();
    }, []);

    async function loadTasks() {
        setTasks(await getTasks());
    }

    async function handleCreate(task) {
        await createTask(task);
        loadTasks();
    }

    function toggleSelection(id) {
        setSelectedIds((prev) =>
            prev.includes(id) ? prev.filter((i) => i !== id) : [...prev, id],
        );
    }

    async function handleDelete() {
        await deleteMultipleTasks(selectedIds);
        setSelectedIds([]);
        loadTasks();
    }

    function handleEditStart(id) {
        setEditingId(id);
    }

    function handleEditCancel() {
        setEditingId(null);
    }

    async function handleEditSave(id, updatedData) {
        await updateTask(id, updatedData);
        setEditingId(null);
        loadTasks();
    }

    return (
        <>
            <Clock />
            <TaskForm onCreate={handleCreate} />

            <TaskList
                tasks={tasks}
                selectedIds={selectedIds}
                editingId={editingId}
                onToggle={toggleSelection}
                onEditStart={handleEditStart}
                onEditCancel={handleEditCancel}
                onEditSave={handleEditSave}
            />

            {selectedIds.length > 0 && (
                <div style={{ marginTop: 16 }}>
                    <button onClick={handleDelete}>Delete</button>
                </div>
            )}
        </>
    );
}
