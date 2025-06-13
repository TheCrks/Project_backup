from pydantic import BaseModel
from typing import List, Optional

# search schema


class CrawlerSearch(BaseModel):
    id: Optional[str]
    keyword: str
    username: str
    date: str
    queryName: str
    status: Optional[str]
    sites: List[str]
    dateRestrict: Optional[str]
    exactTerms: Optional[List[str]]
    excludeTerms: Optional[List[str]]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "de277f84-50f3-41b9-b03f-49b5e49a8e64",
                "keyword": "machine learning",
                "username": "mmutlu",
                "date": "22.08.2021",
                "queryName": "AI Researches",
                "status":"In Progress",
                "sites": ["ieeexplore.ieee.org", "researchgate.net"],
                "dateRestrict": "w1",
                "exactTerms":["artificial intelligence","deep learning"],
                "excludeTerms":["neural networks"]
            }
        }

# response for new search


class CrawlerSearchResponse(BaseModel):
    searchId: str

    class Config:
        json_schema_extra = {
            "example": {
                "searchId": "8f5b18d9-6698-4ce8-825a-81b6d8a1c384"
            }
        }

# sub item for getting search results

class SearchIdList(BaseModel):
    searchIds: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "searchIds": ["de277f84-50f3-41b9-b03f-49b5e49a8e64", "8f5b18d9-6698-4ce8-825a-81b6d8a1c384"]
            }
        }


class CrawlerSearchResultsItem(BaseModel):
    url: str
    title: str

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://www.researchgate.net/publication/327579184_On_the_Issues_of_Communication_in_FANET_A_Light_Fidelity_Based_Approach",
                "title": "(PDF) On the Issues of Communication in FANET: A Light Fidelity ..."
            }
        }

# response for getting search results


class CrawlerSearchResultsResponse(BaseModel):
    searchId: str
    results: List[CrawlerSearchResultsItem]

# sub item for getting search results


class Counts(BaseModel):
    totalSearches: int
    dailySearches: int
    finishedSearches: int

    class Config:
        json_schema_extra = {
            "example": {
                "totalSearches": 324,
                "dailySearches": 5,
                "finishedSearches": 3,
                "failedSearches": 0
            }
        }
