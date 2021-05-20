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
			ipt_name = create_insurance_policy_template(json_dict)
			return ipt_name
	except Exception as e:
		print(e)

@frappe.whitelist(allow_guest=True)
def create_insurance_policy_template(json_dict):
	if json_dict:
		try:
			ipt_doc = frappe.new_doc("Insurance Policy Template")
			ipt_doc.data = json_dict
			ipt_doc.save()
			frappe.db.commit()
			return ipt_doc.name
		except Exception as e:
			print(e)