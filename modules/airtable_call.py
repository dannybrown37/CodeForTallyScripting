# requires
# pip install airtable
# pip install airtable-python-wrapper

import json
import airtable
from airtable import Airtable

BASE_ID = "app38cZA2uPDxdTL8" # found in url of API documentation for table
SERVICES_TABLE = "Services"

def create_services_object():
    return Airtable(BASE_ID, SERVICES_TABLE)

def airtable_call():
    services_object = create_services_object()
    records = services_object.get_all(sort="ID")

    service_list = []
    for record in records:
        od = { # Original Dictionary
            "id" : record['fields']['ID'],
            "name" : record['fields']['Name'],
            "desc" : record['fields']['Desc'],
            "icons" : []
        }
        for record_id in record['fields']['Icons']:
            icon_record = services_object.get(record_id)
            od["icons"].append({
                "text" : icon_record['fields']['text'],
                "icon" : icon_record['fields']['icon']
            })

        service_list.append(od)

    # Output is not used but can be useful for debugging
    #with open("output.json", "w") as f:
    #    json.dump(service_list, f, indent=2)

    return service_list
