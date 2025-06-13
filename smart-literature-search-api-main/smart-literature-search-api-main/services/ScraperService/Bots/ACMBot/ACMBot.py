import requests
from bs4 import BeautifulSoup


class ACMBot:

    def __init__(self):
        # constants
        self.session = requests.Session()

    def siteToSoup(self, siteUrl, headers, cookies):
        try:
            page = self.session.get(siteUrl, headers=headers, cookies=cookies)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        except Exception as ex:
            print(ex)

    def scrapSite(self, siteUrl, headers, cookies):
        try:
            soup = self.siteToSoup(siteUrl, headers, cookies)

            if soup is not None:
                abstract_section = soup.find("section", id="abstract")
                if abstract_section is not None:
                    paragraph_div = abstract_section.find("div", role="paragraph")
                    if paragraph_div is not None:
                        abstract = paragraph_div.get_text(strip=True)
                        return abstract
                    """else:
                        print("[WARN] Could not find div with role='paragraph'.")
                else:
                    print("[WARN] Could not find section with id='abstract'.")
            else:
                print("[ERROR] Failed to convert site to soup.")"""

            return ""
        except Exception as ex:
            print(f"[EXCEPTION] {ex}")
            return ""

