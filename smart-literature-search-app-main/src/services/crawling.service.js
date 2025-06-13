import axios from 'axios';
import DateUtils from '../utils/date.utils';

const getCrawlingCounts = async () => {
  const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_SEARCH_COUNTS;
  return await axios.get(endpoint, {});
};

const getSearchs = async (searchId) => {
    console.log(' Service searchId', searchId);
    const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_SEARCH;
    return await axios.get(endpoint, { params: { searchId } });
};

const createSearch = async (searchDetails) => {
  const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_SEARCH;
  
    const searchBody = {
        id: searchDetails.id || '', // Optional: Provide a default or generate an ID if required
        keyword: searchDetails.keyword || '', // Required: Main search keyword
        username: searchDetails.username || 'mmutlu', // Default username
        date: searchDetails.date || DateUtils.getToday(), // Default to today's date
        queryName: searchDetails.queryName || 'Default Query Name', // Default query name
        status: searchDetails.status || 'Started', // Default status
        sites: searchDetails.sites || [], // List of sites to search
        dateRestrict: searchDetails.dateRestrict || '', // Date restriction
        exactTerms: searchDetails.exactTerms || [], // Exact terms to include
        excludeTerms: searchDetails.excludeTerms || [], // Terms to exclude
    };
  return await axios.post(endpoint, searchBody, {});
};

export default {
  getCrawlingCounts,
  getSearchs,
  createSearch,
};
