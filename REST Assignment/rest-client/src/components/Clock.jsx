import { useEffect, useState } from "react";

export default function Clock() {
    const [time, setTime] = useState("Connecting...");

    useEffect(() => {
        const socket = new WebSocket("ws://localhost:8080");

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setTime(data.time);
        };

        socket.onerror = () => {
            setTime("Connection error");
        };

        socket.onclose = () => {
            console.log("WebSocket closed");
        };

        return () => {
            socket.close();
        };
    }, []);

    return (
        <div className="clock">
            <h3>Current Time</h3>
            <p>{time}</p>
        </div>
    );
}
