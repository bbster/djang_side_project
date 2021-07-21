import React from "react";

interface IDefaultProps {
	children?: React.ReactNode;
}
export default function Default({ children }: IDefaultProps) {
	return <main>{children}</main>;
}
