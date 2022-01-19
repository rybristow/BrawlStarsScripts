import requests
import json
import csv
import os
from brawler import Brawler

my_headers = {'Accept' : 'application/json', 'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg0NzNlZWZhLTcxMDMtNDBmNC04MjdmLWM4MGQwZWQ2YTE5NyIsImlhdCI6MTY0MTQ4Nzc4Mywic3ViIjoiZGV2ZWxvcGVyLzA4MTgyYTk4LTkyNDQtNDdjYS00NjVmLTNkODRhMWY5Njg3OSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTA4Ljc2LjE2Ny4xOTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.M0pgEAhK3saHOBahO5Xu6-W5XbcnwC9E6Ke9lOsExY1-S5XFDy3sZL7-nRN_orzVErjXpQX25BJT0ZzDUCTp5w'}
response = requests.get('https://api.brawlstars.com/v1/players/%23Q092CLL8', headers=my_headers)
file="brawlerStats.csv"

jsonResponse = response.json()

player_data = json.loads(response.text)

brawlers = []

for character in player_data["brawlers"]:
	new_brawler = Brawler(character["name"], character["trophies"])
	brawlers.append(new_brawler)

brawlers.sort(key=lambda x: x.trophies, reverse=True)

if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)

with open(file, 'w') as csvfile:
	datawriter = csv.writer(csvfile)
	datawriter.writerow(["Name","Trophies"])
	for brawler in brawlers:
		datawriter.writerow([brawler.name, brawler.trophies])
