import React, {useState, useEffect} from 'react'; 
import axios from 'axios';

function App(){
  const [prediction, setPrediction] = useState(0); 

  useEffect(() => {
    axios.post('/api/predict')
      .then(function(response){
        console.log(response)
      })
      // setPrediction(data.type)
  }, []);

  return (
    <div className="App">
      <p></p>
    </div>
  )

}

export default App;
