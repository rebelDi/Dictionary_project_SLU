import axios from "axios";

const apiCall = async (language, word, partOfSpeech, setMeanings) => {
  try {
    // const response = await axios.get(
    //   `https://api.dictionaryapi.dev/api/v2/entries/${language}/${word}`
    // );

    const response = await axios.get(
      `http://localhost:3080/words/${word}/${language}/${partOfSpeech}/2`
    );

    setMeanings(response.data);
  } catch (error) {
    console.log(error);
  }
};

export default apiCall;
