import Export from './Export';
import SearchBar from './SearchBar';
import React, { useMemo, useState } from 'react';
import DataTable from 'react-data-table-component';
import { logAction } from '../../redux/actions/logging.actions';
import { useDispatch } from 'react-redux';

const CustomTable = ({ columns, data, loading, searchId }) => {
    const [filterText, setFilterText] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [skipPageNumber, setSkipPageNumber] = useState(null);  // null or number
    const dispatch = useDispatch();

    const filteredItems = data.filter((item) => {
        const keys = Object.keys(item);
        return keys.find((key) => {
            return (
                item[key] &&
                item[key].toString().toLowerCase().includes(filterText.toLowerCase())
            );
        });
    });

    const logCurrentPageItems = () => {
        if (filterText.trim() !== '') return;

        const startIndex = (currentPage - 1) * rowsPerPage;
        const pageItems = filteredItems.slice(startIndex, startIndex + rowsPerPage);

        pageItems.forEach((item, index) => {
            const logItem = {
                action: 'item_shown',
                itemId: item.id ?? null,
                title: item.title,
                url: item.url,
                searchId: item.searchId ?? searchId,
                timestamp: Date.now().toString(),
                rank: item.rank?.toString() ?? (startIndex + index + 1).toString(),
            };
            dispatch(logAction(logItem)).then((res) => {
                console.log('Logging successful:', res);
            });
        });
    };

    const handlePageChange = (newPage) => {
        if (skipPageNumber === newPage) {
            // Skip logging for this page change because it's from rowsPerPage reset
            setSkipPageNumber(null);  
        } else {
            logCurrentPageItems();
        }
        setCurrentPage(newPage);
    };

    const handleRowsPerPageChange = (newRowsPerPage, newPage) => {
        setRowsPerPage(newRowsPerPage);
        setCurrentPage(newPage);

        // Set skip flag only for the page number rowsPerPage change triggers
        setSkipPageNumber(newPage);
    };

    const subHeaderComponentMemo = useMemo(() => {
        return (
            <>
                <SearchBar
                    onFilter={(e) => setFilterText(e.target.value)}
                    filterText={filterText}
                />
                <Export columns={columns} data={filteredItems} />
            </>
        );
    }, [filterText]);

    return (
        <div className='shadow-md mt-6'>
            <DataTable
                columns={columns}
                data={filteredItems}
                pagination
                paginationPerPage={rowsPerPage}            
                paginationRowsPerPageOptions={[5, 10, 15]}
                onChangePage={handlePageChange}
                onChangeRowsPerPage={handleRowsPerPageChange}
                subHeader
                subHeaderAlign='right'
                subHeaderComponent={subHeaderComponentMemo}
                responsive={true}
                progressPending={loading}
            />
        </div>
    );
};

export default CustomTable;
