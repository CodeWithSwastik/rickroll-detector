import aiohttp
import re
  
class RickRollDetector(aiohttp.ClientSession):
  
  async def find(self, url):
      source = str((await self.get(url)).content).lower()
      phrases = ["rickroll","rick roll","rick astley","never gonna give you up"]
      return bool(re.findall("|".join(phrases), source, re.MULTILINE))
