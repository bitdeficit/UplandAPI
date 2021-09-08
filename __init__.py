import requests
import json
# import os

# token = os.environ['UplandToken']

level = ["Visitor","Uplander","Pro","Director","Executive","Chief Executive"]

def getPropertiesUser(user, token):
  headers={"authorization": "Bearer "+token}

  try:
    req = requests.get(f'https://api.upland.me/properties/list/{user}', headers=headers)
    req.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(e)
    return None

  prop_list = ""

  properties = json.loads(req.text)
  for prop in properties:
    prop_list+=prop['full_address']+", "+prop['city_name']+", "+prop['state_name']+"\n"

  print(properties)
  return prop_list
  

def getUserProfile(user, token):
  headers={"authorization": "Bearer "+token}
  
  try:
    req = requests.get(f'https://api.upland.me/profile/{user}', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None



def getState(id, token):
  headers={"authorization": "Bearer "+token}
  
  try:
    req = requests.get(f'https://api.upland.me/state/{id}', headers=headers)
#    req = requests.get(f'https://api.upland.me/state/{id}')
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getAllStates(token):
  headers={"authorization": "Bearer "+token}
  
  try:
    req = requests.get(f'https://api.upland.me/state', headers=headers)
#    req = requests.get('https://api.upland.me/state')
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getVisitorsByPropertyId(id, token):
  headers={"authorization": "Bearer "+token}

  try:
    req = requests.get(f' https://api.upland.me/teleports/visitors/{id}', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getPropertyById(id, token):
  headers={"authorization": "Bearer "+token}

  try:
    req = requests.get(f' https://api.upland.me/properties/{id}', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getCity(id, token):
  headers={"authorization": "Bearer "+token}
  
  try:
    req = requests.get(f'https://api.upland.me/city/{id}', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getAllCities(token):
  headers={"authorization": "Bearer "+token}
  
  try:
    req = requests.get(f'https://api.upland.me/city', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None


def getAllNeighborhoods(token):
  try:
    req = requests.get(f' https://api.upland.me/neighborhood/')
#    req = requests.get(f' https://api.up2land.com/neighborhood_deepinfo/{id}')
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None




###############################################################
#
# Up2Land API Calls
#
###############################################################

def getNeighborhoodDeepInfo(id):
  headers={"Origin": "https://up2land.com",
  "Referer": "https://up2land.com"}

  try:
    req = requests.get(f' https://api.up2land.com/neighborhood_deepinfo/{id}', headers=headers)
#    req = requests.get(f' https://api.up2land.com/neighborhood_deepinfo/{id}')
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None
    

def getPropertyByAddress(address, city_id):
  headers={"Origin": "https://up2land.com",
  "Referer": "https://up2land.com"}

  try:
    req = requests.get(f' https://api.up2land.com/bigdata/query?queryAddress={address}&city={city_id}', headers=headers)
    req.raise_for_status()
    return json.loads(req.text)
  except requests.exceptions.RequestException as e:
    print(e)
    return None
