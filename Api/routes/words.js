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
          encodeURI(req.params.word),
          req.params.language,
          req.params.partofspeech,
          req.params.numberofcluster,
        ],
      };

      const filename = "main.py";
      if (req.params.numberofcluster == 1) options.args[3] = "-1";
      PythonShell.run(filename, options, function (err, results) {
        console.log(filename, options.args[3],options.scriptPath);
        if (err) res.json({ message: err });
        if (results !== null) results = decodeURI(results);
        res.send(
          results
          // .toString()
          // .replace(/\\|\//g, "")
          // .replace(/'/g, '"')
          // .replace(/""|" "/g, '"')
          // .replace(/, "|,"/g, ",")
          // .replace(/,example/g, `,"example`)
        );
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
