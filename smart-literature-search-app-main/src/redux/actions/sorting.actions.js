import { toast } from 'react-toastify';
import SotringService from '../../services/sorting.service';
import { SORT_RESULTS } from '../types';

export const sortAction = (data) => async (dispatch) => {
    return await SotringService.Sort(data)
        .then((res) => {
            const { data } = res;
            dispatch({
                type: SORT_RESULTS,
                payload: data,
            });

            return Promise.resolve(data);
        })
        .catch((error) => {
            const message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString();

            toast.error('Error occured while sorting data.');
            console.error('Error:', message);

            return Promise.reject();
        });
};

export const sortWithModelAction = (data) => async (dispatch) => {
    return await SotringService.SortWithModel(data)
        .then((res) => {
            const { data } = res;
            dispatch({
                type: SORT_RESULTS,
                payload: data,
            });
            return Promise.resolve(data);
        })
        .catch((error) => {
            const message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString();
            toast.error('Error occured while sorting data with model.');
            console.error('Error:', message);
            return Promise.reject();
        });
}