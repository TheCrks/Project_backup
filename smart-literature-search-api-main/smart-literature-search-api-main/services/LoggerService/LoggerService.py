from schemas import LoggerSchema
from serviceReferences.FirebaseServiceReference import FirebaseServiceReference

def logTrainData(body: LoggerSchema.Logs):
    try:
        FirebaseServiceReference.insertLogData(body)
        response = {
            "result" : "Success"
        }
        return response
    except Exception as e:
        print(e)
        response = {
            "result" : "Failed"
        }
        return response