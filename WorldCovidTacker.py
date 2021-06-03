import requests
import json

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

querystring = {"date":"2021-06-02"}

headers = {
    'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4))
print("Total number of COVID cases in the world  till", parsed["data"]["date"], "is", parsed["data"]["confirmed"])
print("Total number of deaths in the world  till", parsed["data"]["date"], "is", parsed["data"]["deaths"])
print("Active number of COVID cases in the world  till", parsed["data"]["date"], "is", parsed["data"]["active"])
print("Total number of recoveries in the world  till", parsed["data"]["date"], "is", parsed["data"]["recovered"])



