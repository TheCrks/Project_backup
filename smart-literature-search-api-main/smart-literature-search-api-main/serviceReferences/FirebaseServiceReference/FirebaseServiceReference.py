import uuid
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.api_core import retry
from datetime import timedelta


def init():
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "./serviceReferences/FirebaseServiceReference/config.json")

            global app

            app = firebase_admin.initialize_app(cred, {
                'projectId': 'smart-literature-search-new',
            })

        return firestore.client()
    except Exception as ex:
        print(ex)


def closeConnection():
    firebase_admin.delete_app(app)



def readSearches(searchId):
    searchId = str(searchId)
    fireStoreClient = init()
    try:

        try:
            search_ref = fireStoreClient.collection(u'search').where(
                u'id', u'==', searchId) if searchId != None else fireStoreClient.collection(u'search')

            docs = search_ref.get()
            return list(docs)
        except Exception as e:
            print(f"Error executing Firestore query: {str(e)}")
            return []

    except Exception as e:
        print(f"Error in readSearches: {str(e)}")
        return []
    finally:
        closeConnection()


def insertSearch(keyword, username, sites, date, queryName, exactTerms, excludeTerms, dateRestrict):
    fireStoreClient = init()
    try:
        id = str(uuid.uuid4())

        tableReference = fireStoreClient.collection(u'search').document()
        tableReference.set({
            u'id': id,
            u'keyword': keyword,
            u'username': username,
            u'sites': sites,
            u'date': date,
            u'queryName': queryName,
            u'status': 'Started',
            u'exactTerms': exactTerms,
            u'excludeTerms': excludeTerms,
            u'dateRestrict': dateRestrict
        })
        return id
    finally:
        closeConnection()


def updateSearchStatus(searchId, status):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'search').where(u'id', u'==', searchId).get()
    for docSnapshot in search_ref:
        docSnapshot.reference.update({u'status':status})
    
    closeConnection()

def readSearchResults(searchId):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'searchResults').where(
        u'searchId', u'==', searchId) if searchId != None else fireStoreClient.collection(u'searchResults')
    docs = search_ref.stream()

    closeConnection()
    return docs


def insertSearchResults(searchId, results):
    fireStoreClient = init()

    tableReference = fireStoreClient.collection(u'searchResults').document()
    tableReference.set({
        u'searchId': searchId,
        u'results': results
    })

    closeConnection()

# scraper
# TODO: Replace .where() with .filter() to avoid warning

def readScrapings(scrapingId):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'scraping').where(
        u'id', u'==', scrapingId) if scrapingId != None else fireStoreClient.collection(u'scraping')
    docs = search_ref.stream()

    closeConnection()
    return docs


def insertScraping(searchId, username):
    fireStoreClient = init()

    id = str(uuid.uuid4())

    tableReference = fireStoreClient.collection(u'scraping').document()
    tableReference.set({
        u'id': id,
        u'searchId': searchId,
        u'username': username
    })

    closeConnection()
    return id

def readScrapingStatus(searchId):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'scraping').where(u'searchId', u'==', searchId) if searchId != None else fireStoreClient.collection(u'scraping')
    docs = search_ref.stream()

    closeConnection()
    return docs

def updateScrapingStatus(scrapingId, status):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'scraping').where(u'id', u'==', scrapingId).get()
    for docSnapshot in search_ref:
        docSnapshot.reference.update({u'status':status})
    
    closeConnection()


def readScrapingResults(scrapingId):
    fireStoreClient = init()

    search_ref = fireStoreClient.collection(u'scrapingResults').where(
        u'scrapingId', u'==', scrapingId) if scrapingId != None else fireStoreClient.collection(u'scrapingResults').get()
    docs = search_ref.stream()

    closeConnection()
    return docs


def insertScrapingResults(scrapingId, results):
    fireStoreClient = init()

    tableReference = fireStoreClient.collection(u'scrapingResults').document()
    try:
        tableReference.set({
            u'scrapingId': scrapingId,
            u'results': results
        })
    except Exception as ex:
        print("Error Writing Result To Database: ", ex)

    closeConnection()


def insertLogData(log):
    fireStoreClient = init()

    tableReference = fireStoreClient.collection(u'trainingLogs').document()
    try:
        id = str(uuid.uuid4())
        tableReference.set({
            u'logID': id,
            u'action': log.action,
            u'itemId': log.itemId,
            u'title': log.title,
            u'url': log.url,
            u'searchId': log.searchId,
            u'timestamp': log.timestamp,
            u'rank': log.rank,
        })
    except Exception as ex:
        print("Error Writing Result To Database: ", ex)

    closeConnection()


def fetch_and_format_logs():
    fireStoreClient = init()

    def readTrainingLogs():
        tableReference = fireStoreClient.collection(u'trainingLogs')
        return tableReference.stream()

    def getKeywords(search_id_key):
        # Search by 'id' field (not document ID)
        search_query = fireStoreClient.collection(u'search') \
            .where("id", "==", search_id_key) \
            .limit(1) \
            .stream()

        search_doc = next(search_query, None)

        if not search_doc or not search_doc.exists:
            print(f"Search Result Not Found for searchId: {search_id_key}")
            return []

        search_data = search_doc.to_dict()
        words = [search_data.get("keyword", "")] + search_data.get("exactTerms", [])
        return words

    def getScrapingId(search_id_scr):
        scrapings_query = fireStoreClient.collection(u'scraping') \
            .where("searchId", "==", search_id_scr).limit(1).stream()
        for scrap in scrapings_query:
            scrap_data = scrap.to_dict()
            return scrap_data.get("id")
        print("Scraping Id Not Found")
        return None

    dataset = []
    training_logs = readTrainingLogs()

    for log in training_logs:
        log_data = log.to_dict()
        search_id = log_data.get("searchId")
        item_title = log_data.get("title")
        rank = int(log_data.get("rank", -1))
        action = log_data.get("action")

        label = (1 if action in ['click_action']
                 else 1.2 if action in ['click_url']
                else 0)

        keywords = getKeywords(search_id)
        scraping_id = getScrapingId(search_id)

        if not scraping_id:
            print(f"Scraping Id Not Found: {search_id}")
            continue  # Skip if no scrapingId

        # Step 3: Get scrapingResults document with that scrapingId
        scraping_results_query = fireStoreClient.collection(u'scrapingResults') \
            .where("scrapingId", "==", scraping_id) \
            .limit(1).stream()

        for doc in scraping_results_query:
            doc_data = doc.to_dict()
            results_list = doc_data.get("results", [])

            for result in results_list:
                if result.get("title", "").strip() == item_title.strip():
                    sample = {
                        "features": {
                            "title": result.get("title", ""),
                            "abstract": result.get("data", ""),  # 'data' is the abstract
                            "keywords": keywords,
                            "rank": rank
                        },
                        "label": label
                    }
                    dataset.append(sample)
                    break  # Found the item, no need to check the rest

    return dataset

def clearLogs():
    try:
        fireStoreClient = init()
        tableReference = fireStoreClient.collection(u'trainingLogs')
        delete_collection(tableReference,100)
        return "Collection Deleted Successfully"
    except Exception as ex:
        print("Error Deleting Collection: ", ex)
        return "Error Deleting Collection"



def delete_collection(coll_ref, batch_size):
    if batch_size == 0:
        return None

    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
    return None