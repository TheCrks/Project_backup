from schemas import ScraperSchema
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks

from services.ScraperService import ScraperService
from services.CrawlerService import CrawlerService

api_scraper_router = APIRouter()

@api_scraper_router.post("/scraper/scrape", response_model=ScraperSchema.ScraperScrapeResponse, tags=["Scraper Api"])
async def start_scraping_by_id(body: ScraperSchema.ScraperScrape, background_tasks: BackgroundTasks):
    # starts scraping, returns scraping id
    scraperScrapeResponse = ScraperService.initScrapingOperation(body.searchId,body.username)
    background_tasks.add_task(ScraperService.startScraping, scrapingId=scraperScrapeResponse.scrapingId, searchId=body.searchId)
    return scraperScrapeResponse

@api_scraper_router.get("/scraper/scrape", response_model=List[ScraperSchema.ScraperScrape], tags=["Scraper Api"])
async def get_scraping_details(scrapingId: Optional[str] = None):
    # gets scraping details from db
    scrapingResponseList = ScraperService.getScrapings(scrapingId)
    return scrapingResponseList

@api_scraper_router.get("/scraper/scrapeResults", response_model=List[ScraperSchema.ScraperScrapeResultsResponse], tags=["Scraper Api"])
async def get_scraping_results(scrapingId: Optional[str] = None, searchId: Optional[str] = None):
    scrapingResultsItems = []
    # gets scraping results from db
    if(searchId == None):
        scrapingResultsItems = ScraperService.getScrapingResults(scrapingId)
    else:
        scrapingResultsItems = ScraperService.getScrapingResultsBySearchId(searchId)

    return scrapingResultsItems