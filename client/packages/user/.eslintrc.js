module.exports = {
    parser: '@typescript-eslint/parser',
    env: {
        browser: true,
        es2020: true,
        node: true,
    },
    extends: [
        '../../.eslintrc.js',
        'next',
        'next/core-web-vitals',
        'eslint:recommended',
        'plugin:@next/next/recommended',
    ],
    parserOptions: {
        ecmaVersion: 2018,
        sourceType: 'module',
        ecmaFeatures: {
            jsx: true,
        },
    },
    rules: {
        'react/prop-types': 0,
    },
    ignorePatterns: [
        'dist/*.js',
        'src/stories/**/*.svg',
        'src/stories/**/*.css',
        'src/stories/**/*.mdx',
    ],
};
