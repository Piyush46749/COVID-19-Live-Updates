from flask import Flask
from flask import request 
from flask import jsonify 
from flask import render_template
import pymongo
import json, time
import requests

URL= "https://corona.lmao.ninja/countries"
r=requests.get(url=URL)
data=r.json()
print("bye")
# drop=[]	# data_json=json.dumps(data)
# for each in data:
name=[each["country"] for each in data]
print(name)
	# down=(each["country"])
	# drop.insert(down)
	# print(drop)

	# for key, values in each.items():
	# 	print(values["country"])