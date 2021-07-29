import React from "react";
import { GetServerSidePropsContext } from "next";
// import Head from "next/head";

import DefaultLayout from "layouts/Default";
import { Button } from "components/atoms";
import { TextInput } from "components/atoms";

export async function getServerSideProps(ctx: GetServerSidePropsContext) {
	return { props: {} };
}

function Index(ctx: GetServerSidePropsContext) {
	return (
		<DefaultLayout>
			<Button.Default label="sfesssf" />
			<Button.SubmitButton label="sfesf" intent="positive" />
			<TextInput.Default />
		</DefaultLayout>
	);
}

export default Index;
