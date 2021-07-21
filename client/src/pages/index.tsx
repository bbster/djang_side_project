import React from "react";
import Head from "next/head";

import DefaultLayout from "layouts/default";
import { Button } from "components";

const TITLE = "팬딩 - 크리에이터와 팬이 가장 가까운 곳";
const Index = () => {
	return (
		<>
			<Head>
				<title>{TITLE}</title>
				<meta name="description" content="" />
				<meta name="keywords" content="" />
			</Head>
			<DefaultLayout></DefaultLayout>
		</>
	);
};
export default Index;
