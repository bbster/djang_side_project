import React from "react";

import moment from "moment";

import Link from "next/link";

import { Post } from "module/forum/models/Post";

import "../styles/PostMeta.sass";

interface PostMetaProps extends Post {
	includeLink?: boolean;
}

const PostMeta: React.FC<PostMetaProps> = (props) => (
	<div className="post-row-content">
		{props.includeLink === false ? (
			""
		) : (
			<Link href={`/discuss/${props.slug}`}>
				<a className="title">
					{props.title}
					{props.link ? <span className="link">[link]</span> : ""}
				</a>
			</Link>
		)}

		<div className="post-row-meta">
			{moment(props.createdAt).fromNow()} | {"by "}{" "}
			<Link href={`/member/${props.postAuthor}`}>{props.postAuthor}</Link>{" "}
			| {`${props.numComments} comments`}
		</div>
	</div>
);

export default PostMeta;
