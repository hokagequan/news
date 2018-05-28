import express from 'express';
import controller from './controllers';

let server = express();
let port = 3000;

server.use("/api/", controller);

server.listen(port, function() {
	console.log(`listening on port : ${port}`)
})