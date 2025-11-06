# Instructions are at https://python.datalumina.com
#

import requests

response = requests.get("https://api.github.com")
print(response.status_code)