import React from "react";
import Document, {
	Html,
	Main,
	Head,
	NextScript,
	DocumentContext,
} from "next/document";
class CustomDocument extends Document<{}> {
	static async getInitialProps(ctx: DocumentContext) {
		const initialProps = await Document.getInitialProps(ctx);
		return initialProps;
	}
	render() {
		return (
			<Html>
				<Head />
				<body>
					<Main />
					<NextScript />
				</body>
			</Html>
		);
	}
}

export default CustomDocument;
