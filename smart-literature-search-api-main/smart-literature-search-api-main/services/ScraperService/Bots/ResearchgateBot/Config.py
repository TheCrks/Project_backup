from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENDPOINT: str = "https://www.researchgate.net/login"
    LOGIN: str = "muhammedmutlu@marun.edu.tr"
    PASSWORD: str = "2L8ib8()v4+eB<p"
    REQUEST_TOKEN: str = "aad-TZzfFJSTn5rvpySE7DguBViTdkKYwOQe97vX7RnWxlf4DZ9WpyNp3TdqaOKKq9lt7fepAnBLpOwW6Ek8TW5^%^2FgkhoZyjDNKRjd54rkn40k9wsBYGmRTpL^%^2B0Tecu^%^2FFeYyrsQbGeV72tzuf19Lvsfy3YSE2lQ1Vws^%^2BlE7hgNyVdVOWuc0N1ldmnqsGnGdmi1zd2Q1D9qyJQrhFzfQFmR8q3mP2epRH9HJk8Iz3NbQZOk^%^2BfDcZYhqN8wTmGTO^%^2BPTyQKDL2J^%^2BZFgqEq7saw1K2T8^%^3D"
    HEADERS: dict = {
        'authority': 'www.researchgate.net',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.researchgate.net',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.researchgate.net/login',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'did=oSrEYdtNsPuQCvlb3BNjeB9qe0As90FZHj1S11l0lTnL7W0YhiCyJYaMwH76er1D; ptc=RG1.1906516378356924725.1604576329; _ga=GA1.2.1983409586.1604576342; __gads=ID=7dde8191e1295162:T=1604576338:S=ALNI_MbLV-BdE1_f_CURsN7_YVuyseqyFg; rghfp=true; GED_PLAYLIST_ACTIVITY=W3sidSI6IjFiYzAiLCJ0c2wiOjE2MDgxMjQ0NjQsIm52IjowLCJ1cHQiOjE2MDgxMTk4NjEsImx0IjoxNjA4MTIyOTg2fV0.; chseen=1; cf_clearance=3045f221f4b69ea261ea7d7b75ff4a309898c5a6-1610829506-0-250; _pbjs_userid_consent_data=3524755945110770; __qca=I0-160370822-1616178413797; __cfduid=d700cacd40a6d28eede2bed104006075c1617011468; captui=NTk4NTIxMDI4OTllMDkwMjEyMWZkZTg1MWIwZGI1MjQ4ODAzNzU0OGQ5ODdkNDNkZjk4YzRmZWM2ODhhNjczNV9FUDFCTTNoSFhNZWZOMHNHR0lQaFl3Zzk2TjlJR3hmaTA5SzY^%^3D; SKpbjs-unifiedid=^%^7B^%^22TDID^%^22^%^3A^%^227e5d2e80-d984-4040-9e16-2d4486c3415b^%^22^%^2C^%^22TDID_LOOKUP^%^22^%^3A^%^22TRUE^%^22^%^2C^%^22TDID_CREATED_AT^%^22^%^3A^%^222021-03-15T09^%^3A55^%^3A38^%^22^%^7D; SKpbjs-unifiedid_last=Thu^%^2C^%^2015^%^20Apr^%^202021^%^2009^%^3A55^%^3A41^%^20GMT; id5id.1st_212_nb=73; _gid=GA1.2.1792219045.1619001550; isResearcher=yes; classification=institution; cirgu=_1_TUSsoW2QBCE4zVbCoS3xBYLvKePdi129mhcC09ZMNU5SclGbWnG^%^2B4G^%^2FHFLoDjXt4wmHwSJPn; _gat=1; _gat_UA-58591210-1=1; sid=zXS7mbk5nTGH6zo49ysx46e5tzVmsH0lLOFFXytfA1jZUBOwE6BKm0bM6ogFMj60eR2nR94alw2umMe8xrgOBOz5hzm1SxcXcWrMDntyZXV1Q0YseHF9ZozsaRG0VcoP',
    }

settings = Settings()
