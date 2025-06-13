import React from 'react';
import Footer from '../Footer';
import Header from '../Header';

function Layout({ children }) {
  return (
    <>
      <Header />
      <div className='h-screen max-w-7xl mx-auto'>
        {children}
        <Footer />
      </div>
    </>
  );
}

export default Layout;
