#!/usr/bin/env python

import sys
import requests
import base64
import hashlib

from conf import data, sse_key

url = sys.argv[1]

sse_key_base64 = base64.standard_b64encode(sse_key)
sse_key_md5 = hashlib.md5(sse_key).digest()
sse_key_md5_base64 = base64.standard_b64encode(sse_key_md5)

headers = {}
headers['x-amz-server-side-encryption-customer-algorithm'] = 'AES256'
headers['x-amz-server-side-encryption-customer-key'] = sse_key_base64
headers['x-amz-server-side-encryption-customer-key-MD5'] = sse_key_md5_base64

from conf import checksum_header_name, data_checksum
headers[checksum_header_name] = data_checksum

ret = requests.put(url, data=data, headers=headers)
print(ret)
print(ret.text)

