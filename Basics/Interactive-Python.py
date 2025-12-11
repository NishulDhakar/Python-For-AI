#pip install ipykernel

#Jupyter > Interactive Window > Text Editor: Execute Selection

#click shift + enter to execute

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200