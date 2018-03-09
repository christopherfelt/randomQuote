import requests
from pprint import pprint

r = requests.get('https://talaikis.com/api/quotes/random/')
print(r.status_code)

return_json = r.json()

author = return_json['author']
quote = return_json['quote']

print(author)
print(quote)


# pprint(r.json())

