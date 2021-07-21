module.exports = {
	i18n: {
		locales: ["ko-KR", "en-US"],
		defaultLocale: "ko-KR",
		domains: [
			{
				domain: "side.com",
				defaultLocale: "ko-KR",
			},
			{
				domain: "side.com/en-US",
				defaultLocale: "en-US",
			},
		],
	},
	future: {
		webpack5: false,
	},
	webpack(config) {
		config.resolve.modules.push(__dirname);

		return config;
	},
	exportPathMap: async function (
		defaultPathMap,
		{ dev, dir, outDir, distDir, buildId },
	) {
		return {};
	},
};
