import requests
import re

def find_rickroll(url):
    source = str(requests.get(url).content).lower()
    phrases = ["rickroll","rick roll","rick astley","never gonna give you up"]
    return bool(re.findall("|".join(phrases), source, re.MULTILINE))
