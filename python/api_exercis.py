#import DPLA wrapper
from dpla.api import DPLA

#retrieve api key from local file
import os
my_api_key = os.getenv('API_KEY')

dpla_connection = DPLA(my_api_key)

#this returns a Return object
result = dpla_connection.search('austen')
print(type(result))

print(str(result.__dict__)[:100])
