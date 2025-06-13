import { SET_LOADING_STATUS } from '../types';

const initialUiState = { loading: false };

const ui = (uiStates = initialUiState, action) => {
  const { type, payload } = action;
  switch (type) {
    case SET_LOADING_STATUS:
      return { ...uiStates, loading: payload };
    default:
      return uiStates;
  }
};

export default ui;
