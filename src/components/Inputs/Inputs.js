import React from "react";
import { TextField, MenuItem, IconButton } from "@material-ui/core";
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
  meanings,
}) => {
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
          apiCall(language, word, partOfSpeech, setMeanings);
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
    </div>
  );
};
export default Inputs;
