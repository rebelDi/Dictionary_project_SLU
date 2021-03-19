const express = require("express");
const Words = require("../models/Word");
const router = express.Router();
let { PythonShell } = require("python-shell");
const Word = require("../models/Word");

router.get("/", (req, res) => {
  res.send("Get posts");
});

// router.get("/:word/:language/:partofspeech/:numberofcluster", (req, res) => {
//   const word = new Words({
//     word: req.params.word,
//     language: req.params.language,
//     partOfSpeech: req.params.partofspeech,
//     numberOfCluster: req.params.numberofcluster,
//   });

//   // let options = {
//   //   mode: "text",
//   //   pythonOptions: ["-u"], // get print results in real-time
//   //   scriptPath: "../back end",
//   //   args: [word.word, word.language, word.partOfSpeech,word.numberOfCluster],
//   // };

//   // PythonShell.run("clustering.py", options, function (err, results) {
//   //   if (err) throw err;
//   //   // results is an array consisting of messages collected during execution
//   //   console.log("results: %j", results);

//   res.json(word);
// });

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

      PythonShell.run("clustering.py", options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        res.json(results.toString().replace(/(\r\n|\\n|\\r)/gm, " "));
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
