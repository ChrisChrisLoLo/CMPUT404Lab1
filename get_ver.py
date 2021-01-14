import requests

# Print version
# print(requests.__version__)

# Print request from google
# r = requests.get('https://www.google.com')
# print(r)

# Get this exact code from github
r = requests.get('https://raw.githubusercontent.com/ChrisChrisLoLo/CMPUT404Lab1/main/get_ver.py')
print(r.text)