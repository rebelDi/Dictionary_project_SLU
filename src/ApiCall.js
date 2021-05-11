import axios from "axios";

const apiCall = async (language, word, partOfSpeech,numberOfCluster, setMeanings) => {
  try {
    console.log(`http://localhost:3080/words/${word}/${language}/${partOfSpeech}/${numberOfCluster}`);
    const response = await axios.get(
      `http://localhost:3080/words/${word}/${language}/${partOfSpeech}/${numberOfCluster}`
    );

     setMeanings(response.data);
  } catch (error) {
    console.log(error);
  }
};

export default apiCall;
