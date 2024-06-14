
const axios = require('axios');

async function request() {

	const endpoint = '/';
	const url = `http://${endpoint}`;

	const payload = {
		
	};

	const config = {
		headers: {
			'Content-Type': 'application/json'
		}
	};

	try {
		const response = await axios.post(url, payload, config);
		console.log(response);

	} catch (error) {
		console.error(error);
	}
}

request();