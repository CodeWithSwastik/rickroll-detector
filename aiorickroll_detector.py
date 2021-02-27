import aiohttp
import re

async def aiorickroll_detector(url):
    source = str(requests.get(url).content).lower()
    return re.findall('rickroll|rick roll|rick astley', source, re.MULTILINE)
