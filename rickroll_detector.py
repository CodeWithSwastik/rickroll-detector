import requests

def find_rickroll(url):
    source = str(requests.get(url).content).lower()
    rickrolls = ["rickroll","rick roll","rick astley"]
    for i in rickrolls:
        if i in source:
            return True
        
    return False
