import { SaveIcon } from '@heroicons/react/outline';

const convertArrayOfObjectsToCSV = (array) => {
  let result;

  const columnDelimiter = ',';
  const lineDelimiter = '\n';
  const keys = Object.keys(array[0]);

  result = '';
  result += keys.join(columnDelimiter);
  result += lineDelimiter;

  array.forEach((item) => {
    let ctr = 0;
    keys.forEach((key) => {
      if (ctr > 0) result += columnDelimiter;

      result += item[key];

      ctr++;
    });
    result += lineDelimiter;
  });

  return result;
};

const downloadCSV = (columns, data) => {
  const link = document.createElement('a');
  let csv = convertArrayOfObjectsToCSV(data);
  if (csv == null) return;

  const filename = 'export.csv';

  columns = { columns };
  if (!csv.match(/^data:text\/csv/i)) {
    csv = `data:text/csv;charset=utf-8,${csv}`;
  }

  link.setAttribute('href', encodeURI(csv));
  link.setAttribute('download', filename);
  link.click();
};

const Export = ({ columns, data }) => (
  <SaveIcon
    className='w-8 h-8 text-green-600 cursor-pointer border border-green-600 rounded-full p-1 hover:text-white hover:bg-green-600'
    aria-placeholder='Download'
    onClick={(e) => downloadCSV(columns, data)}
  />
);

export default Export;
