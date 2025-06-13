# 3rd party
import requests, urllib

# internal imports
from .Config import settings
from .ResponseParser import parseUrls
from .RequestHelper import concatSites, concatTerms

# constants
apiKey = settings.API_KEY
searchEngineKey = settings.SEARCH_ENGINE_KEY
baseUrl = settings.BASE_URL

def searchByQuery(query, sites, exactTerms, excludeTerms, dateRestrict):
    results = []

    params = dict()
    params["key"] = apiKey
    params["cx"] = searchEngineKey
    params["q"] = query + " " + concatSites(sites) + " -inurl:pdf"
    params["exactTerms"] = concatTerms(exactTerms)
    params["excludeTerms"] = concatTerms(excludeTerms)
    params["dateRestrict"] = dateRestrict

    # make api call for 10 times (google api allows 10 page * 10 url for each query and have limited 100 query per day)
    for i in range(1, 92, 10):
        params["start"] = i

        # configure strings
        request_params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)

        # make api call that starts from i'th url
        response = requests.get(baseUrl,params=request_params) 
        
        # parse result
        data = response.json()
        parsedResults = parseUrls(data)

        # append to results
        results += parsedResults

    return results
    