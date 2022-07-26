const http = require('http');
const express = require('express');

const app = express();
app.get('/', (req, res) => {
    res.send('hello world.');
});
const server = http.Server(app2);
server2.listen(80, () => {

});