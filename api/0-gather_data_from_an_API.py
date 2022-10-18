#!/usr/bin/python3
import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/todos/'.format(sys.argv[1])
api_url_2 = 'https://jsonplaceholder.typicode.com/{}/'.format(sys.argv[1])
names_and_tasks = requests.get(api_url)
result = names_and_tasks.json()
titles = requests.get(api_url_2)
result_1 = titles.json()

empl_name = result_1.get('name')

count = 0
count_1 = 0

for value in result:
    if value.get('userId') == int(sys.argv[1]):
        count_1 += 1
    if value.get('completed') and value.get('userId') == int(sys.argv[1]):
        count += 1 
    print('Employee', empl_name 'is done with tasks(', count_1'/'count '):')
    
for value in result:
    if value.get('completed') and value.get('userId') == int(sys.argv[1]):
     print('\t' value['title'])    