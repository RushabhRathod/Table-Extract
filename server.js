const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
var engines = require("consolidate");
const path = require('path');


var corsOptions = { origin: "http://localhost:8081"}

const app = express();
app.use(cors(corsOptions));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, "/app/view")));
app.set('views', path.join(__dirname + "/app/view"))
app.enable('html', engines.mustache);
app.set('view engine', 'html');



const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log("server is running on port " + PORT);
})