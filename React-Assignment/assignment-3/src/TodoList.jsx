function TodoList() {
    const tasks = [
        { id: 1, text: "Learn React" },
        { id: 2, text: "Practice JSX" },
        { id: 3, text: "Build a Todo App" },
    ];

    return (
        <ul>
            {tasks.map((task) => (
                <li key={task.id}>{task.text}</li>
            ))}
        </ul>
    );
}

export default TodoList;
