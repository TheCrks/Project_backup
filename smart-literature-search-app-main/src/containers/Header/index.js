import Nav from './Nav';
import User from './User';
import Brand from './Brand';
import React, { useState } from 'react';
import { Transition } from '@headlessui/react';
import { MenuIcon, XIcon, UserCircleIcon } from '@heroicons/react/outline';

function Header() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <>
      <nav className='bg-gray-800 shadow-2xl'>
        <div className='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8'>
          <div className='flex items-center justify-between h-16'>
            <div className='flex items-center'>
              <div className='flex'>
                <Brand />
              </div>
              <div className='hidden md:block'>
                <div className='ml-10 flex items-baseline space-x-4'>
                  <Nav />
                </div>
              </div>
            </div>
            <div className='hidden md:block'>
              <User />
            </div>
            <div className='-mr-2 flex md:hidden'>
              <button
                onClick={() => setIsOpen(!isOpen)}
                type='button'
                className='bg-gray-900 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white'
                aria-controls='mobile-menu'
                aria-expanded='false'
              >
                <span className='sr-only'>Open main menu</span>
                {!isOpen ? (
                  <MenuIcon className='w-6 h-6' />
                ) : (
                  <XIcon className='w-6 h-6' />
                )}
              </button>
            </div>
          </div>
        </div>

        <Transition
          show={isOpen}
          enter='transition ease-out duration-100 transform'
          enterFrom='opacity-0 scale-95'
          enterTo='opacity-100 scale-100'
          leave='transition ease-in duration-75 transform'
          leaveFrom='opacity-100 scale-100'
          leaveTo='opacity-0 scale-95'
        >
          <div className='md:hidden' id='mobile-menu'>
            <div className='px-2 pt-2 pb-3 space-y-1 sm:px-3'>
              <Nav />
              <User/>
            </div>
          </div>
        </Transition>
      </nav>
    </>
  );
}

export default Header;
