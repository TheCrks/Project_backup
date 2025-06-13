import requests
from bs4 import BeautifulSoup

from .Config import settings

class ResearchgateBot:

    def __init__(self):
        # constants
        self.username = settings.LOGIN
        self.password = settings.PASSWORD
        self.headers = settings.HEADERS
        self.token = settings.REQUEST_TOKEN
        self.loginEndpoint = settings.ENDPOINT
        self.authenticated = False
        self.session = requests.Session()

    def login(self):
        if(self.authenticated == False):
            data = {
                "request_token": self.token,
                "invalidPasswordCount": "0",
                "login": self.username,
                "password": self.password,
                "setLoginCookie": "on"
            }

            response = self.session.post(self.loginEndpoint, headers=self.headers, data=data, timeout=20)
            print("login success: " ,response.text)

            if response.status_code == 200:
                self.authenticated = True

    def siteToSoup(self, siteUrl, headers, cookies):
        try:
            page = self.session.get(siteUrl,headers=headers,cookies=cookies)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        except Exception as ex:
            print(ex)
            return ""

    def scrapSite(self, siteUrl, headers, cookies):
        try:
            print(f"[DEBUG] Attempting to fetch: {siteUrl}")
            soup = self.siteToSoup(siteUrl, headers, cookies)

            if soup is not None:
                print("[DEBUG] Page fetched successfully. Checking for abstract element...")

                # Print a snippet of the HTML for manual inspection
                print("[DEBUG] First 500 characters of page content:")
                print(soup.prettify()[:500])  # or soup.body.prettify()[:500] if body exists

                abstractElement = soup.find(
                    "div",
                    class_="nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-grey-800 research-detail-middle-section__abstract"
                )

                if abstractElement is not None:
                    print("[DEBUG] Abstract container found.")
                    abstractElement = abstractElement.find("div")
                    if abstractElement:
                        abstract = abstractElement.get_text(strip=True)
                        print(f"[DEBUG] Extracted abstract: {abstract[:200]}...")  # print a short preview
                        return abstract
                    else:
                        print("[DEBUG] Inner div inside abstract container not found.")
                        return ""
                else:
                    print("[DEBUG] Abstract container not found in HTML.")
                    return ""
            else:
                print("[DEBUG] Failed to fetch page or parse HTML.")
                return ""
        except Exception as ex:
            print("[ERROR] Exception during scraping:", ex)
            return ""

