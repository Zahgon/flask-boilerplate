#!/usr/bin/env python
import os

from app import create_app

app = create_app('config.development')

os.environ['PYTHONINSPECT'] = 'True'
