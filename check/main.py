import os
import sys

import requests
from requests import Session


ENDPOINT = os.environ['ENDPOINT_SUFFIX']


def test():
    url = 'https://abdoo.free.beeceptor.com/'
    request = requests.Request(method='GET', url=url+ENDPOINT, headers={})
    prepared = request.prepare()

    session = Session()
    response = session.send(prepared)

    if response.status_code == 400:
        sys.exit("Failed for unknown reason: %s" % (str(response.content)))
    if response.status_code == 200:
        print("Success: %s" % (str(response.content)))


if __name__ == '__main__':
    test()
