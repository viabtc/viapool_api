#!/usr/bin/python
# -*- coding: utf-8 -*-

import hmac
import json
import time
from hashlib import sha256
from urllib import urlencode

import requests

api_key = '<your api key>'
secret_key = '<your secret key>'


def get_account_hashrate():
    # api without signature, send request with X-API-KEY header
    args = {'coin': 'BTC'}
    headers = {'X-API-KEY': api_key}
    r = requests.get('https://pool.viabtc.com/res/openapi/v1/hashrate', params=args, headers=headers)
    print r.text


def get_subaccount():
    # api with signature, add tonce parameter, get query_string by urlencode(in any order)
    args = {'tonce': int(time.time() * 1000)}
    query_string = urlencode(args)
    # calculate hmac sha256 signature of query_string with secret_key
    signature = hmac.new(secret_key, query_string, sha256).hexdigest()
    headers = {
        'X-API-KEY': api_key,
        'X-SIGNATURE': signature
    }
    # send the request with X-API-KEY and X-SIGNATURE header.
    r = requests.get('https://pool.viabtc.com/res/openapi/v1/account/sub?' + query_string, headers=headers)
    print r.text


if __name__ == '__main__':
    get_account_hashrate()
    get_subaccount()
