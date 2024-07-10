import urllib.request

def onlineRequest(url):
    pageRawData = urllib.request.urlopen(url)
    return pageRawData.read().decode()