import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { UserCircleIcon } from '@heroicons/react/outline';
import LocalStorage from '../../utils/localStorage.utils';
import Logout from '../../components/Logout';

const User = () => {
  const [user, setUser] = useState({});
  useEffect(() => {
    const userInfo = LocalStorage.getItemWithExpiry('user');
    setUser(userInfo);
  }, []);
  return (
    <div className='flex'>
      <Link href='/user'>
        <a className='flex hover:text-red-600 text-white block px-3 py-2 rounded-md text-base font-medium'>
          <UserCircleIcon className='w-6 h-6 mr-2' />
                  <span className=''>Welcome, {user.name}</span>
        </a>
      </Link>
      <Logout />
    </div>
  );
};

export default User;
