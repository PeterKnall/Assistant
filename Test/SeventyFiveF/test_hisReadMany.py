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
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        4) The date cannot be the current date as there haven't been 1440 trends recorded yet (current date is covered
           with the "today" date range)
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

        self.assertEqual(1440, df.shape[0])

    def test_hisReadMany_DateRange(self):
        """
        This test checks that there are 588 trends returned for a range of dates between two consecutive days.
        This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        4) The date cannot include the current date as there haven't been 588 trends recorded yet (spanning two days)

        Notes: this feature returns historical values at 5 minute intervals instead of 1 minute intervals.
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "2025-11-01T12:00:00-04:00 Detroit,2025-11-01T18:00:00-04:00 Detroit"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertEqual(588, df.shape[0])

    def test_hisReadMany_DateTimeRange(self):
        """
        This test checks that there are 588 trends returned for a range of date time objects that span two consecutive
        days.  This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        4) The date cannot include the current date as there haven't been 588 trends recorded yet (spanning two days)

        Notes: this feature returns historical values at 5 minute intervals instead of 1 minute intervals.
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "2025-11-01,2025-11-02"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertEqual(588, df.shape[0])

    def test_hisReadMany_Latest(self):
        """
        This test checks that there is 1 trend returned when looking for the latest value.  This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "latest"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertEqual(1, df.shape[0])

    def test_hisReadMany_Today(self):
        """
        This test checks that some trends are returned when looking for today's values.  This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        4) The date cannot include the current date as there haven't been 588 trends recorded yet
        5) The test is not run at midnight (some trends will need to be recorded)
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "today"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertLessEqual(1, df.shape[0])

    def test_hisReadMany_Yesterday(self):
        """
        This test checks that there are 1,440 trends returned for yesterday.  This test depends on:
        1) Privileges of username in Facilisite and the 75F API
        2) The date chosen still has trends (may need to be updated if values for these historical value have been archived)
        3) The id being used (while change if the current profile is changed or deleted)
        """
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        ids = ["52bdc021-71d3-4479-903e-0b0986a993ee"]
        date_range = "yesterday"

        authentication_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        reader = rm.hisReadMany(username, password, subscription_key, authentication_key)
        results = reader.read(ids, date_range)
        df = pd.DataFrame(results['rows'][0])

        self.assertEqual(1440, df.shape[0])

