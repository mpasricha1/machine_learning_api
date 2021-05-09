import React from 'react'
import {Header, Text} from '../ContentBox';
import {Row, Container } from '../Grid';
import {bannerText} from '../../utils/text';


function Banner(){
	return (
		<Container>
			<Row>
				 <Header 
          			size = '1'
          			hText='Machine Learning API'
        		/>
        		<Header
        			size = '5'
					hText='Release v1'
				/>
				<Text
					text={bannerText} 
				/>
			</Row>
		</Container>
	)
}
export default Banner;
