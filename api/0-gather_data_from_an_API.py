#!/usr/bin/python3

"""
Module
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    url_2 = "https://jsonplaceholder.typicode.com/users/{}/".format(
        sys.argv[1])

    response = requests.get(url)
    result = response.json()
    response_2 = requests.get(url_2)
    result_2 = response_2.json()

    item_2 = result_2.get('name')

    count = 0
    count_2 = 0

    for item in result:
        if item.get('userId') == int(sys.argv[1]):
            count_2 += 1
        if item.get('completed') and item.get('userId') == int(sys.argv[1]):
            count += 1
    print('Employee {} is done with tasks({}/{}):'.format(item_2,
                                                          count, count_2))

    for item in result:
        if item.get('completed') and item.get('userId') == int(sys.argv[1]):
            print("\t {}".format(item['title']))