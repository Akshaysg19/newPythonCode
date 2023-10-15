# import requests module 
import requests
from requests.auth import HTTPBasicAuth

# Making a get request 
response = requests.get('https://github.com/user, ',
                        auth=HTTPBasicAuth('akshay19', 'Guj@10ec006'))

# print request object 
print(response) 