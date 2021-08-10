import React from 'react';
import Document, { Html, Main, Head, NextScript, DocumentContext } from 'next/document';
import { ServerStyleSheets } from '@material-ui/styles';

class CustomDocument extends Document<any> {
    static async getInitialProps(ctx: DocumentContext) {
        const sheets = new ServerStyleSheets();
        const originalRenderPage = ctx.renderPage;
        ctx.renderPage = () =>
            originalRenderPage({ enhanceApp: App => props => sheets.collect(<App {...props} />) });

        const initialProps = await Document.getInitialProps(ctx);
        return {
            ...initialProps,
            styles: <React.Fragment>{sheets.getStyleElement()}</React.Fragment>,
        };
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
