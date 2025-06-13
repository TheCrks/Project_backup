import requests, extraction
from bs4 import BeautifulSoup

class IEEEBot:
    
    def __init__(self):
        # constants
        self.session = requests.Session()

    def siteToSoup(self,siteUrl, headers, cookies):
        try:
            page = self.session.get(siteUrl,headers=headers,cookies=cookies)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        except Exception as ex:
            print(ex) 

    def scrapSite(self, siteUrl, headers, cookies):
        try:
            soup = self.siteToSoup(siteUrl, headers, cookies)
            with open("debug_output_ieee.html", "w", encoding="utf-8") as f:
                f.write(str(soup.prettify()))
                print("[DEBUG] Saved HTML to debug_output.html")

            if(soup != None):
                ext = extraction.Extractor()

                metadata = ext.extract(soup.prettify(), source_url=siteUrl)
                
                if metadata != None:
                    abstract = metadata.description
                    return abstract
                else:
                    return ""
            else:
                return ""    
        except Exception as ex:
            print(ex)