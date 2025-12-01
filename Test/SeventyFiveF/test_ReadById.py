from unittest import TestCase
import os
import pandas as pd
import APIs.SeventyFiveF.ReadById as Read
import APIs.SeventyFiveF.Auth as Auth

class TestRead_By_Id(TestCase):
    def test_RedById(self):
        """
        This test checks that there are a single row is returned when looking for building equipment at the test site.
        This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The id being used (while change if the current profile is changed or deleted)
        3) The site's structure has not changed (may need to verify if the test fails)
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        this_id = ["52bdc021-71d3-4479-903e-0b0986a993ee"]

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = Read.ReadById(username, password, subscription_key, authentication_key)
        results = reader.read(this_id)
        df = pd.DataFrame(results['rows'])

        self.assertEqual(1, df.shape[0])
