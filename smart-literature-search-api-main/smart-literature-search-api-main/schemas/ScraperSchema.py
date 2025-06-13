from pydantic import BaseModel
from typing import List,Optional

# scraping schema
class ScraperScrape(BaseModel):
    id: Optional[str]
    searchId: str
    username: str

    class Config:
        jsob_schema_extra = {
            "example": {
                "id":"62b1c457-95cf-4838-a324-79f11d93ba07",
                "searchId":"8f5b18d9-6698-4ce8-825a-81b6d8a1c384",
                "username":"mmutlu"
            }
        }

# response for new search
class ScraperScrapeResponse(BaseModel):
    scrapingId : str

    class Config:
        json_schema_extra = {
            "example": {
                "scrapingId":"8f5b18d9-6698-4ce8-825a-81b6d8a1c384"
            }
        }

# sub item for getting search results
class ScraperScrapeResultsItem(BaseModel):
    url: str
    data: str = "None"
    title: str = None
    metadata: dict = None

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://www.researchgate.net/publication/319310847_Flying_Ad-Hoc_Networks_FANETs_A_Review_of_Communication_architectures_and_Routing_protocols",
                "data": "With recent technological progress in the field of electronics, sensors and communication systems, the production of small UAVs (Unmanned Air Vehicles) became possible, which can be used for several military, commercial and civilian applications. However, the capability of a single and small UAV is inadequate. Multiple-UAVs can make a system that is beyond the limitations of a single small UAV. A Flying Ad hoc Networks (FANETs) is such kind of network that consists of a group of small UAVs connected in ad-hoc manner, which are integrated into a team to achieve high level goals. Mobility, lack of central control, self-organizing and ad-hoc nature between the UAVs are the main features of FANETs, which could expand the connectivity and extend the communication range at infrastructure-less area. On one hand, in case of catastrophic situations when ordinary communication infrastructure is not available, FANETs can be used to provide a rapidly deployable, flexible, self-configurable and relatively small operating expenses network; the other hand connecting multiple UAVs in ad-hoc network is a big challenge. This level of coordination requires an appropriate communication architecture and routing protocols that can be set up on highly dynamic flying nodes in order to establish a reliable and robust communication. The main contribution of this paper include the introduction of suitable communication architecture, and an overview of different routing protocols for FANETs. The open research issues of existing routing protocols are also investigated in this paper.",
                "title": "FANET",
                "metadata": {"Accesses": 0 , "Cites": 0}
            }
        }

# response for getting search results
class ScraperScrapeResultsResponse(BaseModel):
    scrapingId: str
    results: List[ScraperScrapeResultsItem]    
    