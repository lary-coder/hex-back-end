#!/usr/bin/python3
"""
script that use REST API for returns information
about employee TODO list progress
"""


import requests as res
from sys import argv


def getApi(u):
    """A function that returns to do list"""
    user = int(u)
    done = 0
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user}).json()
    empl = res.get('https://jsonplaceholder.typicode.com/users',
                   params={'id': user}).json()

    for i in range(len(todo)):
        if todo[i]['completed'] is True:
            done = done+1
    undone = len(todo)
    name = empl[0]['name']
    print("Employee {} is done with tasks({}/{}):".format(name, done, undone))

    for i in range(len(todo)):
        if todo[i]['completed'] is True:
            print("\t {}".format(todo[i]['title']))


if __name__ == '__main__':
    getApi(argv[1])
