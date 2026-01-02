const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 8080;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");

// Helper functions
const dataPath = path.join(__dirname, "/data/tasks.json");

function readData() {
    const data = fs.readFileSync(dataPath, "utf-8");
    return JSON.parse(data);
}

function writeData(data) {
    fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}

// Routes

// GET all tasks (API)
app.get("/tasks", (req, res) => {
    const data = readData();
    res.json(data.tasks);
});

// GET single task (API)
app.get("/tasks/:id", (req, res) => {
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).json({ message: "Task not found" });
    }
    res.json(task);
});

// Render tasks (EJS)
app.get("/tasks-view", (req, res) => {
    const data = readData();
    res.render("index", { tasks: data.tasks });
});

// POST create task
app.post("/tasks", (req, res) => {
    const data = readData();

    const newTask = {
        id: Date.now(),
        title: req.body.title,
        description: req.body.description,
        status: "PENDING",
        priority: "MEDIUM",
    };

    data.tasks.push(newTask);
    writeData(data);

    res.status(201).json(newTask);
});

// DELETE task
app.delete("/tasks/:id", (req, res) => {
    const data = readData();
    data.tasks = data.tasks.filter((t) => t.id !== Number(req.params.id));
    writeData(data);

    res.status(204).send();
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
