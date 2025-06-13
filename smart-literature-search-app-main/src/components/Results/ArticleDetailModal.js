import React, { useState } from 'react';
import 'react-responsive-modal/styles.css';
import Modal from 'react-responsive-modal';
import { DocumentIcon, DocumentTextIcon, PencilAltIcon } from '@heroicons/react/outline';

const ArticleDetailModal = ({ showModal, setShowModal, item }) => {
  return (
    <Modal
      open={showModal}
      onClose={() => {
        setShowModal(false);
      }}
      center={true}
    >
      <div
        className='fixed z-10 inset-0 overflow-y-auto'
        aria-labelledby='modal-title'
        role='dialog'
        aria-modal='true'
      >
        <div className='flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0'>
          <div
            className='fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity'
            aria-hidden='true'
          ></div>

          <span
            className='hidden sm:inline-block sm:align-middle sm:h-screen'
            aria-hidden='true'
          >
            &#8203;
          </span>
          <div className='inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full'>
            <div className='bg-white'>
              <div className='bg-gray-50 px-4 py-3 items-center sm:px-6 sm:flex'>
                <div className='mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10'>
                  <DocumentTextIcon className='h-6 w-6 text-green-600' />
                </div>
                <div className='mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left'>
                  <h3
                    className='text-lg leading-6 font-medium text-gray-900'
                    id='modal-title'
                  >
                    {item.title}
                  </h3>
                </div>
              </div>

              <div className='justify-center pt-2 sm:flex bg-gray-50'>
                <div className='w-full max-w-xs text-justify'>
                 {item.data}
                </div>
              </div>
            </div>
            <div className='bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse'>
              <button
                type='button'
                className='mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm'
                onClick={() => setShowModal(false)}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </Modal>
  );
};

export default ArticleDetailModal;
