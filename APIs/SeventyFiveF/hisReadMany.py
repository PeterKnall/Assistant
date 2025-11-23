import requests
import json
import logging

logger = logging.getLogger(__name__)

class hisReadMany:
    """
    Retrieves historical data from the 75F API using "POST hisReadMany".  It is up to the caller to format the ids
    and date range correctly:

    Examples of Data format (Note: "id" and the subsequent list of ids must be on their own line with no extra whitespace).
        date-time range: ver:"3.0" range:"2020-01-01T12:00:00-04:00 New_York,2020-01-03T00:00:00-04:00 New_York" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418
        date range: ver:"3.0" range:"2020-01-01,2020-01-07" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418
        date: ver:"3.0" range:"2020-01-01" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418
        latest: ver:"3.0" range:"latest" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418
        today: ver:"3.0" range:"today" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418
        yesterday: ver:"3.0" range:"yesterday" id @d7180b62-f926-4d22-812f-ed18b5c91937 @e8791f69-167c-47a2-8f9e-f25dd899b418

    Args:
        username (string):  The Facilisight username that has API privileges
        password (string):  The password for the above username
        subscription_key (string): The subscription key for the above username from the 75F API website
        ids (list): A list of ids to retrieve historical data for (see README.md)
        date_range (string): The date range to pull historical data for

    Returns:
        results (dict):
    """

    def __init__(self, username, password, subscription_key, authentication_key, ids, date_range):
        self.username = username
        self.password = password
        self.subscription_key = subscription_key
        self.authentication_key = authentication_key
        self.ids = ids
        self.date_range = date_range

    def read(self):
        """
        Reads historical data from the 75F API.
        :return: JSON object with historical data.
        :exception: Returns an empty string
        """
        logger.debug("Entering hisReadMany.read()")
        url = "https://api.75f.io/haystack/hisReadMany"
        hdr ={
            'Authorization': self.authentication_key,
            'Accept': 'application/json',
            'Content-Type': 'text/zinc',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }
        # The list sent to the 75F API (ids) must consist of one id on each line without any leading or trailing spaces.
        self.ids = ["@" + s for s in self.ids]                              # Each ID must begin with a "@"
        items = '\n'.join(self.ids)                                         # Each ID must be on a separate line
        data = f"ver:\"3.0\" range:\"{self.date_range}\"\nid\n{items}"      # Combine into body text
        logger.debug(f"Retrieving data for:\n{data}")
        try:
            response = requests.post(url, data=data, headers=hdr, timeout=30)
            return json.loads(response.text)
        except Exception as e:
            logger.error(f"Exception during SeventyFiveF.hisReadMany.post(): {e}")
            return ""