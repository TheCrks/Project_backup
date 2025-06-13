import requests, extraction
from bs4 import BeautifulSoup

class SpringerBot:
    
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
        abstract = ""
        metadata = {""}
        try:
            soup = self.siteToSoup(siteUrl, headers, cookies)

            if(soup != None):
                abstractElement = soup.find('div', class_="c-article-section__content")
                if abstractElement != None:
                    children = abstractElement.findChildren("p" , recursive=False)

                    abstract = ""
                    for child in children:
                        abstract += child.get_text()+" "
                    try:
                        metric_items = soup.find_all("li", class_="app-article-metrics-bar__item")
                        for item in metric_items:
                            count_tag = item.find("p", class_="app-article-metrics-bar__count")
                            label_tag = item.find("span", class_="app-article-metrics-bar__label")

                            if count_tag and label_tag:
                                count_text = count_tag.get_text(strip=True)
                                label_text = label_tag.get_text(strip=True).lower()
                                accesses = "0"
                                citations = "0"
                                if "accesses" in label_text:
                                    accesses = count_text
                                elif "citations" in label_text:
                                    citations = count_text
                                metadata = {
                                    "accesses": "0",
                                    "citations": citations,
                                }
                                return abstract , metadata
                    except Exception as ex:
                        print("Failed to get metrics:", ex)
                        metadata = {
                            "accesses": "0",
                            "citations": "0",
                        }
                    return abstract, metadata
                else:
                    return ""
            else:
                return ""
        except Exception as ex:
            print(ex)