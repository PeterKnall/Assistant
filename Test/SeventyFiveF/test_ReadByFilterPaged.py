from unittest import TestCase
import os
import pandas as pd
import APIs.SeventyFiveF.ReadByFilterPaged as Read
import APIs.SeventyFiveF.Auth as Auth

class TestRead_By_Filter_Paged(TestCase):
    def test_RedByFilterPaged(self):
        """
        This test checks that between one and three results are returned for page 1 results o a ReadByFilterPaged query.
        This test depends on:
        1) Privileges of username in Facilisight and the 75F API
        2) The id being used (while change if the current profile is changed or deleted)
        3) The site's structure has not changed (may need to verify if the test fails)
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        page_size = "3"
        page_number = "1"
        siteRef = "@4f04cf8f-9d19-4138-b376-0cd468fc5545"
        query_string = f"siteRef=={siteRef}"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = Read.ReadByFilterPaged(username, password, subscription_key, authentication_key, page_size, page_number)
        results = reader.read(query_string)
        df = pd.DataFrame(results['rows'])

        self.assertLessEqual(1, df.shape[0])
        self.assertGreaterEqual(3, df.shape[0])
