import os
import random
import requests
from colorama import Fore

token = 'NzQ2NjEwNzI3Nzg3Mjk4ODc2.X0C1ig.YRgFbHMIWWYMHC8OXPnrLEvPwEQ'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
payload = {
    'status': "online",
    'custom_status': "https://github.com/Cuet1337/",
  }

r = request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
if r.status_code == 200:
  print('Success.')
if r.status_code == 402:
  print('Error, try again')
