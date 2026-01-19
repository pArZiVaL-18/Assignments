import { Routes, Route } from "react-router-dom";
import TasksPage from "./pages/TaskPage";
import TaskViewPage from "./pages/TaskViewPage";
import TaskEditPage from "./pages/TaskEditPage";

export default function App() {
    return (
        <div className="app-container">
            <h1>Task Manager</h1>

            <Routes>
                <Route path="/" element={<TasksPage />} />
                <Route path="/tasks/:id" element={<TaskViewPage />} />
                <Route path="/tasks/:id/edit" element={<TaskEditPage />} />
            </Routes>
        </div>
    );
}
