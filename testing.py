#!/usr/bin/env python3
"""
Do Yoda Speak

Takes text and converts it into something Yoda might say
"""

import requests

req = requests.request('GET', 'https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait.',
  headers={
      "X-Mashape-Key": "Upi6oCn4eRmshBVdnoRikxZLfAqkp17iLWzjsnisxHux3sNAnC",
      "Accept": "text/plain"
  }
)
#code so "sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait." is a seperate paramenters
print(req)

# Key: Upi6oCn4eRmshBVdnoRikxZLfAqkp17iLWzjsnisxHux3sNAnC
#
# response = unirest.get("",
#   headers={
#     "X-Mashape-Key": "Upi6oCn4eRmshBVdnoRikxZLfAqkp17iLWzjsnisxHux3sNAnC",
#     "Accept": "text/plain"
#   }
# )
