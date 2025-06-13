import { toast } from 'react-toastify';
import { START_SCRAPING, RETRIEVE_SCRAPING_RESULTS } from '../types';
import ScrapingService from '../../services/scraping.service';

export const startScrapingAction = (searchId) => async (dispatch) => {
    toast.info('Scraping has been started ');
  return await ScrapingService.startScraping(searchId)
    .then((res) => {
      dispatch({ type: START_SCRAPING, payload: {} });

      return Promise.resolve(res);
    })
    .catch((error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

        toast.error('Error occured while scraping results');
        console.error('Error:', message);

      return Promise.reject();
    });
};

export const getScrapingResultsAction = (searchId) => async (dispatch) => {
  return await ScrapingService.getScrapingResults(searchId)
    .then((res) => {
      const { data } = res;
      dispatch({ type: RETRIEVE_SCRAPING_RESULTS, payload: data[0] });

      return Promise.resolve(data[0]);
    })
    .catch((error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      toast.error('Error occured while getting scraping results.');
        console.error('Error:', message);
      return Promise.reject();
    });
};
