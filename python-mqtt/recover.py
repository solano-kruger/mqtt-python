import urllib.request
import json

with urllib.request.urlopen("https://aula-0405-e89fe-default-rtdb.firebaseio.com/users.json") as url:
    json = json.loads(url.read().decode())

    print(json)
