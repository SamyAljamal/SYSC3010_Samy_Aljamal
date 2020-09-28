def read_data_thingspeak():
	URL = 'https://api.thingspeak.com/channels/1161382/fields/1.json?api_key=2ZAU8B7782FDAMEI&results=2'
	KEY = '2ZAU8B7782FDAMEI'
	HEADER = '&results=2'
	NEW_URL = URL + KEY + HEADER
	print(NEW_URL)

	get_data = requests.get(NEW_URL).json()
	print(get_data)
	channel_id = get_data['channel']['id']

	field_1 = get_data['feeds']
	print(field_1)

	t = []

	for x in field_1:
		print(x['field1'])
		t.append(x['field1'])
