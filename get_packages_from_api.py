"""
Makes an API call to the host Repology mirror and returns the filtered list with only packages we want and the datetime
"""

from datetime import datetime
import requests

URL = "myurl.com"


def request_repology_api_local(pm):
    local_datetime = datetime.now()
    response = requests.get(URL)
    if response.status_code == 200:
        api_return = response.json()
        package_list = [pkg for pkg in api_return if pkg["package_manager"] == pm]
        return package_list, local_datetime
    else:
        raise requests.HTTPError("Failed to connect to API")
