import requests
#suggetison , add a gui on top for the user to select the quiz categories (welcome screen )
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
#parse the data from API into the question data to match the rest of the old code from the quiz brain
question_data = data["results"]
