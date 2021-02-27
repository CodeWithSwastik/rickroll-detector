import requests
import re

def find_rickroll(url):
    source = str(requests.get(url).content).lower()
    return re.findall('rickroll|rick roll|rick astley', source, re.MULTILINE)
