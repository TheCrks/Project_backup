import LocalStorage from './localStorage.utils'
// HOC/withAuth.jsx
import { useRouter } from 'next/router';
const withAuth = (WrappedComponent) => {
  return (props) => {
    if (typeof window !== 'undefined') {
      const router = useRouter();

      const user = LocalStorage.getItemWithExpiry('user');

      if (!user) {
        router.replace('/login');
        return null;
      }

      return <WrappedComponent {...props} />;
    }

    return <></>;
  };
};

export default withAuth;
