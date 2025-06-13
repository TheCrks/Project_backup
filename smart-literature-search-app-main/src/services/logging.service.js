import axios from 'axios';

const Log = async (data) => {
    const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_LOG;
    return await axios.post(endpoint, data, {});
};

export default {
    Log,
};
