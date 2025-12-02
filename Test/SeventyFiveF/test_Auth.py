from unittest import TestCase
import os
import APIs.SeventyFiveF.Auth as Auth
import re

class TestAuth(TestCase):

    def test_get_authorization_key_pattern(self):
        """
        Verify the test pattern works with a random authorization key.
        """
        # JWT: JSON Web Token
        test_pattern = "Bearer abcdefghijklmnopqrstuvwxyz1234567890.abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefg.abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890"
        pattern = r"Bearer\s[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
        m = re.findall(pattern, test_pattern)

        self.assertEqual(len(m),1)

    def test_get_authorization_key(self):
        """
        Verify Auth().get_authorization_key() returns a valid JWT.
        :return:
        """
        pattern = r"Bearer\s[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
        username = os.environ.get("75F API Username")
        password = os.environ.get("75F API Password")
        subscription_key = os.environ.get("75F API Subscription Key")
        authorization_key = Auth.Auth().get_authorization_key(username, password, subscription_key)
        m = re.findall(pattern, authorization_key)

        self.assertEqual(len(m),1)
