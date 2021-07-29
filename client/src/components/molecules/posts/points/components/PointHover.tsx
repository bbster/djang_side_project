import React from "react";
import Link from "next/link";
import "../styles/PointHover.sass";

interface PostPointsProps {
	isHover: boolean;
}

const PointHover: React.FC<PostPointsProps> = (props) => (
	<div className={`post-points-hover ${props.isHover && "is-hover"}`}>
		<p>
			Want to vote? You need to sign up
			<Link href="/login"> Here</Link>
		</p>
	</div>
);

export default PointHover;
