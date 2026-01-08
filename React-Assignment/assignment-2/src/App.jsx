import { useState } from "react";
import Sender from "./Sender";
import Receiver from "./Receiver";
import "./style.css";

function App() {
    const [message, setMessage] = useState("");

    return (
        <div style={{ padding: "20px" }}>
            <center>
                <h2>Passing Data Between Sibling Components</h2>
            </center>

            <div className="childs">
                <Sender onMessageChange={setMessage} />
                <Receiver message={message} />
            </div>
        </div>
    );
}

export default App;
