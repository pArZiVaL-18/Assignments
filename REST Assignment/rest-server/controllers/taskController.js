const { readData, writeData } = require("../utils/fileHandler");

exports.getAllTasks = (req, res) => {
    const data = readData();
    res.json(data.tasks);
};

exports.getTaskById = (req, res) => {
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).json({ message: "Task not found" });
    }

    res.json(task);
};

exports.createTask = (req, res) => {
    const data = readData();

    console.log(req.body);
    const newTask = {
        id: data.tasks.length + 1,
        ...req.body,
    };

    data.tasks.push(newTask);
    writeData(data);
    // console.log("data saved" + data);
    res.status(201).json(newTask);
};

exports.updateTask = (req, res) => {
    const data = readData();
    const task = data.tasks.find((t) => t.id === Number(req.params.id));

    if (!task) {
        return res.status(404).json({ message: "Task not found" });
    }

    Object.assign(task, req.body);
    writeData(data);

    res.json(task);
};

exports.deleteTask = (req, res) => {
    const data = readData();
    data.tasks = data.tasks.filter((t) => t.id !== Number(req.params.id));
    writeData(data);

    res.status(204).end();
};
