import json
import requests
import APIs.SeventyFiveF.Auth as Auth

class Read:
    def __init__(self, username, password, subscription_key):
        self.username = username
        self.password = password
        self.subscription_key = subscription_key
        self.authorization_string = Auth.get_authorization(username, password, subscription_key)
        self.url = "https://api.75f.io/haystack/read"

    def post(self):
        self.hdr = {
            'Authorization': self.authorization_string,
            'Accept': 'application/json',
            'Content-Type': 'text/zinc',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }
        data = self.get_body()
        try:
            response = requests.post(self.url, data=data, headers=self.hdr, timeout=30)
            return json.loads(response.text)
        except Exception as e:
            raise Exception(f"Exception during SeventyFiveF.Read(): {e}")

    def get_body(self):
        raise Exception("Read should not be used directly.  Use one of the 'ReadyBy' children instead.")