import os
import pandas as pd
import APIs.SeventyFiveF.Auth as SeventyFiveFAuth
import APIs. SeventyFiveF.ReadByFilter as SeventyFiveFReadByFilter
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

class API:
    def __init__(self):
        logging.debug("Entering MPL.__init__()")
        self.subscription_key = os.environ.get("75F API Subscription Key")
        self.username = os.environ.get("75F API Username")
        self.password = os.environ.get("75F API Password")
        self.authorization_key = self.get_credentials_and_authorization_key()
        self.reader = SeventyFiveFReadByFilter.ReadByFilter(self.username, self.password, self.subscription_key, self.authorization_key)

    def get_credentials_and_authorization_key(self):
        logging.debug("Entering MPL.get_credentials_and_authorization_key()")
        auth = SeventyFiveFAuth.Auth()
        return auth.get_authorization_key(self.username, self.password, self.subscription_key)

    def query(self, query_text):
        logging.debug("Entering MPL.query()")
        return self.reader.read(query_text)

def get_site_id_and_display_name_lists(api):
    logging.debug("Entering get_site_id_and_display_name_lists()")
    response = api.query("building and equip")
    df = pd.DataFrame(response["rows"])
    df.to_csv("site_df.csv", header=True, index=False)
    site_id_list = [s[2:] for s in df["siteRef"].tolist()]
    display_name_list = [s.replace("-buildingEquip","") for s in df["dis"].tolist()]
    logging.debug(f"site_id_list: {site_id_list}")
    logging.debug(f"display_name_list: {display_name_list}")
    return site_id_list, display_name_list

def get_all_equip_from_site_list(api, site_id, display_name):
    logging.debug("Entering get_all_site_ids_df()")
    os.makedirs("equip_df", exist_ok=True)
    response = api.query(f"siteRef==@{site_id} and space and temp and not ti and not cm")
    df = pd.DataFrame(response["rows"])
    df.insert(0, "site_display_name", display_name)
    df.insert(1, "equipment", [s for s in df.get('dis',[])])
    df.insert(2, "site_id", site_id)
    df.insert(3, "equip_id", [s[2:] for s in df.get('equipRef', [])])
    df.to_csv(f"equip_df\\{display_name} equip_df.csv", header=True, index=False)
    return df

def clear_app_log():
    with open("app.log", "w") as f:
        f.write("")

if __name__ == "__main__":
    clear_app_log()
    logging.info("*** Application starting ***")
    api = API()
    # """
    site_id_list, display_name_list = get_site_id_and_display_name_lists(api)
    counter = 0
    all_equip = pd.DataFrame()
    for site_id, display_name in zip(site_id_list, display_name_list):
        counter += 1
        print(f"Processing: {counter} {display_name} {site_id}")
        logging.debug(f"Processing: {counter} {display_name} : {site_id}")
        df = get_all_equip_from_site_list(api, site_id, display_name)
        all_equip = pd.concat([all_equip, df], ignore_index=True)
    # """
    # all_equip = pd.DataFrame(api.query("equip")["rows"])
    all_equip.drop(all_equip.columns[4:], axis=1, inplace=True)
    all_equip.to_csv("all_equip.csv", header=True, index=False)

