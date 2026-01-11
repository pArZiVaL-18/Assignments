import { useState, useRef, useEffect } from "react";
import "./App.css";
import Sender from "./components/Sender";
import Receiver from "./components/Receiver";
import TodoList from "./components/TodoList";

function App() {
    const [count, setCount] = useState(0);
    const [message, setMessage] = useState("");
    const [user, setUser] = useState(null);
    const inputRef = useRef(null);

    const handleClick = () => {
        inputRef.current.focus();
    };

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await fetch(
                    "https://jsonplaceholder.typicode.com/users"
                );
                const data = await response.json();
                setUser(data[0]); // first user
            } catch (error) {
                console.error("Error fetching user data:", error);
            }
        };

        fetchUser();
    }, []);

    return (
        <>
            <center>
                <h1>Assignment 1</h1>
                <div className="card">
                    <button onClick={() => setCount((count) => count + 1)}>
                        count is {count}
                    </button>
                </div>
                <br />
                <br />
                <h1>Passing data between Sibling Components</h1>
                <Sender onMessageChange={setMessage} />
                <Receiver message={message} />
                <br />
                <br />
                <h1>Employee Data</h1>
                <div style={{ padding: "20px" }}>
                    <h2>Todo List</h2>
                    <TodoList />
                </div>
                <br /> <br />
                <h1>Input Focus</h1>
                <div>
                    <input
                        ref={inputRef}
                        type="text"
                        placeholder="Click the button to focus me"
                    />
                    <br />
                    <br />
                    <button onClick={handleClick}>Focus Input</button>
                </div>
                <br />
                <br />
                <h1>User Data</h1>
                <div>
                    <h2>User Details</h2>
                    {user ? (
                        <>
                            <p>
                                <strong>Name:</strong> {user.name}
                            </p>
                            <p>
                                <strong>Email:</strong> {user.email}
                            </p>
                        </>
                    ) : (
                        <p>Loading...</p>
                    )}
                </div>
            </center>
        </>
    );
}

export default App;
