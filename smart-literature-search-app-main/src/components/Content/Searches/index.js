import React from 'react';
import CustomTable from '../../CustomTable';
import Actions from './Actions';

const Searches = ({ searches, loading }) => {
  const tableColumns = [
    {
      name: 'Date',
      selector: (row) => row['date'],
      width: '10%'
    },
    {
      name: 'Name',
      selector: (row) => row['queryName'],
      width: '20%'
    },
    {
      name: 'Keyword',
      selector: (row) => row['keyword'],
      width: '20%'
    },
    {
      name: 'Status',
      selector: (row) => row['status'],
      width:'10%'
    },
    {
      name: 'Sites',
      selector: (row) => row.sites.join(', '),
      width: '30%'
    },
    {
      name: 'Actions',
      selector: (row) => row['action'],
      width: '10%'
    },
  ];

  searches.map((item) => {
    item.action = <Actions item={item}/>;
  });

  return (
    <>
      <CustomTable columns={tableColumns} data={searches} loading={loading}/>
    </>
  );
};

export default Searches;
