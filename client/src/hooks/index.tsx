import React, { useCallback, useState } from "react";

export const test = (initialState = false) => {
	const [state, setState] = useState(initialState);

	const toggle = useCallback(() => setState((state) => !state), []);

	return [state, toggle];
};
