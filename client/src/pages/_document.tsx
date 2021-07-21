import React from "react";
import Document, {
	Html,
	Head,
	Main,
	NextScript,
	DocumentContext,
} from "next/document";

interface IDocumentProps {
	styleTags: Array<React.ReactElement<{}>>;
}
const META = {
	viewport:
		"width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, shrink-to-fit=no",
	description: "팬딩 - 크리에이터와 팬이 가장 가까운 곳",
	keywords:
		"위시빈, 여행일정, 여행정보, 여행꿀팁, 세계여행정보, 국내여행정보, 해외여행정보, 여행팁, 자유여행, 자유여행준비, 가이드북, 지도, 추천일정, 테마여행, 명소, 스팟, 맛집, 쇼핑, 숙박, 호텔, 게스트하우스, 최저가 항공권 검색, 최저가 숙박 검색, 최저가 호텔 검색, 특가 항공권, 무료 항공 이벤트, 무료 호텔 이벤트, 여행Q&A, 여행후기, 홍콩, 마카오, 오사카, 후쿠오카, 도쿄, 타이베이, 베이징, 상하이, 칭다오, 싱가포르, 방콕, 푸껫, 보라카이, 코타 키나발루, 파리, 로마, 런던, 바르셀로나, 크로아티아, 이스탄불, 뉴욕, 하와이, 미서부, 괌, 시드니, 제주, 타이중, 가오슝",
};

const metaTags = Object.entries(META).map(([key, value]) => (
	<meta name={key} content={value} key={key} />
));

class CustomDocument extends Document<IDocumentProps> {
	static async getInitialProps(ctx: DocumentContext) {
		const initialProps = await Document.getInitialProps(ctx);
		// const page = ctx.renderPage(() => () => <></>);
		return {
			...initialProps,
			// ...page,
		};
	}
	render() {
		const { styleTags } = this.props;
		return (
			<Html lang="ko">
				<Head>
					<meta charSet="utf-8" />
					<link rel="shortcut icon" href="/favicon.ico" />
					{metaTags}
					{styleTags}
				</Head>
				<body>
					<Main />
					<NextScript />
				</body>
			</Html>
		);
	}
}

export default CustomDocument;
