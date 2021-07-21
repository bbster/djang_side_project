import React from "react";
import { NextPage, NextPageContext } from "next";

interface IErrorProps {
	statusCode: number | undefined;
}

const CustomError: NextPage<IErrorProps> = ({ statusCode }) => (
	<p>{statusCode}</p>
);

CustomError.getInitialProps = async ({ res, err }: NextPageContext) => {
	const statusCode = res ? res.statusCode : err ? err.statusCode : 404;
	return { statusCode };
};

export default CustomError;
