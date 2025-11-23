import os
import APIs.SeventyFiveF.Auth as SeventyFiveFAuth
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

class MPL:
    def init(self):
        pass

    def startup(self):
        logging.debug("Entering startup()")
        # These values are stored in the Windows Environmental Variables so they can be accessed during runtime
        # rather than having them publicly viewable on GitHub.
        self.username = os.environ.get("75F API Username")                                   # 75F Facilisite username
        self.password = os.environ.get("75F API Password")                                   # 75F Facilisite password
        self.subscription_key = os.environ.get("75F API Subscription Key")                    # API Key from 75F API Management portal

        auth = SeventyFiveFAuth.Auth()
        self.authorization_key = auth.get_authorization_key(self.username, self.password, self.subscription_key)

if __name__ == "__main__":
    logging.info("*** Application starting ***")
    mpl = MPL()
    mpl.startup()