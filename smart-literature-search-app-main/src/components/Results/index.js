import { useEffect } from 'react';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useRouter } from 'next/router';
import { getScrapingResultsAction } from '../../redux/actions/scraping.actions';
import { sortAction, sortWithModelAction } from '../../redux/actions/sorting.actions';
import Actions from './Actions';
import CustomTable from '../CustomTable';
import { getSearchesAction } from '../../redux/actions/crawling.actions';
import { logAction } from '../../redux/actions/logging.actions'; // Import logging actions
const Results = () => {
    const router = useRouter();
    const { searchId } = router.query; // Retrieve searchId from query parameters
    const dispatch = useDispatch();
    const [scrapingResults, setScrapingResults] = useState([]);
    const [loading, setLoading] = useState(true);
    const [keyword, setKeyword] = useState('');
    const [exactWords, setExactWords] = useState([]);
    const [keywords, setKeywords] = useState([]);
    const [sortMethod, setSortMethod] = useState('relevance');
    const [rawResults, setRawResults] = useState([]);
    useEffect(() => {
        if (searchId) {
            dispatch(getSearchesAction(searchId)).then((res) => {
                if (!res) {
                    console.error("No results found");
                } else {
                    const data = res[0];
                    setKeyword(data.keyword);
                    setExactWords(data.exactTerms);
                    const newKeywords = [data.keyword, ...(data.exactTerms || [])];
                    setKeywords(newKeywords);

                    dispatch(getScrapingResultsAction(searchId)).then((res) => {
                        const cleaned = res.results.map(({ action, ...rest }) => rest);
                        setRawResults(cleaned);
                        setSortMethod('relevance');
                        dispatch(sortAction({ results: cleaned, keywords: newKeywords })).then((sortRes) => {
                            const results = sortRes.results.map((item, i) => ({
                                ...item,
                                searchId,
                                rank: i + 1,
                                id: item.id || `result_${i + 1}`,
                                action: <Actions item={{ ...item, searchId, rank: i + 1, id: item.id || `result_${i + 1}` }} />,
                            }));
                            setScrapingResults(results);
                            setLoading(false);
                        });
                        setLoading(false); // only initial loading
                    });
                }
            });
        }
    }, [searchId]);

    useEffect(() => {
        if (!rawResults.length || !keywords.length) return;
        setLoading(true);

        const sortFn = getSortFunction(sortMethod);
        dispatch(sortFn({ results: rawResults, keywords })).then((sortRes) => {
            let { results } = sortRes;
            const enhanced = results.map((item, i) => {
                const fullItem = {
                    ...item,
                    searchId: searchId,
                    rank: i + 1,
                    id: item.id || `result_${i + 1}`,
                };
                return {
                    ...fullItem,
                    action: <Actions item={fullItem} />,
                };
            });
            setScrapingResults(enhanced);
            setLoading(false);
        });
    }, [sortMethod]);

    const getSortFunction = (method) => {
        switch (method) {
            case 'model':
                return sortWithModelAction;
            case 'relevance':
                return sortAction;
            default:
                return sortAction;
        }
    };

    const sortAndSetResults = (results, keywords) => {
        const cleanedResults = results.map(({ action, ...rest }) => rest);
        const sortFn = getSortFunction(sortMethod);

        dispatch(sortFn({ results: cleanedResults, keywords })).then((sortRes) => {
            let { results } = sortRes;
            results = results.map((item, i) => {
                const fullItem = {
                    ...item,
                    searchId: searchId,
                    rank: i + 1,
                    id: item.id || `result_${i + 1}`,
                };
                return {
                    ...fullItem,
                    action: <Actions item={fullItem} />,
                };
            });
            setScrapingResults(results);
            setLoading(false);
        });
    };
    const columns = [
        {
            name: 'Actions',
            selector: (row) => row['action'],
            width: '10%',
        },
        {
            name: 'URL',
            selector: (row) => (
                <a
                    href={row.url}
                    className='text-blue-500 underline'
                    target='_blank'
                    rel='noopener noreferrer'
                    onClick={(e) => {
                        // Log before navigating
                        const logItem = {
                            action: 'click_url',
                            itemId: row.id,
                            title: row.title,
                            url: row.url,
                            searchId: row.searchId,
                            timestamp: Date.now().toString(),
                            rank: row.rank.toString(),
                        }
                        dispatch(logAction(logItem))
                            .then((res) => {
                                console.log('Logging successful:', res);
                            });
                    }}
                >
                    {row.url}
                </a>
            ),
            width: '10%',
        },
        {
            name: 'Title',
            selector: (row) => row['title'],
            width: '30%',
            wrap: true,
        },
        {
            name: 'Abstract',
            selector: (row) => row['data'],
            width: '50%',
            wrap: true,
        },
    ];

    return (
        <div className='grid mb-4 pb-10 px-8 mx-4'>
            <div className='grid grid-cols-12 gap-6'>
                <div className='grid grid-cols-12 col-span-12 gap-6 xxl:col-span-9'>
                    <div className='col-span-12 mt-8'>
                        <div className='flex items-center h-10 intro-y'>
                            <h2 className='mr-5 text-lg font-medium truncate'>Results</h2>
                        </div>
                        <div className='col-span-12 mt-5'>
                            <div className='grid gap-2 grid-cols-1'>
                                <div className="mb-4">
                                    <label className="mr-2 font-semibold">Sort By:</label>
                                    <select
                                        className="border border-gray-300 rounded p-2"
                                        value={sortMethod}
                                        onChange={(e) => setSortMethod(e.target.value)}
                                    >
                                        <option value="relevance">Relevance</option>
                                        <option value="model">Relavance With Trained Model</option>
                                    </select>
                                </div>
                                <div className='bg-white shadow-lg p-4 shadow-xl rounded-lg col-span-12 sm:col-span-6 xl:col-span-3 intro-y bg-white'>
                                    {scrapingResults ? (
                                        <CustomTable
                                            data={scrapingResults}
                                            columns={columns}
                                            loading={loading}
                                            searchId={searchId}
                                        />
                                    ) : null}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Results;

