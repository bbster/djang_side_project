import React from 'react';
import { Global as EmotionGlobal, css, ThemeProvider } from '@emotion/react';

export const Global = () => (
    <EmotionGlobal
        styles={css`
            html,
            body {
                margin: 0;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 10px;
                background: #ffffff;
            }
            #__next {
            }
            main {
            }
        `}
    />
);

export const Reset = () => (
    <EmotionGlobal
        styles={css`
            h1,
            h2,
            h3,
            h4,
            h5,
            h6 {
                margin: 0;
            }
        `}
    />
);

interface ThemeProps {
    theme: 'default' | 'dark';
}
const defaultThemeProps: ThemeProps = {
    theme: 'default',
};
export const Theme: React.FC<ThemeProps> = (props = defaultThemeProps) => {
    const variables = {
        default: {},
        dark: {},
    }[props.theme];
    return <ThemeProvider theme={variables}>{props.children}</ThemeProvider>;
};
