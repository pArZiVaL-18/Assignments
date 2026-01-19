const BASE_URL = "http://localhost:8080/api";

// get all tasks
export async function getTasks() {
    const res = await fetch(`${BASE_URL}/tasks`);
    if (!res.ok) throw new Error("Failed to fetch tasks");
    return res.json();
}

// get a task based on id
export async function getTaskById(id) {
    const res = await fetch(`${BASE_URL}/tasks/${id}`);
    if (!res.ok) throw new Error("Task not found");
    return res.json();
}

// create a new task
export async function createTask(task) {
    const res = await fetch(`${BASE_URL}/tasks`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task),
    });

    if (!res.ok) throw new Error("Failed to create task");
    return res.json();
}

// update a task
export async function updateTask(id, task) {
    const res = await fetch(`${BASE_URL}/tasks/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task),
    });

    if (!res.ok) throw new Error("Update failed");
    return res.json();
}

// delete a single task based on id
export async function deleteTask(id) {
    const res = await fetch(`${BASE_URL}/tasks/${id}`, {
        method: "DELETE",
    });

    if (!res.ok) throw new Error("Failed to delete task");
}

// delete multiple tasks
export async function deleteMultipleTasks(ids) {
    await Promise.all(ids.map((id) => deleteTask(id)));
}
