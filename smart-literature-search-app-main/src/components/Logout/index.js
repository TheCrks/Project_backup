import { googleLogout } from '@react-oauth/google';
import { LogoutIcon } from '@heroicons/react/outline';
import LocalStorage from '../../utils/localStorage.utils';
import { useRouter } from 'next/router';

const Logout = () => {
    const router = useRouter();

    const onLogoutSuccess = () => {
        console.log('[Logout Successful]');
        LocalStorage.deleteItem('user');
        router.push('/');
    };

    const onFailure = (res) => {
        console.log('[Logout Failed] res:', res);
    };

    const handleLogout = () => {
        googleLogout();
        onLogoutSuccess();
    };

    return (
        <button onClick={handleLogout} className='text-white'>
            <LogoutIcon className='h-8 w-8' />
        </button>
    );
};

export default Logout;