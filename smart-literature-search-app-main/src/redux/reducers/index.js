import { combineReducers } from 'redux';

import scraping from './scraping.reducers';
import crawling from './crawling.reducers';
import ui from './ui.reducers';

export default combineReducers({ scraping, crawling, ui });
