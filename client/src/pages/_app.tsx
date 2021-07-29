import React from "react";
import Head from "next/head";
import { AppProps } from "next/app";

import * as Styles from "styles";

function CustomApp({ Component, pageProps }: AppProps<{}>) {
	return (
		<>
			<Head>
				<title>게시판</title>

				<meta charSet="utf-8" />
				<meta
					name="viewport"
					content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, shrink-to-fit=no"
				/>

				<meta name="description" content="그냥 게시판" />
				<meta name="Keywords" content="그냥 게시판" />

				<meta property="og:title" content="그냥 게시판" />
				<meta property="og:description" content="그냥 게시판" />
				<meta property="og:image" content="/images/logo.png" />
				<meta property="og:type" content="website" />
				<meta
					property="og:url"
					content={process.env.NEXT_PUBLIC_HOST}
				/>

				<meta name="twitter:title" content="그냥 게시판" />
				<meta name="twitter:description" content="그냥 게시판" />
				<meta name="twitter:image" content="https://" />
				<meta name="twitter:card" content="summary" />
				<meta name="twitter:site" content="@그냥 게시판" />

				<meta name="msapplication-TileColor" content="#000000" />
				<meta
					name="msapplication-config"
					content="/static/browserconfig.xml"
				/>

				<meta name="theme-color" content="#000" />

				<link
					rel="alternate"
					type="application/rss+xml"
					href="/feed.xml"
				/>
				<link rel="manifest" href="/static/site.webmanifest" />

				<link rel="mask-icon" href="/static/favicon/" color="#000000" />
				<link rel="shortcut icon" href="/static/favicon.ico" />
				<link
					rel="apple-touch-icon"
					sizes="180x180"
					href="/static/favicon/apple-touch-icon.png"
				/>
				<link
					rel="icon"
					type="image/png"
					sizes="32x32"
					href="/static/favicon/favicon-32x32.png"
				/>
				<link
					rel="icon"
					type="image/png"
					sizes="16x16"
					href="/static/favicon/favicon-16x16.png"
				/>
				<noscript></noscript>
			</Head>
			<Styles.Reset />
			<Styles.Global />
			<Styles.Theme theme={"default"}>
				<Component {...pageProps} />
			</Styles.Theme>
		</>
	);
}

export default CustomApp;
