import React from "react";
import styled, { StyledComponent } from "@emotion/styled";

export interface TextInputProps {
	className?: string;
	placeholder?: string;
	onChange?: (val: string) => void;
	type?: string;
}

const Component: StyledComponent<TextInputProps> = styled.input(
	({ theme }) => ({
		display: "block",
		padding: "0.6rem 1rem 0.6rem 1rem",
		borderRadius: " 3px",
		border: "solid 3px #000000c9",
		width: "100%",
		marginBottom: " 0.5rem",
		color: "#000000d6",
		transition: "0.2s all",
		fontSize: "1rem",
		boxSizing: "border-box",
		"&:hover": {
			background: "#fbfbfb",
		},
	}),
);

const Default: React.FC<TextInputProps> = (props) => {
	return <Component {...props} type={props.type ? props.type : "text"} />;
};

export default Default;
