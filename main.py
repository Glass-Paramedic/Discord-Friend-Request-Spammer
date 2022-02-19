import requests

with open("t.txt", "r") as myfile:
  for line in myfile:
    try:
      tokey = (line.rstrip('\n'))
      print(tokey)
      headers = {
      'authority': 'discord.com',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
      'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk4LjAuNDc1OC4xMDIgU2FmYXJpLzUzNy4zNiBFZGcvOTguMC4xMTA4LjU1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTguMC40NzU4LjEwMiIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbSIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZV9jdXJyZW50IjoiZ29vZ2xlIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTE1NjMzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
      'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==',
      'x-debug-options': 'bugReporterEnabled',
      'sec-ch-ua-mobile': '?0',
      'authorization': tokey,
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
      'x-discord-locale': 'en-US',
      'dnt': '1',
      'sec-ch-ua-platform': '"Windows"',
      'accept': '*/*',
      'origin': 'https://discord.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://discord.com/channels/@me',
      'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
      }

      json_data = {
          'username': 'Deltara',
          'discriminator': 4947,
      }

      response = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers, json=json_data)
      print(response.text)
    except Exception as e:
      print(e)
          
        
