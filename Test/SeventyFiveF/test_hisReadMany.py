from unittest import TestCase
import os
import APIs.SeventyFiveF.hisReadMany as rm
import APIs.SeventyFiveF.Auth as Auth
import pandas as pd

class Test_hisReadMany_date(TestCase):
    def test_hisReadMany_Date(self):
        """
        This test checks that there are 1,440 trends returned for a "date" date range.  This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived
        3) The id being used (while change if the current profile is changed or deleted)
        4) The date cannot be the current date as there haven't been 1440 trends recorded yet
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "2025-11-01"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertEqual(df.shape[0], 1440)     # There are

