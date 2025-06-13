import React from 'react';
import { useState } from 'react';
import ArticleDetailModal from './ArticleDetailModal';
import { SearchCircleIcon } from '@heroicons/react/outline';
import { logAction } from '../../redux/actions/logging.actions';
import { useDispatch } from 'react-redux';

const Actions = ({ item }) => {
    const [showModal, setShowModal] = useState(false);
    const dispatch = useDispatch();
    const browseButtonHandler = () => {
        setShowModal(true);
        const logItem = {
            action: 'click_action',
            itemId: item.id,
            title: item.title,
            url: item.url,
            searchId: item.searchId,
            timestamp: Date.now().toString(),
            rank: item.rank.toString(),
        }
        dispatch(logAction(logItem))
            .then((res) => {
                console.log('Logging successful:', res);
            });
  };

  return (
    <>
      <ArticleDetailModal
        showModal={showModal}
        setShowModal={setShowModal}
        item={item}
      />
      <div
        id={`action_${item.id}`}
        className='flex items-center m-2 justify-content-between'
      >
        <SearchCircleIcon
          className='w-8 h-8 text-yellow-400 cursor-pointer hover:text-yellow-600'
          onClick={() => browseButtonHandler()}
        />
      </div>
    </>
  );
};

export default Actions;
