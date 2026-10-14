# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://cvarun07788.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0lnfj4EIHulnTipIIhMoGNFgybnuR89qKoU-KpZf2YjFNaVVGOq1lJHbeYBnMSir2Dfwa3uMvcUlGAz7zeX3wgHjdx4oMGnJI0cU7-tODgS-rrV2m2F7AnVndvBOmxp-ACv00I14pUSu1iNDXmHrJsn5gJu6S6RpvE8Uit69rAmo=E5F7F458"

auth = HTTPBasicAuth("cvarun07788@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "TES"
    },
    "issuetype": {
      "id": "10004"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
