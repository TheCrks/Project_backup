# 3rd party imports
import requests

# internal imports
from schemas import ScraperSchema
from serviceReferences.FirebaseServiceReference import FirebaseServiceReference
from .Scraper import scrapSites

def startScraping(scrapingId, searchId):
    # updates scraping status to in progress when job is started.
    FirebaseServiceReference.updateSearchStatus(searchId, 'In Progress')

    # get search results from db
    searchResults = FirebaseServiceReference.readSearchResults(searchId)
    for doc in searchResults:
        docObject = doc.to_dict()
        searchResultsObject = docObject["results"]
    

    # scrap by beautifulsoup
    scrapingResults = scrapSites(searchResultsObject)


    # insert search results
    FirebaseServiceReference.insertScrapingResults(scrapingId, scrapingResults)
    

    # updates scraping status to finished when all job done.
    FirebaseServiceReference.updateSearchStatus(searchId, 'Finished')

def initScrapingOperation(searchId, username):    
    # insert scraping details to db
    scrapingId = FirebaseServiceReference.insertScraping(searchId, username)

    scraperScrapingResponse = ScraperSchema.ScraperScrapeResponse(scrapingId=scrapingId)

    return scraperScrapingResponse

def getScrapings(scrapingId):
    # get scraping details from db
    scrapingResponseList = []

    docs = FirebaseServiceReference.readScrapings(scrapingId)
    for doc in docs:
        docObject = doc.to_dict()
        searchResponse = ScraperSchema.ScraperScrape(
        id=docObject["id"], 
        username=docObject["username"], 
        searchId=docObject["searchId"])

        scrapingResponseList.append(searchResponse)
    
    return scrapingResponseList

def getScrapingResults(scrapingId):
    # get search results from db
    scrapingResultsItems = []

    docs = FirebaseServiceReference.readScrapingResults(scrapingId)
    for doc in docs:
        docObject = doc.to_dict()
        scrapingResultResponse = ScraperSchema.ScraperScrapeResultsResponse(
        scrapingId=docObject["scrapingId"], 
        results=docObject["results"])

        scrapingResultsItems.append(scrapingResultResponse)

    return scrapingResultsItems

def getScrapingResultsBySearchId(searchId):
    # get search results from db
    scrapingResultsItems = []

    docs = FirebaseServiceReference.readScrapings(None)
    for doc in docs:
        docObject = doc.to_dict()
        if(docObject["searchId"] == searchId):
            scrapingId = docObject["id"]
            docs = FirebaseServiceReference.readScrapingResults(scrapingId)
            for doc in docs:
                docObject = doc.to_dict()
                scrapingResultResponse = ScraperSchema.ScraperScrapeResultsResponse(
                scrapingId=docObject["scrapingId"],
                results=docObject["results"])

                scrapingResultsItems.append(scrapingResultResponse)

    return scrapingResultsItems

def getScrapingCounts():
    count_finished = 0

    docs = FirebaseServiceReference.readScrapings(None)

    for doc in docs:
        docObject = doc.to_dict()
        if(docObject["status"] == "Finished"):
            count_finished = count_finished + 1

    return {"finishedSearches":count_finished}

def getScrapingStatus(searchId):
    docs = FirebaseServiceReference.readScrapingStatus(searchId)

    for doc in docs:
        docObject = doc.to_dict()
        return docObject["status"]