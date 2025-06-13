import { toast } from 'react-toastify';
import DateUtils from '../../utils/date.utils';
import CrawlingService from '../../services/crawling.service';
import {
  RETRIEVE_SEARCH_COUNTS,
  RETRIEVE_SEARCHES,
  CREATE_NEW_SEARCH,
  SET_LOADING_STATUS,
} from '../types';

export const getCrawlingCountsAction = () => async (dispatch) => {
  return await CrawlingService.getCrawlingCounts()
    .then((res) => {
      const { data } = res;

      dispatch({
        type: RETRIEVE_SEARCH_COUNTS,
        payload: data,
      });

      return Promise.resolve();
    })
    .catch((error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      toast.error('Error occured while fetching search counts.');

      return Promise.reject();
    });
};

export const getSearchesAction = (searchId) => async (dispatch) => {
  return await CrawlingService.getSearchs(searchId)
    .then((res) => {
      const { data } = res;
      console.log('Action data', data);
      dispatch({ type: RETRIEVE_SEARCHES, payload: data });

      return Promise.resolve(data);
    })
    .catch((error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

        toast.error('Error occured while fetching searches.');
        console.error('Error:', message);

      return Promise.reject();
    });
};

export const createSearchAction = (searchInfo) => async (dispatch) => {
  dispatch({ type: SET_LOADING_STATUS, payload: true });
  return await CrawlingService.createSearch(searchInfo)
    .then((res) => {
      const { data } = res;
      const { searchId } = data;

      searchInfo = {
        ...searchInfo,
        id: searchId,
        date: DateUtils.getToday(),
        username: 'mmutlu',
        status: 'Started',
      };
       console.log('searchInfo', searchInfo);
      toast.success(`'${searchInfo.queryName}' search has been started.`);
      dispatch({ type: CREATE_NEW_SEARCH, payload: searchInfo });
      dispatch({ type: SET_LOADING_STATUS, payload: false });

      return Promise.resolve(searchId);
    })
    .catch((error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      toast.error('Error occured while creating new search.');
      dispatch({ type: SET_LOADING_STATUS, payload: false });

      return Promise.reject();
    });
};
