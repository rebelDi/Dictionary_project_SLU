import React from "react";
import {
  TextField,
  MenuItem,
  IconButton,
  Slider,
  Typography,
} from "@material-ui/core";
import { Search } from "@material-ui/icons";
import "./Inputs.css";
import languages from "../../data/languages";
import poSpeech from "../../data/partofspeech";
import apiCall from "../../ApiCall";

const Inputs = ({
  language,
  setLanguage,
  partOfSpeech,
  setPartOfSpeech,
  word,
  setWord,
  setMeanings,
  setNumberOfCluster,
  numberOfCluster,
}) => {
  function valuetext(value) {
    setNumberOfCluster(value);
    return `${value}`;
  }

  return (
    <div className="inputs">
      <br />
      <TextField
        className="search_field"
        id="filled-basic"
        value={word}
        label="Search a Word"
        onChange={(e) => setWord(e.target.value)}
      />
      <IconButton
        color="primary"
        aria-label="add an alarm"
        onClick={(e) => {
          apiCall(language, word, partOfSpeech, numberOfCluster, setMeanings);
        }}
      >
        <Search />
      </IconButton>

      <br />
      <br />
      <TextField
        select
        label="Part of Speech"
        value={partOfSpeech}
        onChange={(e) => setPartOfSpeech(e.target.value)}
        className="part_of_speech_field"
      >
        {poSpeech.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {item.value}
          </MenuItem>
        ))}
      </TextField>

      <TextField
        className="language"
        select
        label="Language"
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="language_select"
      >
        {languages.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {item.value}
          </MenuItem>
        ))}
      </TextField>

      <Typography id="discrete-slider-small-steps" gutterBottom>
        {" Number Of Cluster "}
      </Typography>
      <Slider
        defaultValue={2}
        getAriaValueText={valuetext}
        aria-labelledby="discrete-slider-small-steps"
        step={1}
        marks
        min={2}
        max={10}
        color="secondary"
        valueLabelDisplay="auto"
        onChange={valuetext}
      />
    </div>
  );
};
export default Inputs;
