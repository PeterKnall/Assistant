import json
import requests
import logging

logger = logging.getLogger(__name__)

class Read:
    """
    Do not use directly, use either ReadByFilter, ReadByFilterPaged, or ReadById.
    """
    def __init__(self, username, password, subscription_key, authentication_key):
        """
        Class parent constructor.
        :param username: Facilisight Username (required API privileges)
        :param password: Facilisight Password
        :param subscription_key: Subscription key from the API website
        :param authentication_key: Authentication key provided by Facilisight through the Auth class.
        """
        logging.debug("Entering Read.constructor()")
        self.username = username
        self.password = password
        self.subscription_key = subscription_key
        self.authentication_key = authentication_key
        self.url = "https://api.75f.io/haystack/read"

    def read(self, read_argument):
        """
        Sends information to 75F API using an HTTPS Post call and returns the result as JSON object.
        :return: JSON object with data from 75F API
        :exception: Returns an empty string
        """
        self.hdr = {
            'Authorization': self.authentication_key,
            'Accept': 'application/json',
            'Content-Type': 'text/zinc',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }
        data = self.get_body(read_argument) # Call to function in child class
        try:
            response = requests.post(self.url, data=data, headers=self.hdr, timeout=30)
            return json.loads(response.text)
        except Exception as e:
            logger.error(f"Exception during SeventyFiveF.Read(): {e}")
            return ""

    def get_body(self, read_argument):
        """
        Something bad has happened, you should not be here.
        :return: Empty string
        """
        logger.error("Read should not be used directly.  Use one of the 'ReadyBy' children instead.")
        return ""