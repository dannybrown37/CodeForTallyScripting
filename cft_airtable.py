# requires pip install airtable
# and
# pip install airtable-python-wrapper

import simplejson
from airtable import Airtable
from pprint import pprint
from collections import OrderedDict

BASE_ID = "app38cZA2uPDxdTL8" # found in url of API documentation for table
TABLE_NAME = "Services"

airtable = Airtable(BASE_ID, TABLE_NAME)
records = airtable.get_all()

service_list = []
for record in records:
    od = OrderedDict()
    od['name'] = record['fields']['Name']
    od['desc'] = record['fields']['Desc']
    od['icons'] = record['fields']['Icons']
    service_list.append(od)

with open("output.json", "w") as f:
    simplejson.dump(service_list, f, indent=2)
