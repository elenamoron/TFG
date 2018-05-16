import requests
import json

json_data=open('id_profesional.json').read()
data = json.loads(json_data)
def chunks(l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]

for chunk in data:
	chunk['id'] = str(chunk['id'])


clinic_chunks = list(chunks(data, 100))

headers = {
            'Authorization': 'Token 1bc97d9099777fdbc04e20b18613818c1c6634eb',
            'Content-Type': 'application/json'
        }

for chunk in clinic_chunks:
	print ("Delete 100 profesionales")
	response = requests.delete('https://eu1-api.doofinder.com/v1/b35222395c73e5b543e8a8b6bd5f207c/items/profesionales', data=json.dumps(chunk), headers=headers)
