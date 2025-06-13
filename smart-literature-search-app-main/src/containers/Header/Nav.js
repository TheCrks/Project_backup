import Link from 'next/link'
import React from 'react'

const Nav = () => {
  return (
    <>
      <Link href='/'>
        <a className='hover:text-red-600 text-white block px-3 py-2 rounded-md text-base font-medium'>
          Home
        </a>
      </Link>

      <Link href='/za'>
        <a className='hover:text-red-600 text-white block px-3 py-2 rounded-md text-base font-medium'>
          About
        </a>
      </Link>
    </>
  )
}

export default Nav
