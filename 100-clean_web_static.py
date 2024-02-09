#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
import os


# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
# env.hosts = ['54.236.47.245', '100.26.156.253']
# env.user = "ubuntu"

def do_clean(number=0):
    """ Deletes out-of-date archives """
    number = int(number)
    if number in [0, 1]:
        number == 1
    local('cd versions')
    total = len(os.listdir('.'))
    # local('ls -t | tail -n {} | xargs rm'.format(total - number))
    local('echo "Total: {}\nNumber: +{}" > file.txt'.format(total, number))
