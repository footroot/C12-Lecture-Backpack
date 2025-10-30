import requests

response = requests.get(url="https://api.funtranslations.com/translate/yoda.json",
                        params={"text": "Obi Wan does not know what he is doing."})
print(response.json())