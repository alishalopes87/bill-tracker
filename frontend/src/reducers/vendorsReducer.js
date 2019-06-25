export default (state = [], action) => {
	switch (action.type){
		case 'FETCH_VENDORS':
			return action.payload
		default:
			return state
	}
};