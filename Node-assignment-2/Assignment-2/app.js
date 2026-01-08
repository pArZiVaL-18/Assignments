const fs = require("fs");
const filename = "log.txt";

// Use of fs module
// checks if file exists or not and create a new if not exists.
if (!fs.existsSync(filename)) {
    fs.writeFileSync(filename, "This is the first log\n");
    console.log("File is created!");
}

// this adds a new log each time script is executed.
const logMessage = `Log update at ${new Date().toISOString()}\n`;
fs.appendFileSync(filename, logMessage);
console.log("New log appended");

// Simulation of blocking vs. Non-blocking
// readFileSync() blocks the event loop till the reading of file is completed. execution is top to bottom.
function readFileBlocking() {
    console.log("Text before starting a blocking synchronous task.");
    const data = fs.readFileSync(filename, "utf-8");
    console.log(data);
    console.log("Text after completion of a blocking sync task.");
}

// readFile() doesn't blocks the event loop.
function readFileNonBlocking() {
    console.log("Text before non-blocking work starts.");

    fs.readFile(filename, "utf-8", (err, data) => {
        if (err) {
            console.log(err);
        }
        console.log(data);
    });

    console.log(
        "Text after the non-blocking task. Even though it is logged after the readFile, it still get executed before the readFile gets executed, because readFile is asynchronous it doesn't blocks the event loop like the readFileSync()."
    );
}

console.log("\nCalling event loop blocking function : ");
readFileBlocking();

console.log("\nCalling Event loop non-blocking function : ");
readFileNonBlocking();

console.log(
    "\nLog message after calling non-blocking function, still it will get logged before readFile execution begins"
);

// Event loop demo
console.log("Event loop practice first message.");

// this goes is macrotask queue or the callback queue. which is picked up by event loop after microtask queue. this queue contains all the callbacks, I/O results etc.
setTimeout(() => {
    console.log("Log message from setTimeout");
}, 0);

// this goes in microtask queue, event loop picks task from this queue after process.tick queue. this queue contains all the promises, catch, finally etc.
setImmediate(() => {
    console.log("Log message from setImmidiate");
});

// this blocks everything and executes first, it goes in process.tick queue (queue from which the event loop picks tasks first)
process.nextTick(() => {
    console.log("Log message from process.nextTick");
});

// So the order is
// synchronous tasks > process.nextTick > setImmediate > setTimeout
// call stack > process.nextTick queue > microtask queue > macrotask queue

console.log("event loop demo end message");
