import React from "react";
import styled, { StyledComponent } from "@emotion/styled";

import { ButtonProps } from "./Default";

interface SubmitButtonProps extends ButtonProps {
	intent?: "positive" | "negative";
}

const Component: StyledComponent<SubmitButtonProps> = styled.button((props) => {
	return {
		border: "none",
		outline: "none",
		padding: "0.5rem",
		cursor: "pointer",
		background: "green",
		...(props.intent === "positive" && {
			color: "white",
		}),
		...(props.intent === "negative" && {
			color: "black",
		}),
	};
});

const SubmitButton: React.FC<SubmitButtonProps> = (props) => {
	return <Component {...props}>{props.label}</Component>;
};

export default SubmitButton;
