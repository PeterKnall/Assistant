from unittest import TestCase
import os

import pandas as pd

import APIs.SeventyFiveF.ReadByFilter as Read
import APIs.SeventyFiveF.Auth as Auth

class TestReadByFilter(TestCase):
    def test_RedByFilter(self):
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

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = Read.ReadByFilter(username, password, subscription_key, authentication_key)
        query_string = "building and equip and siteRef==@4f04cf8f-9d19-4138-b376-0cd468fc5545"
        results = reader.read(query_string)
        df = pd.DataFrame(results['rows'])

        self.assertEqual(1, df.shape[0])
