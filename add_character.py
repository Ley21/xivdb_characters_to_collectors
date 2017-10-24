import requests
import json

def addCharacter(x):
    url = 'http://ffxivcollector.com/handler/charakter.php?id=%d&show=false' % (x)
    ret = requests.get(url)
    return ret.text
    
def getId(x):
    url = 'http://api.xivdb.com/character/%d' % (x)
    ret = requests.get(url)
    if ret.status_code != 404:
        json_data = json.loads(ret.text)
        minions = len(json_data['data']['minions'])
        if minions > 150:
            return x
        return None
    
for index in range(14000000):
    result = getId(index)
    if result != None:
        print addCharacter(result)