# TODO здесь писать код
import json


with open("json_new.json", "r") as file:
    j_new = json.load(file)

with open("json_old.json", "r") as file:
    j_old = json.load(file)

diff_list = ["services", "staff", "datetime"]
result = {}


for key in diff_list:
    if j_old['data'][key] != j_new['data'][key]:
        result[key] = {
            'old_value': j_old['data'][key],
            'new_value': j_new['data'][key]
        }

print(result)
with open('result.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)

