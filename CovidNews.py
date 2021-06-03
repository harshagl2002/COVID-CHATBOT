import requests
import json 

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-coronavirus-news/0"

headers = {
    'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
parsed = json.loads(response.text)
#print(json.dumps(parsed, indent=4))
for i in range (0,len(parsed["news"])):
    print()
    print(parsed["news"][i]["title"])
    print(parsed["news"][i]["link"])
    print()
