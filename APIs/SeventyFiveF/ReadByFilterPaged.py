import APIs.SeventyFiveF.Read as SeventyFiveF
import logging

logger = logging.getLogger(__name__)

class ReadByFilterPaged(SeventyFiveF.Read):
    def __init__(self, username, password, subscription_key, authentication_key, page_size, page_number):
        super().__init__(username, password, subscription_key, authentication_key)
        logging.debug("Entering ReadByFilterPaged.constructor()")
        self.page_size = page_size
        self.page_number = page_number

    def get_body(self, read_argument):
        """
        Formats the body text for a ReadyByFilterPaged query.  Whitespace at the end of any line will cause errors.
        Example:

        ver:"3.0" size:25 page:3
        filter
        "system and equip and siteRef==@12345678-1234-1234-1234-123456789012"

        :return: Properly formatted string
        """
        logger.debug("Entering ReadByFilterPaged.get_body()")
        # NOTE:  The "id" filter does not use quotes around the argument, the "filter" filter does
        body_text = f"ver:\"3.0\" size:{self.page_size} page:{self.page_number}\nfilter\n\"{read_argument}\""
        logger.debug(f"Body text:\n{body_text}")
        return body_text
