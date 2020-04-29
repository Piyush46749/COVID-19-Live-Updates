from flask import Flask
from flask import request 
from flask import jsonify 
from flask import render_template
import json
import requests
import folium
from folium.plugins import HeatMap
import datetime

app=Flask(__name__)

# mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# nosql_db = mongo_client["project"]
# col = nosql_db["data"]

now = datetime.datetime.now()
date_actual = now.day
date_to_send = date_actual - 1

month = now.month
year = now.year

hour_actual = now.hour
hour_to_send = hour_actual - 3

minute_actual = now.minute
minute_to_send = minute_actual - 6

second_actual = now.second
second_to_send = second_actual - 8

date = (str(date_to_send)+"/"+str(month)+"/"+str(year))
# time = (str(hour_to_send)+":"+str(minute_to_send)+":"+str(second_to_send)+" seconds")
time = "2:00 am"
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

	continent="0"
	active="0"
	tests="0"
	search_word= request.form.get('search')

	URL= "https://corona.lmao.ninja/v2/countries"
	r=requests.get(url=URL)
	data=r.json()
	# data_json=json.dumps(data)
	for each in data:
		# print(each.keys())
		# for key, values in each.items():
		# 	print(key+"-"+ str(values))
		if each["country"].lower() == search_word.lower():
			country=each["country"]
			cases=each["cases"]
			todayCases=each["todayCases"]
			deaths=each["deaths"]
			todayDeaths=each["todayDeaths"]
			recovered=each["recovered"]
			critical=each["critical"]

			continent=each["continent"]
			active=each["active"]
			tests=each["tests"]
		# 	listing=[(each.keys())]
		# 	print(listing)
			# print(critical)
		# else:
		# 	message="Luckily, "+search_word+" is not affected by Corona Virus"
			return render_template("front.html",country=country, cases=cases, todayCases=todayCases, continent=continent, active=active, tests=tests, deaths=deaths, todayDeaths=todayDeaths, recovered=recovered, critical=critical, date= date, time= time, flag=True)


		country_name=[each["country"].lower() for each in data]
		if search_word.lower() not in country_name:
			return render_template("front.html", flag=False)

	return render_template("front.html")
		# if each.get("country") != search_word:

			# print(" - ")
			# print(each.values())

		# for key, value in each.items():
		# 	print(key)


@app.route("/world_covid_map", methods=["GET"])
def world_covid_map():
	m = folium.Map(
    location=[20, 77],
    zoom_start=4,
    tiles='Stamen Terrain'
	)
	URL= "https://corona.lmao.ninja/v2/countries"
	r=requests.get(url=URL)
	data=r.json()
	# print(data)
	for each in data:
		# print(each["country"])
		# print(each["countryInfo"])
		# print(each["countryInfo"]["flag"])
		lat = each["countryInfo"]["lat"]
		lon = each["countryInfo"]["long"]
		cases = each["cases"]
		deaths = each["deaths"]
		icon = folium.features.CustomIcon(each["countryInfo"]["flag"],icon_size=(40, 30))
		tooltip = each["country"]
		folium.Marker([lat, lon], icon= icon, popup="Total Cases: "+str(cases)+"\n"+"Total Deaths: "+str(deaths), tooltip=tooltip).add_to(m)
		# folium.plugins.Heatmap([20, 77, 50], "MY_INDIA")
		# folium.Marker([latitude[], longitude[1]], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)
		# m.save("index1.html")	
	m.save("templates/world_covid_map.html")
	return render_template("world_map.html", date= date, time= time)

@app.route("/send_world_covid_map", methods=["GET"])
def send_world_covid_map():
	return render_template("world_covid_map.html")

@app.route("/covid_19_basics", methods=["GET"])
def covid_19_basics():
	return render_template("covid_19_basics.html")

@app.route("/news_information", methods=["GET"])
def news_information():
	return render_template("news_information.html")