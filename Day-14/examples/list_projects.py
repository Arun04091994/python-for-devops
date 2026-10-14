# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://cvarun07788.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0lnfj4EIHulnTipIIhMoGNFgybnuR89qKoU-KpZf2YjFNaVVGOq1lJHbeYBnMSir2Dfwa3uMvcUlGAz7zeX3wgHjdx4oMGnJI0cU7-tODgS-rrV2m2F7AnVndvBOmxp-ACv00I14pUSu1iNDXmHrJsn5gJu6S6RpvE8Uit69rAmo=E5F7F458"

auth = HTTPBasicAuth("cvarun07788@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
