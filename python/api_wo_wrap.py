#'requests' is a library that allows you to make requests to an API
import requests
import os
import math

my_api_key = os.getenv('API_KEY')

#dpla endpoint
#we can find out API endpoint by looking at DPLA's great documentation. Not every API provides you with such great guides to their work,
endpoint = 'https://api.dp.la/v2/items'

params = {
    'api_key': my_api_key,
    'q': 'Austin, Texas',
    'page_size':'500'
}

requested_the_hard_way = requests.get(endpoint, params)
requested_the_hard_way.status_code
print(requested_the_hard_way.url)

print(requested_the_hard_way)
#create list to store results of first 20 pages
total_hard_way_results=[]

#how to generate number of pages if you have 500 results per page
total_results = requested_the_hard_way.json()['count']
number_of_pgs=math.ceil(total_results/500)
print (number_of_pgs)

#how to generate a list of items on the first 20 pages
list_of_page_numbers = range(1,21,1)
for page_num in list_of_page_numbers:
    # add a param called page that will let us know what page we're on
    params['page']=page_num

    #get the results that fit the new parameters and add them to list
    for result in requests.get(endpoint, params).json()['docs']:
        total_hard_way_results.append(result)

#how to print first item record
item1=requested_the_hard_way.json()['docs'][0]
# print(item1)

#counting the number of record per state
state_results={}
state_results['other_format']=0
for item in total_hard_way_results:
    if 'stateLocatedIn' in item['sourceResource']:
        if item['sourceResource']['stateLocatedIn'][0]['name'] in state_results:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']]+=1
        else:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']]=1
    elif 'format' in item['sourceResource'] and item['sourceResource']['format']!='Text':
        state_results['other_format']+=1
    else:
        pass
print(state_results)

#enter search term, generate results with search other_format
