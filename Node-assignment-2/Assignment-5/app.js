const express = require("express");
const axios = require("axios");

const app = express();
const PORT = 3000;
app.use(express.json()); // to parse json data, imp for post route

// middleware to log request method and request url
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

app.get("/", (req, res) => {
    res.send("Welcome to Express Server!");
});

app.post("/data", (req, res) => {
    console.log(req.body);
    res.send("Data received.");
});

app.get("/users", (req, res) => {
    res.json([
        { id: 1, name: "Roshan" },
        { id: 2, name: "Sujal" },
        { id: 3, name: "Chaitanya" },
        { id: 4, name: "Pranav" },
    ]);
});

// external posts request
app.get("/externalposts", async (req, res, next) => {
    try {
        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts"
        );
        res.json(response.data);
    } catch (error) {
        next(error);
    }
});

// 404 not found middleware
app.use((req, res) => {
    res.status(404).send("Route not found");
});

// Middleware to handle errors
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send("Something went wrong!");
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
