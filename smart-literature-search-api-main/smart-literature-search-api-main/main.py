#3rd party
from fastapi import FastAPI

# api routers
from api.CrawlerApi import api_crawler_router
from api.LoggerApi import api_logger_router
from api.ScraperApi import api_scraper_router
from api.SorterApi import api_sorter_router
import services

# api configs & initialiser
from core import Config
from initialiser import configureCors

# uvicorn
import uvicorn

# create uvicorn app
app = FastAPI(title=Config.settings.PROJECT_NAME)

# configure cors
app = configureCors(app)

# define routes
app.include_router(api_crawler_router,prefix=Config.settings.API_V1_STR)
app.include_router(api_scraper_router,prefix=Config.settings.API_V1_STR)
app.include_router(api_sorter_router,prefix=Config.settings.API_V1_STR)
app.include_router(api_logger_router, prefix=Config.settings.API_V1_STR)
if __name__ == "__main__":
      uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

#localhost:8000/docs for swagger