#!/usr/bin/python3

"""
Module of script that gets todo list from an API 
and export resutlts to csv file.
"""

import csv
import requests
import sys 


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_url = '{}users/{}'.format(url, user_id)
    res = requests.get(user_url)
    json_o = res.json()
    name = json_o.get('username')
   
    todos = '{}todos?userId={}'.format(url, user_id)
    res = requests.get(todos)
    tasks = res.json
    list_tasks = []
    for task in tasks:
        list_tasks.append([user_id,
                            name,
                            tasks.get('completed'),
                            tasks.get('title')])

    filename = "{}.csv".format(user_id)
    with open(filename, 'w') as f:
        f_writer = csv.writer(f,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for task in list_tasks:
            f_writer.writerow(tasks)
