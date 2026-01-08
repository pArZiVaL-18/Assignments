import { useState } from "react";
import TodoList from "./TodoList";

function App() {
    return (
        <>
            <div style={{ padding: "20px" }}>
                <h2>Todo List</h2>
                <TodoList />
            </div>
        </>
    );
}

export default App;
