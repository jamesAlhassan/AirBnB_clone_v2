#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ["100.25.22.118", "52.90.13.68"]

def do_clean(number=0):
    ''' Remove old archives '''
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
