#!/usr/bin/python3
"""
 the nodule gets information from an api
"""

import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/todos/'.format(sys.argv[1])
# this is the api url used to get the list of tasks completed 
api_url_2 = 'https://jsonplaceholder.typicode.com/{}/'.format(sys.argv[1])
# this url is used to get names of employees
names_and_tasks = requests.get(api_url)
result = names_and_tasks.json()
titles = requests.get(api_url_2)
result_1 = titles.json()

empl_name = result_1.get('name')

count = 0
count_1 = 0

for value in result:
    if value.get('userId') == int(sys.argv[1]):
        # getting the total tasks supposed to be done
        count_1 += 1
    if value.get('completed') and value.get('userId') == int(sys.argv[1]):
        # getting tasks completed
        count += 1 
    print('Employee', empl_name 'is done with tasks(', count_1'/'count '):')
    
for value in result:
    if value.get('completed') and value.get('userId') == int(sys.argv[1]):
    # getting the titles of tasks supposed to be done
     print('\t' value['title'])    