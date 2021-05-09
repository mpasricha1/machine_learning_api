import React from "react"; 

export function Header(props){
	const HeaderTag = `h${props.size}`
	return (
		<HeaderTag>{props.hText}</HeaderTag>
	)
}

export function Text(props){
	return (
		<p>{props.text}</p>
	)
}
