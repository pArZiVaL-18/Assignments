const express = require("express");
const fs = require("fs");
const path = require("path");
const ejsMate = require("ejs-mate");
const multer = require("multer");

const app = express();
const PORT = 8080;

// Middlewares
app.use(express.json()); // used to parse json data (content type : application/json)
app.use(express.urlencoded({ extended: true })); // used to parse form data (content type: application/x-www-form-urlencoded)
app.set("view engine", "ejs"); // it tells express that we are using embedded javascript for templeting
app.engine("ejs", ejsMate);

// Helper functions : to read and write data in json files
const dataPath = path.join(__dirname, "/data/tasks.json");

function readData() {
    const data = fs.readFileSync(dataPath, "utf-8");
    return JSON.parse(data);
}

function writeData(data) {
    fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}

// Routes

// multer storage set up
const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, "uploads/"),
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    },
});
const upload = multer({ storage });

// Handling file upload
app.post("/upload", upload.single("file"), (req, res) => {
    res.json({
        message: "File uploaded successfully!",
        filename: req.file.filename,
    });
});

app.get("/time", (req, res) => {
    const now = new Date();

    res.json({
        timestamp: now.getTime(),
        iso: now.toISOString(),
        time: now.toLocaleTimeString(),
        date: now.toLocaleDateString(),
    });
});

app.get("/", (req, res) => {
    res.send("Server is started!");
});
// Index route
app.get("/tasks", (req, res) => {
    const data = readData();
    res.render("index", { tasks: data.tasks });
});

// Routes for creatig new task
app.get("/tasks/new", (req, res) => {
    // Render form for creating new task
    res.render("newTask");
});

app.post("/tasks/create", (req, res) => {
    // reads data from form and create new object and writes it back in json data file
    const data = readData();

    const newTask = {
        id: data.tasks.length + 1,
        title: req.body.title,
        description: req.body.description,
        status: req.body.status,
        priority: req.body.priority,
    };

    data.tasks.push(newTask);
    writeData(data);

    res.redirect("/tasks");
});

// update/change a particular task
app.get("/tasks/:id/edit", (req, res) => {
    // matches the id of the record which we want to update and renders data of that record in form to update
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).send("Task not found");
    }

    res.render("editTask", { task });
});

app.post("/tasks/:id/update", (req, res) => {
    // reads data from form and updates it in json file and redirect to home page
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).send("Task not found");
    }

    task.title = req.body.title;
    task.description = req.body.description;
    task.status = req.body.status;
    task.priority = req.body.priority;

    writeData(data);
    res.redirect("/tasks");
});

// GET single task
app.get("/tasks/:id", (req, res) => {
    // views a particular task
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).json({ message: "Task not found" });
    }
    res.render("viewTask", { task });
    // res.json(task);
});

// DELETE task
app.post("/tasks/:id/delete", (req, res) => {
    const data = readData();
    data.tasks = data.tasks.filter((t) => t.id !== Number(req.params.id));
    writeData(data);

    res.status(204).redirect("/tasks");
});

app.listen(PORT, () => {
    console.log(`Server running on https://localhost:${PORT}`);
});
