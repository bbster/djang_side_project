import React from "react";
import styled, { StyledComponent } from "@emotion/styled";

import Loader from "react-loader-spinner";

export interface LoaderProps {
	className?: string;
}

const Component: StyledComponent<LoaderProps> = styled.button(({ theme }) => ({
	position: "absolute",
	top: 0,
	left: "0",
	right: "0",
	bottom: "0",
	background: "#00000024",
	display: "flex",
	alignItems: "center",
	justifyContent: "center",
}));

const Default = () => (
	<Component>
		<Loader type="Rings" color="#6a69ff" height={100} width={100} />
	</Component>
);

export default Default;
