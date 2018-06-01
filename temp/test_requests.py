#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get("http://www.charitystars.com", headers=headers)
print(r.status_code)

r = requests.get("http://httpbin.org/get")
print(r.text)
