#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.22.118", "52.90.13.68"]

