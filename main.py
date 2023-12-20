import json

with open('sample.json', encoding="utf-8") as json_file:
    data = json.load(json_file)


for company in data["companies"]:
    for contact in company["contacts"]:
        print(contact["Phone"])