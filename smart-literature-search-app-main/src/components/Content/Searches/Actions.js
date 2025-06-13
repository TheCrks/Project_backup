import React from 'react';
import { ArrowsExpandIcon } from '@heroicons/react/outline'

const Actions = ({ item }) => {
  const link = `results?searchId=${item.id}`;

  return (
    <div
      id={`action_${item.id}`}
      className='flex items-center m-2 justify-content-between'
    >
      <a
        href={link}
      >
        <ArrowsExpandIcon className='w-5 h-5 text-yellow-400 cursor-pointer hover:text-yellow-600' />
      </a>
    </div>
  );
};

export default Actions;
