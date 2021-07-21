import axios from "axios";

function processResponse(result) {
	return result
		.then((response) => ({ response }))
		.catch((error) => ({ error }));
}

const api = (baseURL) => ({
	get(endpoint) {
		const response = axios.get(endpoint, { baseURL });
		return processResponse(response);
	},
	post(endpoint, params) {
		const response = axios.post(endpoint, params, {
			baseURL,
		});

		return processResponse(response);
	},
	put(endpoint, params) {
		const response = axios.put(endpoint, params, {
			baseURL,
		});

		return processResponse(response);
	},
	delete(endpoint, params) {
		const response = axios.delete(endpoint, {
			baseURL,
			params,
		});

		return processResponse(response);
	},
});

export default api;
