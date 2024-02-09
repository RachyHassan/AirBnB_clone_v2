#!/usr/bin/python3
"""Clean up my web static"""
from fabric.api import local, env, run


# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
env.hosts = ['54.236.47.245', '100.26.156.253']
env.user = "ubuntu"


def do_clean(number=0):
    """ Deletes out-of-date archives """
    number = int(number)
    if number in [0, 1]:
        number = 2
    else:
        number += 1
    # tail -n +{NUM} => use  -n +NUM to output starting with line NUM
    local(f'cd ./versions; ls -t | tail -n +{number} | xargs rm -rf')
    folder = '/data/web_static/releases'
    run(f'cd {folder}; ls -t | tail -n +{number} | xargs rm -rf')
