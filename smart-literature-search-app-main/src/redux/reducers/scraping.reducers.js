import { RETRIEVE_SCRAPING_RESULTS, START_SCRAPING } from '../types';

const initialStateScrapingResult = {};

const scraping = (scrapingResult = initialStateScrapingResult, action) => {
  const { type, payload } = action;
  switch (type) {
    case RETRIEVE_SCRAPING_RESULTS:
      return payload;
    case START_SCRAPING:
      return scrapingResult;
    default:
      return scrapingResult;
  }
};

export default scraping;
