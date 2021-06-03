import requests
import json

url = "https://covid-193.p.rapidapi.com/history"

country = "Papua New Guinea"
date = "2020-12-31"

querystring = {"country":country,"day":date}

headers = {
    'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))
if parsed["results"] == 0:
    print("Data Not availible for this country. Sorry")
else:
    response_dict = parsed["response"][0]
    cases_dict = response_dict["cases"]
    print("new cases in", parsed["parameters"]["country"], "on", response_dict["day"], "is", cases_dict["new"])
    print("Number of deaths recorded in", parsed["parameters"]["country"], "on", response_dict["day"], "is", response_dict["deaths"]["new"])
    print("Number of recoveries recorded in", parsed["parameters"]["country"], "till", response_dict["day"], "is", cases_dict["recovered"])
    print("Total number of tests conducted in", parsed["parameters"]["country"], "till", response_dict["day"], "is", response_dict["tests"]["total"])