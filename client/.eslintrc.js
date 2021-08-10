module.exports = {
    env: {
        browser: true,
        es2020: true,
        node: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:prettier/recommended',
        'plugin:@typescript-eslint/eslint-recommended',
        'plugin:@typescript-eslint/recommended',
        'prettier/@typescript-eslint',
    ],
    parser: '@typescript-eslint/parser',
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 2020,
        sourceType: 'module',
    },
    rules: {
        'prettier/prettier': ['error', { singleQuote: true, endOfLine: 'auto' }],
        'linebreak-style': 0,
        'no-console': 'error',
        '@typescript-eslint/explicit-function-return-type': ['off'],
        '@typescript-eslint/explicit-module-boundary-types': ['off'],
        '@typescript-eslint/no-unused-vars': ['error'],
        'no-unused-expressions': 'off',
        'no-useless-concat': 'off',
        'no-useless-constructor': 'off',
        'default-case': 'off',
        '@typescript-eslint/no-use-before-define': 'off',
        '@typescript-eslint/no-explicit-any': 'off',
        '@typescript-eslint/no-empty-interface': 'off',
        '@typescript-eslint/ban-ts-ignore': 'off',
        '@typescript-eslint/no-empty-function': 'off',
        '@typescript-eslint/no-var-requires': ['off'],
        'react/react-in-jsx-scope': 1,
        '@typescript-eslint/ban-types': ['off'],
    },
    settings: {
        react: {
            version: 'detect',
        },
    },
};
