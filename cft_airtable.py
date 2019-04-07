# requires
# pip install airtable
# and
# pip install airtable-python-wrapper

import json
from airtable import Airtable
from collections import OrderedDict

BASE_ID = "app38cZA2uPDxdTL8" # found in url of API documentation for table
TABLE_NAME = "Services"

airtable = Airtable(BASE_ID, TABLE_NAME)
records = airtable.get_all()

service_list = []
for record in records:
    od = OrderedDict()
    try:
        od['name'] = record['fields']['Name']
    except KeyError:
        pass
    try:
        od['desc'] = record['fields']['Desc']
    except KeyError:
        pass
    try:
        for record_id in record['fields']['Icons']:
            od["icons"] = record_id
            # TODO access Icon table and get its fields
            #od["icons"]["icon"] = record_id["icon"]
            #od["icons"]["text"] = record_id["text"]
    except KeyError:
        pass
    service_list.append(od)

with open("output.json", "w") as f:
    json.dump(service_list, f, indent=2)
