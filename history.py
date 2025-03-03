import pickledb
from utils import log, basePath

history = pickledb.load(basePath() + "/history.db", True)
try:
    history.lget("events", 0)
except:
    log("History doesn't exist, creating!", "warn")
    history.lcreate("events")

log("Loaded history with " + str(history.llen("events")) + " events!")

def saveEvent(event):
    history.ladd("events", event)

def getLength():
    return history.llen("events")

def fetchEvents(count):
    length = history.llen("events")
    return history.lrange("events", length-count, length)