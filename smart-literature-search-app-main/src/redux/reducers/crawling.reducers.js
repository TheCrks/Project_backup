import {
  RETRIEVE_SEARCH_COUNTS,
  CREATE_NEW_SEARCH,
  RETRIEVE_SEARCHES,
} from '../types';

const initialStateCrawling = { counts: {}, searches: [] };

const crawling = (crawlingResults = initialStateCrawling, action) => {
  const { type, payload } = action;
  switch (type) {
    case RETRIEVE_SEARCH_COUNTS:
      return { ...crawlingResults, counts: payload };
    case RETRIEVE_SEARCHES:
      return { ...crawlingResults, searches: payload };
    case CREATE_NEW_SEARCH:
      return {
        ...crawlingResults,
        searches: [...crawlingResults.searches, payload],
      };
    default:
      return crawlingResults;
  }
};

export default crawling;


