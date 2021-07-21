import React from "react";
import { css, Global } from "@emotion/react";

export const globalStyles = (
	<Global
		styles={css`
			html,
			body {
				min-height: 100%;
				margin: 0;
				font-family: Helvetica, Arial, sans-serif;
				font-size: 24px;
				background: #ffffff;
			}
		`}
	/>
);

export const resetStyles = css`
	h1,
	h2,
	h3,
	h4,
	h5,
	h6 {
		margin: 0;
	}
`;
