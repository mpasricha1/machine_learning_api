import React, {useState, useEffect} from 'react';
// import Header from './components/Header';
import Banner from './components/Banner';
import {Header, Text} from './components/ContentBox';
import {Input, TextArea, FormBtn} from './components/Form';
import * as MainText from './utils/text';
import { Col, Row, Container } from "./components/Grid";


function App(){
  return (
    <>
      <Container fluid>
        <Row>
          <Col size = 'md-3'>
            <Header size='5' hText='Current Model Accuracy'/>
          </Col>
          <Col size = 'md-9'>
            <Banner />
            <Row>
              <Header size='3' hText='Overview'/>
            </Row>
            <Row>
              <Text text={MainText.overviewText} / >
            </Row>
            <Row>
              <Header size='3' hText='Current Models'/>
            </Row>
            <Row>
              <Header size='6' hText='Clothing Image Classifier'/>
            </Row>
            <Row>
              <Header size='6' hText='About'/>
            </Row>
            <Row>
              <Text text={MainText.cnnAboutText1} / >
            </Row>
            <Row>
              <Text text={MainText.cnnAboutText2} / >
            </Row>
            <Row>
              <Header size='6' hText='Usage'
              />
            </Row>
            <Row>
              <Text text={MainText.apiCallText} / >
            </Row>
            <Row>
              <Text text={MainText.apiCallUsage} / >
            </Row>
            <Row>
              <Header size = '3' hText='Try it Yourself'/>
            </Row>
            <Row>
              <Text text={MainText.tryText} / >
            </Row>
            <Row>
              <form>
                <Input name='url' placeholder='Image URL'/>
                <FormBtn>Submit</FormBtn>
              </form>
            </Row>
          </Col>
        </Row>
        
      </Container>
    </>
  )

}

export default App;
