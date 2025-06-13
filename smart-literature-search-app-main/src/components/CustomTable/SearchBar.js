import React from 'react';
import { SearchIcon } from '@heroicons/react/outline';

const SearchBar = ({ filterText, onFilter }) => {
  return (
    <div className='border flex w-1/4 mr-2 float-right'>
      <input
        type='text'
        className='text-sm flex-shrink flex-grow flex-auto leading-normal w-px border-0 h-10 px-3 relative self-center outline-none'
        placeholder='Search in results'
        value={filterText}
        onChange={onFilter}
      />
      <div className='flex -mr-px items-center pr-3'>
        <SearchIcon className='w-4 h-4 text-gray-300' />
      </div>
    </div>
  );
};

export default SearchBar;