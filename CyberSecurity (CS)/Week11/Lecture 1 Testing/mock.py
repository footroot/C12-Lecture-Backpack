from unittest.mock import MagicMock

def fetch_data(api_client):
    return api_client.get_data()

mock_api = MagicMock()
mock_api.get_data.return_value = {"status": "success", "data": [1,2,3]}

print(fetch_data(mock_api))
