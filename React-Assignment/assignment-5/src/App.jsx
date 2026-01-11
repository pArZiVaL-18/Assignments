import React, { useEffect, useState } from "react";

function App() {
    const [user, setUser] = useState(null);

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
    }, []); // runs once on component mount

    return (
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
    );
}

export default App;
