const fs = require("fs");
const path = require("path");

const dataPath = path.join(__dirname, "..", "data", "tasks.json");

function readData() {
    return JSON.parse(fs.readFileSync(dataPath, "utf-8"));
}

function writeData(data) {
    fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}

module.exports = { readData, writeData };
