import { combineReducers } from 'redux';
import vendorsReducer from './vendorsReducer';

export default combineReducers({
	vendors: vendorsReducer
})