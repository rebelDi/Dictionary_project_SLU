const express = require("express");
const cors = require('cors')
const app = express();

app.use(cors())

//import Routes

const postRoute = require("./routes/words");

app.use('/words',postRoute);

//Routes
app.get("/", (req, res) => {
  res.send("Welcome");
});

//Listening server
app.listen(3080);
