import axios from 'axios';

const Sort = async (data) => {
    const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_SORT;

    return await axios.post(endpoint, data, {});
};
const SortWithModel = async (data) => {
    const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_MODEL;

    return await axios.post(endpoint, data, {});
};
export default {
    Sort,
    SortWithModel,
};