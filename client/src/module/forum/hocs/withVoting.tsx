import React from "react";
import { IForumOperations } from "../redux/operators";
import { ForumState } from "../redux/states";

interface IWrappedComponentProps extends React.FC<any> {
	upvoteComment: any;
	downvoteComment: any;
	upvotePost: any;
	downvotePost: any;
}
interface withVotingProps extends IForumOperations {
	users: ForumState;
}

function withVoting(WrappedComponent: IWrappedComponentProps) {
	class HOC extends React.Component<withVotingProps, any> {
		constructor(props: withVotingProps) {
			super(props);
		}

		handleUpvoteComment(commentId: string) {
			this.props.upvoteComment(commentId);
		}

		handleDownvoteComment(commentId: string) {
			this.props.downvoteComment(commentId);
		}

		handleUpvotePost(postSlug: string) {
			this.props.upvotePost(postSlug);
		}

		handleDownvotePost(postSlug: string) {
			this.props.downvotePost(postSlug);
		}

		render() {
			return (
				<WrappedComponent
					upvoteComment={(commentId: string) =>
						this.handleUpvoteComment(commentId)
					}
					downvoteComment={(commentId: string) =>
						this.handleDownvoteComment(commentId)
					}
					upvotePost={(slug: string) => this.handleUpvotePost(slug)}
					downvotePost={(slug: string) =>
						this.handleDownvotePost(slug)
					}
					users={this.props.users}
				/>
			);
		}
	}
	return HOC;
}

export default withVoting;
