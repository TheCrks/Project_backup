import ReactTagInput from '@pathofdev/react-tag-input';
import '@pathofdev/react-tag-input/build/index.css';

const MultipleTag = ({ filters, setFilters, field, title }) => {
  const handleChange = (newTags) => {
    setFilters({ ...filters, [field]: newTags });
  };

  return (
    <ReactTagInput
      placeholder={`Select ${title}`}
      tags={filters[field]}
      onChange={handleChange}
    />
  );
};

export default MultipleTag;
