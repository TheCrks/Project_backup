# 3rd party imports
import time
import requests,json

# internal imports
from .Robots import urlAllowed

# bots
from services.ScraperService.Bots.ACMBot import ACMBot
from services.ScraperService.Bots.IEEEBot import IEEEBot
from services.ScraperService.Bots.SpringerBot import SpringerBot
from services.ScraperService.Bots.ResearchgateBot import ResearchgateBot

researchgateBot = ResearchgateBot.ResearchgateBot()
ieeeBot = IEEEBot.IEEEBot()
acmBot = ACMBot.ACMBot()
springerBot = SpringerBot.SpringerBot()

def scrapBySite(siteUrl, title, headers, cookies):
    try:
        if "researchgate" in siteUrl:
            abstract, metadata = researchgateBot.scrapSite(siteUrl, headers, cookies)
            return {"url":siteUrl,"data":abstract, "title":title}
        elif "springer" in siteUrl:
            abstract, metadata = springerBot.scrapSite(siteUrl, headers, cookies)
            return {"url":siteUrl,"data":abstract, "title":title, "metadata":metadata}
        elif "dl.acm.org" in siteUrl:
            abstract = acmBot.scrapSite(siteUrl, headers, cookies)
            return {"url":siteUrl,"data":abstract, "title":title}
        elif "ieeexplore.ieee.org" in siteUrl:
            abstract = ieeeBot.scrapSite(siteUrl, headers, cookies)
            return {"url":siteUrl,"data":abstract, "title":title}
        return None
    except Exception as e:
        print(e)
        return None


def scrapSites(sitesToScrap):
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    results = []
    for site in sitesToScrap: 
        url = site["url"]
        title = site["title"]
        try:
            if(urlAllowed(url)):
                cookies = requests.head(url)
                results.append(scrapBySite(url, title, headers, cookies))

                time.sleep(0.065)
            else:
                print("site not allowed: "+url)
        except Exception as e:
            print(e)
    return results