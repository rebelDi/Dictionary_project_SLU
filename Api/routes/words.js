const express = require("express");
const Words = require("../models/Word");
const router = express.Router();
let { PythonShell } = require("python-shell");
const Word = require("../models/Word");

router.get("/", (req, res) => {
  res.send("Get posts");
});

router.get(
  "/:word/:language/:partofspeech/:numberofcluster",
  async (req, res) => {
    try {
      let options = {
        mode: "text",
        pythonOptions: ["-u"], // get print results in real-time
        scriptPath: "../back end",
        args: [
          req.params.word,
          req.params.language,
          req.params.partofspeech,
          req.params.numberofcluster,
        ],
      };

      PythonShell.run("main.py", options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution 
        // results = JSON.stringify(results)
        res.send(results.toString().replace(/\\|\//g,'').replace(/'/g,'"'));
      });
    } catch (error) {
      res.json({ message: error });
    }
  }
);

router.post("/", (req, res) => {
  console.log(req.body);
});

module.exports = router;
