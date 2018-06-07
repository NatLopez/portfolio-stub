#retrieve api key from local file
import os
import json
my_api_key = os.getenv('API_KEY')

#import DPLA wrapper
from dpla.api import DPLA

#connect to DPLA wrapper
dpla_connection = DPLA(my_api_key)

#this returns all results with search term austen
result = dpla_connection.search('cat')
# print(type(result))

# print(str(result.__dict__)[:500])

item = result.items[0]
print(json.dumps(item, sort_keys=True,indent=4))
# print(item['sourceResource']['stateLocatedIn'])
#
# for item in result.items[:9]:
#     print(item['sourceResource']['stateLocatedIn'])

# print (result.items[4]['sourceResource']['stateLocatedIn'])

# for item in result.items[:9]:
#     if 'stateLocatedIn' in item['sourceResource']:
#         print(item['sourceResource']['stateLocatedIn'])
#     else:
#         print(item['sourceResource']['format'])
