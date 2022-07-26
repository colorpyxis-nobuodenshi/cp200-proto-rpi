const http = require('http');
const net = require('net');
const WebSocket = require('ws');

const server = http.Server(app);
const PORT = 8080;
const wss = new WebSocket.Server({ server:server, path:'/api' });

server.listen(PORT, () => {
    //console.log('server listening. port' + PORT)
});

// var wslisteners = []

// var client1 = new net.Socket();
// client1.setEncoding('utf8');
// client1.connect('/tmp/request.sock');
// client1.on('connect', () => {
//     console.log('request server socket connected.')
// });

// client1.on('error', (err) => {
//     console.log(err.message);
// });
// client1.on('data', (data) => {
//     wss.broadcast(data);
//     console.log(data);
// });

// var client2 = new net.Socket();
// client2.setEncoding('utf8');
// client2.connect('/tmp/response.sock');
// client2.on('connect', () => {
//     console.log('notification server socket connected.')
// });

// client2.on('error', (err) => {
//     console.log(err.message);
// });
// client2.on('data', (data) => {
//     wss.broadcast(data);
//     console.log(data);
// });

var backendConnected = false;
var client = new net.Socket();
client.setEncoding('utf8');
client.on('data', (data) => {
    //console.log('res:'+data);
    //var msg = JSON.parse(data);
    //ws.send(JSON.stringify(msg.message));
    wss.broadcast(data);
});
client.on('error', (err) => {
    console.log("error : " + err.message);
});
client.on('close', (err) =>{
    console.log("backend communication socket close.");
    backendConnected = false;
});

wss.broadcast = (data) => {
    wss.clients.forEach((client)=>{
        if(client.readyState === WebSocket.OPEN){
            console.log(data);
            var message = JSON.parse(data);
            client.send(JSON.stringify(message.message));
        }
    });
};

wss.on('connection', (ws) => {
    //wslisteners.push(ws);

    //console.log("websocket client connected.");
    if(!backendConnected){
        client.connect('/tmp/request.sock',()=>{
            console.log("backend communication socket open.");
        });
        backendConnected = true;
    }

    ws.on('message', (message) => {
        client.write(JSON.stringify({'payload':'change','message':JSON.parse(message)}));

        console.log(JSON.stringify({'payload':'change','message':JSON.parse(message)}));
    });
});