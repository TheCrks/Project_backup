const FormInput = ({filters, setFilters, field}) => {
  return (
    <input
      className='appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500'
      id={`grid-${field}`}
      type='text'
      placeholder={`Enter a ${field}`}
      value={filters[field]}
      onChange={(e) => setFilters({ ...filters, [field]: e.target.value })}
    />
  );
};

export default FormInput;
