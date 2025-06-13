import Select from 'react-select';

const DropdownFilter = ({
  options,
  filters,
  setFilters,
  field,
  isMulti,
}) => {
  const handleChange = (selectedOptions) => {
    setFilters({ ...filters, [field]: selectedOptions });
  };

  return (
    <Select
      id={`${field}Select`}
      instanceId={`${field}Select`}
      value={filters[field]}
      isMulti={isMulti}
      onChange={(e) => handleChange(e)}
      options={options}
      placeholder={`Select ${field}`}
    />
  );
};

export default DropdownFilter;
