module.exports = {
	env: {
		browser: true,
		es2020: true,
		node: true,
	},
	extends: [
		"eslint:recommended",
		"plugin:react/recommended",
		"plugin:prettier/recommended",
		"plugin:@typescript-eslint/eslint-recommended",
		"plugin:@typescript-eslint/recommended",
	],
	parser: "@typescript-eslint/parser",
	parserOptions: {
		ecmaFeatures: {
			jsx: true,
		},
		ecmaVersion: 11,
		sourceType: "module",
	},
	plugins: ["react", "@typescript-eslint", "prettier"],
	rules: {
		quotes: ["error", "double"],
		semi: ["error", "always"],
		"@typescript-eslint/explicit-module-boundary-types": 0,
		"@typescript-eslint/no-var-requires": 0,
		"@typescript-eslint/ban-types": 0,
		"react/prop-types": 0,
		"react/react-in-jsx-scope": 1,
		"prettier/prettier": "error",
		"linebreak-style": ["error", "windows"],
	},
	ignorePatterns: [
		"dist/*.js",
		"src/stories/**/*.svg",
		"src/stories/**/*.css",
		"src/stories/**/*.mdx",
	],
	settings: {
		react: {
			version: "detect",
		},
	},
};
