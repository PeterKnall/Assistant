# Read
# This API provides operations for reading and writing operational data to writable points as well as historizing
# data for any point type.

# Read by filter (paged): ver:"3.0" size:25 page:3 filter "system and equip and siteRef==@b8a1a5be-3080-40e6-9161-64f39944db9e"

import APIs.SeventyFiveF.Read as SeventyFiveF
import logging

logger = logging.getLogger(__name__)

class Read_By_Filter_Paged(SeventyFiveF.Read):
    def __init__(self, username, password, subscription_key, authentication_key, read_argument, page_size, page_number):
        super().__init__(username, password, subscription_key, authentication_key)
        logging.debug("Entering ReadByFilterPaged.constructor()")
        self.read_argument = read_argument
        self.page_size = page_size
        self.page_number = page_number

    def get_body(self):
        """
        Formats the body text for a ReadyByFilterPaged query.  Whitespace at the end of any line will cause errors.
        Example:

        ver:"3.0" size:25 page:3
        filter
        "system and equip and siteRef==@b8a1a5be-3080-40e6-9161-64f39944db9e"

        :return: Properly formatted string
        """
        logger.debug("Entering ReadByFilterPaged.get_body()")
        # NOTE:  The "id" filter does not use quotes around the argument, the "filter" filter does
        body_text = f"ver:\"3.0\" size:{self.page_size} page:{self.page_number}\nfilter\n\"{self.read_argument}\""
        logger.debug(f"Body text:\n{body_text}")
        return body_text
