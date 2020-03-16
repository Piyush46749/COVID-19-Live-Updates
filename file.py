from flask import Flask
from flask import request 
from flask import jsonify 
from flask import render_template
import json
import requests

app=Flask(__name__)

# mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# nosql_db = mongo_client["project"]
# col = nosql_db["data"]

@app.route("/", methods=["GET"])
def home():
	return render_template("front.html")

@app.route("/", methods=["POST"])
def search():
	country="0"
	cases="0"
	todayCases="0"
	deaths="0"
	todayDeaths="0"
	recovered="0"
	critical="0"
	# message="0"
	search_word= request.form.get('search')

	URL= "https://corona.lmao.ninja/countries"
	r=requests.get(url=URL)
	data=r.json()
	# data_json=json.dumps(data)
	for each in data:
		# print(each.keys())
		# for key, values in each.items():
		# 	print(key+"-"+ str(values))
		if each.get("country") == search_word:
			country=each["country"]
			cases=each["cases"]
			todayCases=each["todayCases"]
			deaths=each["deaths"]
			todayDeaths=each["todayDeaths"]
			recovered=each["recovered"]
			critical=each["critical"]
		# 	listing=[(each.keys())]
		# 	print(listing)
			# print(critical)
		# else:
		# 	message="Luckily, "+search_word+" is not affected by Corona Virus"
			return render_template("front.html",country=country, cases=cases, todayCases=todayCases, deaths=deaths, todayDeaths=todayDeaths, recovered=recovered, critical=critical)


		country_name=[each["country"] for each in data]
		if search_word not in country_name:
			return render_template("front.html", message="Please check the country's name. Note: First letter of the country's name must be capital")

	return render_template("front.html")
		# if each.get("country") != search_word:

			# print(" - ")
			# print(each.values())

		# for key, value in each.items():
		# 	print(key)