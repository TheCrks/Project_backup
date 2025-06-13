import axios from 'axios';

const startScraping = async (searchId) => {
  const endpoint = process.env.NEXT_PUBLIC_ENDPOINT_SCRAPE;
    const body = {
        id : '',
        searchId: searchId || '', // Ensure `searchId` is provided
        username: 'mmutlu', // Default username
    };

    console.log('body', body);
  return axios.post(endpoint, body, {});
};

const getScrapingResults = async (searchId) => {
    if (!searchId) {
        throw new Error('searchId is required');
    }
  const endpoint = `${process.env.NEXT_PUBLIC_ENDPOINT_SCRAPE_RESULTS}?searchId=${searchId}`;
  return axios.get(endpoint, {});
};

export default {
  startScraping,
  getScrapingResults
};
