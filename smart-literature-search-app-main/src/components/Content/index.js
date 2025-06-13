import React, { useEffect } from 'react';
import KPITile from './KPITile';
import FilterTile from './FilterTile';
import {
  getCrawlingCountsAction,
  getSearchesAction,
} from '../../redux/actions/crawling.actions';
import { useDispatch, useSelector } from 'react-redux';
import Searches from './Searches';
import { useState } from 'react';
import LoadingSpinner from '../LoadingSpinner';
import withAuth from '../../utils/auth.utils';

const Content = () => {
  const crawling = useSelector((state) => state.crawling);
  const ui = useSelector((state) => state.ui);
  const [tableLoading, setTableLoading] = useState(true);

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCrawlingCountsAction());
    dispatch(getSearchesAction()).then((res) => {
      setTableLoading(false);
    });
  }, []);
  return (
    <>
      <LoadingSpinner loading={ui.loading} />
      <div className='grid mb-4 pb-10 px-8 mx-4'>
        <div className='grid grid-cols-12 gap-6'>
          <div className='grid grid-cols-12 col-span-12 gap-6 xxl:col-span-9'>
            <div className='col-span-12 mt-8'>
              <div className='flex items-center h-10 intro-y'>
                <h2 className='mr-5 text-lg font-medium truncate'>Dashboard</h2>
              </div>
              <div className='grid grid-cols-12 gap-6 mt-5'>
                <KPITile counts={crawling.counts} />
              </div>
            </div>

            <div className='col-span-12 mt-5'>
              <div className='grid gap-2 grid-cols-1'>
                <div className='bg-white shadow-lg p-4 transform shadow-xl rounded-lg col-span-12 sm:col-span-6 xl:col-span-3 intro-y bg-white'>
                  <FilterTile />
                </div>
              </div>
            </div>

            <div className='col-span-12 mt-5'>
              <div className='grid gap-2 grid-cols-1'>
                <div className='bg-white shadow-lg p-4 shadow-xl rounded-lg col-span-12 sm:col-span-6 xl:col-span-3 intro-y bg-white'>
                  <h3 className='mt-6 text-xl'>Searches</h3>
                  <Searches
                    searches={crawling.searches}
                    loading={tableLoading}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default withAuth(Content);
