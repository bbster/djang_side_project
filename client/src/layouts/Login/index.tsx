import React from "react";

import Styles from "./Login.module.scss";

interface ILoginProps {
	children?: React.ReactNode;
}
export default function Login({ children }: ILoginProps) {
	return <main className={Styles.main}>{children}</main>;
}
