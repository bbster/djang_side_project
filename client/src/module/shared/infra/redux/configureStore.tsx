import { createStore, applyMiddleware, combineReducers, compose } from "redux";
import thunk from "redux-thunk";
import users from "../../../users/redux/reducers";
import forum from "../../../forum/redux/reducers";

const reducers = {
	users,
	forum,
};

export default function configureStore(initialState = {}) {
	return createStore(
		combineReducers({
			...reducers,
		}),
		initialState,
		compose(
			applyMiddleware(thunk),
			(window as any).devToolsExtension
				? (window as any).devToolsExtension()
				: (f: any) => f,
		),
	);
}
