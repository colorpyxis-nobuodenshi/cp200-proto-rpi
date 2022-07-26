const http = require('http');
const express = require('express');

const app = express();
const server = http.Server(app);
const PORT = 8080;

app.use(express.static('public'));
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

server.listen(PORT, () => {
    //console.log('server listening. port' + PORT)
});