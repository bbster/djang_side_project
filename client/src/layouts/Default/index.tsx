import React from "react";

import Styles from "./Default.module.scss";

interface IDefaultProps {
	children?: React.ReactNode;
}
export default function Default({ children }: IDefaultProps) {
	return <main className={Styles.main}>{children}</main>;
}
