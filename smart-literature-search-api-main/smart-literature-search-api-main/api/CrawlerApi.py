# 3rd party
from typing import List, Optional
from fastapi import APIRouter

# internal imports
from schemas import CrawlerSchema
from services.CrawlerService import CrawlerService

api_crawler_router = APIRouter()

@api_crawler_router.post("/crawler/search", response_model=CrawlerSchema.CrawlerSearchResponse, tags=["Crawler Api"])
async def start_searching_by_keyword(body: CrawlerSchema.CrawlerSearch):
    crawlerSearchResponse = CrawlerService.createSearch(body.keyword, body.username, body.sites, body.date, body.queryName, body.exactTerms, body.excludeTerms, body.dateRestrict)
    CrawlerService.startSearching(crawlerSearchResponse.searchId, body.keyword, body.sites, body.exactTerms, body.excludeTerms, body.dateRestrict)
    #background_tasks.add_task(CrawlerService.startSearching, searchId=crawlerSearchResponse.searchId, keyword=body.keyword, sites=body.sites)
    return crawlerSearchResponse

@api_crawler_router.get("/crawler/search", response_model=List[CrawlerSchema.CrawlerSearch], tags=["Crawler Api"])
async def get_search_details(searchId: Optional[str] = None):
    searchResponseList = CrawlerService.getSearchs(searchId)
    return searchResponseList

@api_crawler_router.get("/crawler/searchResults", response_model=List[CrawlerSchema.CrawlerSearchResultsResponse], tags=["Crawler Api"])
async def get_search_results(searchId: Optional[str] = None):
    searchResultsItems = CrawlerService.getSearchResults(searchId)
    return searchResultsItems

@api_crawler_router.get("/crawler/counts", response_model=CrawlerSchema.Counts, tags=["Crawler Api"])
async def get_search_counts():
    crawlerCounts = CrawlerService.getSearchCounts()
    return crawlerCounts

@api_crawler_router.get("/crawler/search-ids", response_model=CrawlerSchema.SearchIdList, tags=["Crawler Api"])
async def get_all_search_ids():
    return CrawlerService.getAllSearchIds()
