import React from "react";
import styled, { StyledComponent } from "@emotion/styled";

export interface ButtonProps {
	className?: string;
	label?: string | React.ReactElement;
	onClick?: () => void;
}

const Component: StyledComponent<ButtonProps> = styled.button(({ theme }) => ({
	outline: "none",
	background: "white",
	padding: "0.5rem",
	cursor: "pointer",
	color: "black",
}));

const Default: React.FC<ButtonProps> = (props) => {
	return <Component {...props}>{props.label}</Component>;
};

export default Default;
