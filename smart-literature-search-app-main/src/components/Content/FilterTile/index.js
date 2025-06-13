import React from 'react';
import { useState } from 'react';
import MultipleTag from './MultipleTag';
import { useDispatch } from 'react-redux';
import DropdownFilter from './DropdownFilter';
import { createSearchAction } from '../../../redux/actions/crawling.actions';
import { startScrapingAction } from '../../../redux/actions/scraping.actions';
import FormInput from './FormInput';

const FilterTile = () => {
  const [filters, setFilters] = useState({
    sites: [{ value: 'researchgate.net', label: 'researchgate.net' }],
    dateRestrict: { value: 'y1', label: 'Past year' },
    queryName: '',
    keyword: '',
    excludeTerms: [],
    exactTerms: [],
  });

  const dispatch = useDispatch();
  const createNewSearch = () => {
    const requestSites = filters.sites.map((site) => {
      return site.value;
    });
    const requestDate = filters.dateRestrict.value;

    const searchFilters = {
      ...filters,
      sites: requestSites,
      dateRestrict: requestDate,
    };

    dispatch(createSearchAction(searchFilters))
      .then((searchId) => {
        dispatch(startScrapingAction(searchId));
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const sites = [
    { value: 'researchgate.net', label: 'researchgate.net' },
    { value: 'IEEE.iexplore.org', label: 'IEEE.iexplore.org' },
    { value: 'dl.ACM.org', label: 'dl.ACM.org' },
    { value: 'link.Springer.com', label: 'link.Springer.com' },
  ];

  const date = [
    { value: 'd1', label: 'Past 24 hours' },
    { value: 'w1', label: 'Past week' },
    { value: 'm1', label: 'Past month' },
    { value: 'y1', label: 'Past year' },
    { value: 'y2', label: 'Past two years' },
    { value: 'y3', label: 'Past three years' },
    { value: 'y5', label: 'Past five years' },
    { value: 'y10', label: 'Past ten years' },
  ];

  return (
    <>
      <h3 className='mt-6 text-xl'>New Query</h3>
      <div className='flex justify-center p-2'>
        <div className='w-full max-w-lg self-center'>
          <div className='flex flex-wrap -mx-3 mb-6'>
            <div className='w-full md:w-1/2 px-3 mb-6 md:mb-0'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-query-name'
              >
                Query Name
              </label>
              <FormInput
                field='queryName'
                filters={filters}
                setFilters={setFilters}
              />
            </div>
            <div className='w-full md:w-1/2 px-3'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-keyword'
              >
                Keyword
              </label>
              <FormInput
                field='keyword'
                filters={filters}
                setFilters={setFilters}
              />
            </div>
          </div>
          <div className='flex flex-wrap -mx-3 mb-6'>
            <div className='w-full md:w-1/2 px-3 mb-6 md:mb-0'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-sites'
              >
                Sites
              </label>
              <DropdownFilter
                title='Sites'
                options={sites}
                filters={filters}
                setFilters={setFilters}
                field='sites'
                isMulti={true}
              />
            </div>
            <div className='w-full md:w-1/2 px-3 mb-6 md:mb-0'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-date'
              >
                Date
              </label>
              <DropdownFilter
                title='Date'
                options={date}
                filters={filters}
                setFilters={setFilters}
                field='dateRestrict'
                isMulti={false}
              />
            </div>
          </div>
          <div className='flex flex-wrap -mx-3 mb-2'>
            <div className='w-full md:w-1/2 px-3 mb-6 md:mb-0'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-exact-words'
              >
                Exact Words
              </label>
              <MultipleTag
                filters={filters}
                setFilters={setFilters}
                field='exactTerms'
                title='Exact Words'
              />
            </div>
            <div className='w-full md:w-1/2 px-3 mb-6 md:mb-0'>
              <label
                className='block  tracking-wide text-gray-700 text-xs font-bold mb-2'
                htmlFor='grid-excluded-words'
              >
                Excluded Words
              </label>
              <MultipleTag
                filters={filters}
                setFilters={setFilters}
                field='excludeTerms'
                title='Excluded Words'
              />
            </div>
          </div>
          <button
            className='w-full font-bold text-white bg-indigo-600 p-4 rounded-lg hover:bg-indigo-900 mt-4'
            onClick={(e) => {
              e.preventDefault();
              createNewSearch();
            }}
          >
            Create a query
          </button>
        </div>
      </div>
      <div className='w-full'></div>
    </>
  );
};

export default FilterTile;
