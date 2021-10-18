import requests

url = "https://simplescraper.io/api/PnVNwsptTJNMZ9kvg0qT?apikey=BmMrObKcpYmEu8078FrDy6NSxma33geO&limit=100"
response = requests.get(url)


def getAprDict():
	if(str(response.status_code) == "200"):
		print('Fetched successfully.')

		# Creates a list of dicts from the response received.
		jsonResponse = response.json()
		data = jsonResponse["data"]

		poolNames = []
		values 		=	[]	 

		for dict in data:

			value = dict['apy']
			poolName = dict['poolName']

			poolNames.append(poolName)
			values.append(value)

		apr_dict = {poolNames[i]: values[i] for i in range(len(poolNames))}
		print(apr_dict)

	else:
		print('Call Failed.')



