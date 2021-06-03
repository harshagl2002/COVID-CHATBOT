import requests
import json

url = "https://covid-19-statistics.p.rapidapi.com/reports"

querystring = {"date":"2020-08-09","iso":"NZ","region_province":"Auckland"}

headers = {
    'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
data = response.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))
if len(parsed["data"]) == 0:
    print("Data not available")
else:
    data_dict = parsed["data"][0]
    print(data_dict["confirmed_diff"])
