import os
import pandas as pd
import json
import APIs.SeventyFiveF.Auth as SeventyFiveFAuth
import APIs. SeventyFiveF.ReadByFilter as SeventyFiveFReadByFilter
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

class MPL:
    def init(self):
        pass

    def get_credentials_and_authorization_key(self):
        logging.debug("Entering startup()")
        # These values are stored in the Windows Environmental Variables so they can be accessed during runtime
        # rather than having them publicly viewable on GitHub.
        self.username = os.environ.get("75F API Username")                                   # 75F Facilisite username
        self.password = os.environ.get("75F API Password")                                   # 75F Facilisite password
        self.subscription_key = os.environ.get("75F API Subscription Key")                   # API Key from 75F API Management portal

        auth = SeventyFiveFAuth.Auth()
        self.authorization_key = auth.get_authorization_key(self.username, self.password, self.subscription_key)

    def get_site_ids(self):
        query_text = "building and equip"
        reader = SeventyFiveFReadByFilter.ReadByFilter(self.username, self.password, self.subscription_key,
                                                       self.authorization_key, query_text)

        # TODO: Should be "reader.read("building and equip")
        return reader.read()

if __name__ == "__main__":
    logging.info("*** Application starting ***")
    mpl = MPL()
    mpl.get_credentials_and_authorization_key()
    sites_json = mpl.get_site_ids()
    print(json.dumps(sites_json, indent=4, sort_keys=False))
    sites_df = pd.DataFrame(sites_json["rows"])
    sites_df.to_csv("site_df.csv", header=True, index=False)