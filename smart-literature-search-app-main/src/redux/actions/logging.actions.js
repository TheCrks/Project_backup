import { toast } from 'react-toastify';
import loggingService from '../../services/logging.service';
import { LOG_RESULTS } from '../types';

export const logAction = (data) => async (dispatch) => {
    return await loggingService.Log(data)
        .then((res) => {
            const { data } = res;
            dispatch({
                type: LOG_RESULTS,
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

            console.error('Error occured while logging data.');
            console.error('Error:', message);

            return Promise.reject();
        });
};
