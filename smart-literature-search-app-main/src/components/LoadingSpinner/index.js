import ClipLoader from 'react-spinners/ClipLoader';

const LoadingSpinner = ({ loading }) => {
  const style = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    zIndex:'999'
  };
  return (
    <div style={style}>
      <ClipLoader color='#000' loading={loading} size={50} />
    </div>
  );
};

export default LoadingSpinner;
