# internal imports
from schemas import CrawlerSchema
from serviceReferences.FirebaseServiceReference import FirebaseServiceReference
from serviceReferences.GoogleApiServiceReference import GoogleApiServiceReference
from utils import TimeUtils

def createSearch(keyword, username, sites, date, queryName, exactTerms, excludeTerms, dateRestrict):    
    # insert search details
    searchId = FirebaseServiceReference.insertSearch(keyword, username, sites, date, queryName, exactTerms, excludeTerms, dateRestrict)

    # start search, return search id
    crawlerSearchResponse = CrawlerSchema.CrawlerSearchResponse(searchId=searchId)

    return crawlerSearchResponse

def startSearching(searchId, keyword, sites, exactTerms, excludeTerms, dateRestrict):
    # search by google
    searchResults = GoogleApiServiceReference.searchByQuery(keyword, sites, exactTerms, excludeTerms, dateRestrict)

    # insert search results
    FirebaseServiceReference.insertSearchResults(searchId, searchResults)


def getSearchs(searchId):
    searchResponseList = []

    try:
        docs = FirebaseServiceReference.readSearches(searchId)
        print(f"Search ID being queried: {searchId}")

        if not docs:
            print("No documents returned from Firebase")
            return searchResponseList

        for doc in docs:
            try:
                docObject = doc.to_dict()

                searchResponse = CrawlerSchema.CrawlerSearch(
                    id=docObject["id"],
                    username=docObject["username"],
                    keyword=docObject["keyword"],
                    sites=docObject["sites"],
                    date=docObject["date"],
                    queryName=docObject["queryName"],
                    dateRestrict=docObject["dateRestrict"],
                    exactTerms=docObject["exactTerms"],
                    excludeTerms=docObject["excludeTerms"],
                    status=docObject["status"])

                searchResponseList.append(searchResponse)
            except Exception as e:
                print(f"Error processing document: {e}")
                continue

        return searchResponseList
    except Exception as e:
        print(f"Error in getSearchs: {e}")
        return searchResponseList


def getSearchResults(searchId):
    # get search results from db
    searchResultsItems = []

    docs = FirebaseServiceReference.readSearchResults(searchId)
    for doc in docs:
        docObject = doc.to_dict()
        searchResultResponse = CrawlerSchema.CrawlerSearchResultsResponse(
            searchId=docObject["searchId"],
            results=docObject["results"])

        searchResultsItems.append(searchResultResponse)

    return searchResultsItems


def getSearchCounts():
    count_today = 0
    count_total = 0
    count_finished = 0
    today_date = TimeUtils.getToday()
    docs = FirebaseServiceReference.readSearches(None)
    for doc in docs:
        docObject = doc.to_dict()
        if(docObject["date"] == today_date):
            count_today = count_today + 1

        if(docObject["status"] == "Finished"):
            count_finished = count_finished + 1

        count_total = count_total + 1
    crawlerCounts = CrawlerSchema.Counts(totalSearches=count_total,
                                         dailySearches=count_today,
                                         finishedSearches=count_finished)
    return crawlerCounts


def getAllSearchIds():
    searchIds = []
    try:
        docs = FirebaseServiceReference.readSearches(None)

        for doc in docs:
            docObject = doc.to_dict()
            if 'id' in docObject:
                searchIds.append(docObject['id'])

        return CrawlerSchema.SearchIdList(searchIds=searchIds)
    except Exception as e:
        print(f"Error getting search IDs: {e}")
        return CrawlerSchema.SearchIdList(searchIds=[])
