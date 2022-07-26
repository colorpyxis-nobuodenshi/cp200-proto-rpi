const http = require('http');
// const net = require('net');
const express = require('express');
// const WebSocket = require('ws');
const socketio = require('socket.io');
var redis = require("redis");

const app = express();
const server = http.Server(app);
const PORT = 8080;
// const wss = new WebSocket.Server({ server:server, path:'/api' });
const io = socketio.listen(server);
//io.set('transports', ['websocket']);      
const api = io.of('/api');

const subscriber = redis.createClient();
const publisher  = redis.createClient();

app.use(express.static('public'));
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

server.listen(PORT, () => {
    //console.log('server listening. port' + PORT)

});

api.on('connection', (socket) => {

    socket.on('change', (message) => {
        console.log(message);
        publisher.publish('change', message);
    });
});

subscriber.on("message", function(channel, message) {
    console.log("Message '" + message + "' on channel '" + channel + "' arrived!")
    api.emit('status', message);
});

subscriber.subscribe("status");

// setInterval(
//     () => {
//         publisher.publish("change", JSON.stringify({'illuminant':5000, 'power':100, 'on': true}));
//     },1000);

    