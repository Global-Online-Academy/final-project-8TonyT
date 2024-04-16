import requests
import config
fields= {'api_ key':config.api_key,'city_id':'3469'}
url = 'https://www.numbeo.com/api/'
r= requests.get(url + '/indices', params- fields)
data =r.json()
print(data)
