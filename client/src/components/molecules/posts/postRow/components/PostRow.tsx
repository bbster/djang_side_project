import React from "react";

import { Post } from "module/forum/models/Post";
import PostMeta from "components/molecules/posts/post/components/PostMeta";
import { Points } from "components/molecules/posts/points";

import "../styles/PostRow.sass";
interface PostRowProps extends Post {
	onUpvoteClicked: () => void;

	onDownvoteClicked: () => void;

	isLoggedIn: boolean;
}

const PostRow: React.FC<PostRowProps> = (props) => (
	<div className="post-row">
		<Points
			onUpvoteClicked={() => props.onUpvoteClicked()}
			onDownvoteClicked={() => props.onDownvoteClicked()}
			points={props.points}
			isLoggedIn={props.isLoggedIn}
		/>

		<PostMeta {...props} />
	</div>
);

export default PostRow;
