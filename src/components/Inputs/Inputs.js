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
  meanings,
  setMeanings,
  setNumberOfCluster,
  numberOfCluster,
  t,
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
        label={t("Search a Word")}
        onChange={(e) => setWord(e.target.value)}
      />
      <IconButton
        color="primary"
        aria-label="search a word"
        onClick={(e) => {
          console.log(word, numberOfCluster);
          apiCall(language, word, partOfSpeech, numberOfCluster, setMeanings);
        }}
      >
        <Search />
      </IconButton>

      <br />
      <br />
      <TextField
        select
        label={t("Part of Speech")}
        value={partOfSpeech}
        onChange={(e) => setPartOfSpeech(e.target.value)}
        className="part_of_speech_field"
      >
        {poSpeech.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {t(item.value)}
          </MenuItem>
        ))}
      </TextField>

      <TextField
        className="language_selector"
        select
        label={t("Language")}
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        {languages.map((item) => (
          <MenuItem key={item.label} value={item.label}>
            {t(item.value)}
          </MenuItem>
        ))}
      </TextField>
      {meanings.length !== 0 ? (
        <div>
          <Typography id="discrete-slider-small-steps" gutterBottom>
            {t("Number of Cluster")}
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
            onChangeCommitted={(e) => {
              apiCall(
                language,
                word,
                partOfSpeech,
                numberOfCluster,
                setMeanings
              );
            }}
          />
        </div>
      ) : null}
    </div>
  );
};
export default Inputs;
