const mongoose = require("mongoose");

const WordSchema = mongoose.Schema({
  word: { type: String, required: true },
  language: { type: String, required: true },
  partOfSpeech: { type: String, required: true },
  numberOfCluster: { type: Number, required: true },
});

module.exports = mongoose.model("Words", WordSchema);
