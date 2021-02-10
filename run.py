import requests
import json
import sms
from sms import send_message
import schedule
import time
from datetime import date

# def setup():
# 	global today_date, today_year, today_month, today_day, today_yesterday
# 	today_date = date.today()
# 	today_year = str(today_date.year).zfill(4)
# 	today_month = str(today_date.month).zfill(2)
# 	today_day = str(today_date.day).zfill(2)
# 	today_yesterday = str(today_date.day - 1).zfill(2)

# 	return today_date, today_year, today_month, today_day, today_yesterday

def callsApi():
	# bitcoin_api_url = "https://api.coindesk.com/v1/bpi/historical/close.json?start="+today_year+"-"+today_month+"-"+today_yesterday+"&end="+today_year+"-"+today_month+"-"+today_day+""
	# bitcoin_api_response = requests.get(bitcoin_api_url)

	btc_cotation_url = "https://economia.awesomeapi.com.br/json/all"
	all_cotations = requests.get(btc_cotation_url)

	# return bitcoin_api_response, all_cotations
	return all_cotations

def jprint(obj):
    jsonResponse = json.dumps(obj, sort_keys=True, indent=4)
    return jsonResponse

# def clearData(bitcoin_api_response, all_cotations):
def clearData(all_cotations):
	# bitcoin_cotation = jprint(bitcoin_api_response.json()["bpi"][today_year+"-"+today_month+"-"+today_day])
	btc_cotation = jprint(all_cotations.json()['BTC']['bid'])
	stripped_btc_cotation = btc_cotation.strip('"')
	bitcoin_value = round(float(stripped_btc_cotation),2)
	return bitcoin_value

def scheduleProcess(bitcoin_value):
	schedule.every(10).seconds.do(send_message, bitcoin_value)
	schedule.every().day.at("10:30").do(send_message, bitcoin_value)
	schedule.every().day.at("16:30").do(send_message, bitcoin_value)
	schedule.every().day.at("21:00").do(send_message, bitcoin_value)

def main():
	# today_date, today_year, today_month, today_day, today_yesterday = setup()
	# bitcoin_api_response, all_cotations = callsApi()
	all_cotations = callsApi()
	# finalValue = clearData(bitcoin_api_response, all_cotations)
	finalValue = clearData(all_cotations)
	scheduleProcess(finalValue)
	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == '__main__':
	main()