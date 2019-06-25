import React from 'react';
import { connect } from 'react-redux';
import { fetchVendors } from '../actions';

class VendorList extends React.Component {
	componentDidMount(){
		this.props.fetchVendors();
	}
	render(){
		console.log(this.props.vendors)
		return <div>Vendor List</div>
	}
}

const mapStateToProps = (state) => {
	return { vendors: state.vendors }
}

export default connect(
	mapStateToProps,
	{fetchVendors: fetchVendors}
	)(VendorList);