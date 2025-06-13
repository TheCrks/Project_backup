import { ChartBarIcon, ChartPieIcon, DocumentSearchIcon, PresentationChartLineIcon } from '@heroicons/react/outline';
import React from 'react';
import KPICard from './KPICard';

const KPITile = ({counts}) => {
  const {totalSearches, finishedSearches, dailySearches} = counts;
  return (
    <>
      <KPICard title='Total Searches' value={totalSearches}>
        <DocumentSearchIcon className='h-7 w-7 text-blue-400' />
        <div className='bg-green-500 rounded-full h-6 px-2 flex justify-items-center text-white font-semibold text-sm'>
          <span className='flex items-center'>8 per day</span>
        </div>
      </KPICard>
      <KPICard title='Daily Searches' value={dailySearches}>
        <ChartBarIcon className='h-7 w-7 text-yellow-400' />
        <div className='bg-red-500 rounded-full h-6 px-2 flex justify-items-center text-white font-semibold text-sm'>
          <span className='flex items-center'>Limit: {10-dailySearches}</span>
        </div>
      </KPICard>
      <KPICard title='Finished Searches' value={finishedSearches}>
        <ChartPieIcon className='h-7 w-7 text-pink-400' />
        <div className='bg-yellow-500 rounded-full h-6 px-2 flex justify-items-center text-white font-semibold text-sm'>
          <span className='flex items-center'>%{Math.round((finishedSearches/totalSearches)*100)}</span>
        </div>
      </KPICard>
      <KPICard title='Failed Searches' value='0'>
        <PresentationChartLineIcon className='h-7 w-7 text-green-400' />
        <div className='bg-blue-500 rounded-full h-6 px-2 flex justify-items-center text-white font-semibold text-sm'>
          <span className='flex items-center'>0%</span>
        </div>
      </KPICard>
    </>
  );
};

export default KPITile;
