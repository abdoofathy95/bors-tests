import os
import sys
import re
import requests
from requests import Session


ENDPOINT = os.environ['ENDPOINT_SUFFIX']
AFFECTED_FILES = os.environ['AFFECTED_FILES']
# ENDPOINT = 'valid'
# AFFECTED_FILES = ["argocd/environments/prod/eu-central-1/1vapi-1/Dummy.md","argocd/environments/prod/eu-central-1/1vapi-2/Dummy.md"]

def test():
    url = 'https://abdoo.free.beeceptor.com/'
    request = requests.Request(method='GET', url=url+ENDPOINT, headers={})
    prepared = request.prepare()

    print(AFFECTED_FILES)

    print(get_affected_regions_by_file_changes(AFFECTED_FILES, 'prod'))

    session = Session()
    response = session.send(prepared)

    if response.status_code == 400:
        sys.exit("Failed for unknown reason: %s" % (str(response.content)))
    if response.status_code == 200:
        print("Success: %s" % (str(response.content)))


def get_affected_regions_by_file_changes(affected_files, env):
    affected_clusters_by_region = {}

    for path in affected_files:
        match = re.search('argocd/environments/%s/([^/]*)/([^/]*)' % env, path)
        print(match.groups(), path)
        if match and len(match.groups()) == 2:
            region = match.group(1)
            cluster = match.group(2)
            if not affected_clusters_by_region.get(region):
                affected_clusters_by_region[region] = [cluster]
                continue
            affected_clusters_by_region.get(region).append(cluster)

    return affected_clusters_by_region

if __name__ == '__main__':
    test()
