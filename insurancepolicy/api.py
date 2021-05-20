import frappe
import xmltodict
import json
import requests


@frappe.whitelist(allow_guest=True)
def sync_daily_xml():
	url ='https://ratingqa.itcdataservices.com/Webservices/ITCRateEngineAPI/api/objectsamples/ITCRateEngineRequest?type=xml&useacord=true'
	try:
		response = requests.get(url)
		if response.status_code == 200:
			# print(response)
			response_data = response._content
			json_dict = json.dumps(xmltodict.parse(response_data))
			print(json_dict)
	except Exception as e:
		print(e)

# sync_daily_xml()