# Read
# This API provides operations for reading and writing operational data to writable points as well as historizing
# data for any point type.

# Read by id: ver:"3.0" id @6d78f1c0-d10a-4482-8058-db328441a669 @84010772-46ec-4937-9430-71083196f2c4

import APIs.SeventyFiveF.Read as SeventyFiveF
import logging

logger = logging.getLogger(__name__)

class Read_By_Id(SeventyFiveF.Read):
    def __init__(self, username, password, subscription_key, authentication_key, read_argument):
        super().__init__(username, password, subscription_key, authentication_key)
        logging.debug("Entering ReadById.constructor()")
        self.read_argument = read_argument

    def get_body(self):
        logger.debug("Entering ReadById.get_body()")
        # NOTE:  The "id" filter does not use quotes around the argument, the "filter" filter does
        ids = "\n".join(self.read_argument)
        body_text = f"ver:\"3.0\"\nid\n{ids}"
        logger.debug(f"Body text:\n{body_text}")
        return body_text