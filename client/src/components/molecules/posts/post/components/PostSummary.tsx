import React from "react";
import PostMeta from "./PostMeta";
import { Post } from "module/forum/models/Post";
import { TextUtil } from "module/shared/utils/TextUtil";

import "../styles/PostSummary.sass";

type PostProps = Post;

const PostSummary: React.FC<PostProps> = (props) => (
	<div className="post">
		<PostMeta {...props} includeLink={false} />
		{props.text ? (
			<div dangerouslySetInnerHTML={{ __html: props.text }} />
		) : (
			<a
				className="link"
				target="_blank"
				href={props.link}
				rel="noreferrer"
			>
				Click to visit the link at{" "}
				{TextUtil.getDomainNameFromUrl(props.link)}
			</a>
		)}
	</div>
);

export default PostSummary;
