import requests
import re
import logging

logger = logging.getLogger(__name__)

class Auth():
    def __init__(self):
        pass

    def get_authorization_key(self, username, password, subscription_key):
        """
        Retrieves the Authorization Key using the username, password, and subscription key.  Prepends 'Bearer '
        to the Authorization Code per the 75F documentation.
        Args:
            username (string):  The Facilisight username that has API privileges
            password (string):  The password for the above username
            subscription_key (string): The subscription key for the above username from the 75F API website

        Returns:
            Authorization Key (string): The authorization code from the 75F API for use during future requests.
            Returns an empty string ("") if an Authorization Key is not returned.
        :param username: Facilisight Username (required API privileges)
        :param password: Facilisight Password
        :param subscription_key: Subscription key from the API website
        :return: (string) 855 character Authorization Key
        :exception: Returns an empty string
        """
        logging.debug("Entered SeventyFiveF.Auth.get_authorization_key()")
        url = "https://api.75f.io/oauth/token"

        hdr ={
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Cache-Control' : 'no-cache',
        'Ocp-Apim-Subscription-Key' : subscription_key
        }

        data = {
            "grant_type" : "client_credentials",
            "client_id" : username,
            "client_secret" : password
        }

        try:
            response = requests.post(url, data=data, headers=hdr, timeout=15)
        except Exception as e:
            logging.error(f"Exception while requesting Authentication Key in SeventyFiveF_Auth.get_authorization():\n{e}")
            return ""

        matches = re.findall(r'"(.*?)"', response.text)
        if matches is None:
            logging.error(f"Exception while retrieving Authentication Key from Response:  No Matches found in response.")
            return ""
        elif len(matches) < 2:
            logging.error(f"Exception while retrieving Authentication Key from Response: Only one field returned: ")
            return ""
        elif len(matches[1]) != 855:
            logging.error(f"Authorization Key is not 855 characters: {len(matches[1])}")
            return ""

        authorization_string = 'Bearer ' + matches[1]
        return authorization_string