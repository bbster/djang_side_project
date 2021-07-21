module.exports = {
	roots: ["<rootDir>/src"],
	preset: "ts-jest",
	globals: {
		"ts-jest": {
			tsConfig: "jest.tsconfig.json",
		},
	},
	collectCoverageFrom: [
		"src/**/*.{js,jsx,ts,tsx}",
		"!src/**/*.d.ts",
		"!**/node_modules/**",
	],
	testPathIgnorePatterns: ["<rootDir>/node_modules/", "<rootDir>/.next/"],
	coverageReporters: ["json", "lcov", "text", "text-summary"],
	setupFilesAfterEnv: ["<rootDir>/setupTests.ts"],
	testMatch: [
		"<rootDir>/src/**/__tests__/**/*.{spec,test}.{js,jsx,ts,tsx}",
		"<rootDir>/src/**/*.{spec,test}.{js,jsx,ts,tsx}",
	],
	transform: {
		"^.+\\.(js|jsx|ts|tsx)$": "ts-jest",
		"^.+\\.css$": "<rootDir>/config/jest/cssTransform.js",
	},
	transformIgnorePatterns: [
		"[/\\\\]node_modules[/\\\\].+\\.(js|jsx|ts|tsx)$",
		"^.+\\.module\\.(css|sass|scss)$",
	],
	moduleNameMapper: {
		"^.+\\.module\\.(css|sass|scss)$": "identity-obj-proxy",
	},
	modulePaths: [],
	moduleFileExtensions: [
		"web.js",
		"js",
		"web.ts",
		"ts",
		"web.tsx",
		"tsx",
		"json",
		"web.jsx",
		"jsx",
		"node",
	],

	watchPlugins: [],
	snapshotSerializers: ["enzyme-to-json/serializer"],
};
