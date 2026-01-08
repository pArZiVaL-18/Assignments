const http = require("http");
const { getMessage } = require("./module");
const PORT = 3000;

const server = http.createServer((req, res) => {
    if (req.url == "/" && req.method == "GET") {
        res.end("Hello from server!");
    }

    if (req.url == "/api" && req.method == "GET") {
        res.end("Welcome from Server!");
    }
});

console.log(getMessage());

server.listen(PORT, () => {
    console.log(`Server is listing to port ${PORT}`);
});
