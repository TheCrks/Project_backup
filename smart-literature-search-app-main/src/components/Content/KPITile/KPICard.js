import React from 'react';

const KPICard = ({ children, title, value }) => {
  return (
    <div className='transform  hover:scale-105 transition duration-300 shadow-xl rounded-lg col-span-12 sm:col-span-6 xl:col-span-3 intro-y bg-white'>
      <div className='p-5'>
        <div className='flex justify-between'>
          {children}
        </div>
        <div className='ml-2 w-full flex-1'>
          <div>
            <div className='mt-3 text-3xl font-bold leading-8'>{value}</div>
            <div className='mt-1 text-base text-gray-600'>{title}</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default KPICard;
