# 3rd party
import json

def parseUrls(responseData):
    results = []

    if "items" in responseData:
        items = responseData["items"]

        for item in items:            
            result = {"title":item["title"],"url":item["link"]}
            results.append(result)

    return results