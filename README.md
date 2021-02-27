![rickroll](https://media.giphy.com/media/10kABVanhwykJW/giphy.gif)

A simple rickroll detector
# Installation 
This isn't a python module on pypi as of now so you'll need to download the rickroll_detector.py file and keep it in the same directory as your main file. <br> <br>
You can also `git clone https://github.com/CodeWithSwastik/rickroll-detector`
# Usage 

```python
from rickroll_detector import find_rickroll

result = find_rickroll("https://youtu.be/oHg5SJYRHA0")
print(result) #returns True
```

# Async Usage 
```python
from async_rickroll_detector import RickRollDetector

detector = RickRollDetector()
await detector.find('https://youtu.be/oHg5SJYRHA0')
```

# Example bot
I also have a bot.py file here which is an example discord bot that will detect rickrolls
