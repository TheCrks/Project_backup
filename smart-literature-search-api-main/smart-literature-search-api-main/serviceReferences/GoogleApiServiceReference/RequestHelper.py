def concatSites(sitesList):
    sitesString = ""
    for idx, site in enumerate(sitesList):
        if (idx == len(sitesList) - 1):
            sitesString += "site:" + site
        else:
            sitesString += "site:" + site + " OR "

    return sitesString

def concatTerms(termsList):
    terms = ""
    for idx, term in enumerate(termsList):
        if(idx == len(termsList) -1 ):
            terms += "\""+term+"\""
        else:
            terms += "\""+term+"\" "
    
    return terms