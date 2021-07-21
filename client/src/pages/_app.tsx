import React from "react";
import { NextComponentType } from "next";
import { AppContext, AppInitialProps, AppProps } from "next/app";

import { globalStyles } from "shared/styles";

const CustomApp: NextComponentType<AppContext, AppInitialProps, AppProps> = ({
	Component,
	pageProps,
}) => {
	return (
		<>
			{globalStyles}
			<Component {...pageProps} />
		</>
	);
};

export default CustomApp;
