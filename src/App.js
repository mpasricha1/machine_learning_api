import React, {useState, useEffect} from 'react';
// import Header from './components/Header';
import Banner from './components/Banner';
import {Header, Text} from './components/ContentBox';
import axios from 'axios';
import {overviewText, usageText, tryText} from './utils/text';
import { Col, Row, Container } from "./components/Grid";


function App(){
  // const [prediction, setPrediction] = useState(0); 

  // useEffect(() => {
  //   axios.post('/api/predict')
  //     .then(function(response){
  //       console.log(response)
  //     })
  //     // setPrediction(data.type)
  // }, []);

  console.log(overviewText)

  return (
    <>
      <Container>
        <Row>
          <Banner />
        </Row>
        <Row>
          <Header 
            size = '3'
            hText='Overview'
          />
        </Row>
        <Row>
          <Text text={overviewText} / >
        </Row>
        <Row>
          <Header 
            size = '3'
            hText='Usage'
          />
        </Row>
        <Row>
          <Text text={usageText} / >
        </Row>
        <Row>
          <Header 
            size = '3'
            hText='Try it Yourself'
          />
        </Row>
        <Row>
          <Text text={tryText} / >
        </Row>
      </Container>
    </>
  )

}

export default App;
