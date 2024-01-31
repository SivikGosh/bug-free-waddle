# TODO: добавить конвертацию xlsx в json (либо сразу писать в бд?)

import csv
import json


def csv_to_json(csv_file, json_file):
    jsonArray = []

    with open(csv_file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)


csv_to_json('bill.csv', 'bill.json')
