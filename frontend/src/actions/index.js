import backend from '../apis/backend';

export const fetchVendors = () => async dispatch => {
	const response = await backend.get('/vendors');

	dispatch({ type: 'FETCH_VENDORS', payload: response.data })
}