import axios from "axios";

const apiCall = async (language, word,setMeanings) => {
  try {
    const response = await axios.get(
      `https://api.dictionaryapi.dev/api/v2/entries/${language}/${word}`
    );

    
    setMeanings(response.data);
  } catch (error) {

    console.log(error);
  }
};

export default apiCall;
