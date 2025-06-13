from datetime import date

def getToday():
    return date.today().strftime("%d.%m.%Y")