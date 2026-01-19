const express = require("express");
const cors = require("cors");
const multer = require("multer");
const path = require("path");
const http = require("http");
const WebSocket = require("ws");
// const moment = require("moment");
const moment = require("moment-timezone");

const taskRoutes = require("./routes/taskRoutes");

const app = express();
const PORT = 8080;

app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());
app.use("/uploads", express.static("uploads"));

const storage = multer.diskStorage({
    destination: "uploads/",
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    },
});
const upload = multer({ storage });

app.post("/api/upload", upload.single("file"), (req, res) => {
    res.json({
        filename: req.file.filename,
        url: `/uploads/${req.file.filename}`,
    });
});

app.use("/api/tasks", taskRoutes);

// server for realtime connection
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

wss.on("connection", (ws) => {
    console.log("WebSocket client connected");

    const interval = setInterval(() => {
        const now = new Date();
        const lostime = moment()
            .tz("America/New_York")
            .format("YYYY-MM-DD HH:mm:ss");
        ws.send(
            JSON.stringify({
                time: lostime,
                timestamp: now.getTime(),
            }),
        );
    }, 1000);

    ws.on("close", () => {
        console.log("WebSocket client disconnected");
        clearInterval(interval);
    });
});

server.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
    console.log(`WebSocket running on ws://localhost:${PORT}`);
});
