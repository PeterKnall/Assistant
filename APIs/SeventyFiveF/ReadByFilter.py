import APIs.SeventyFiveF.Read as SeventyFiveF
import logging

logger = logging.getLogger(__name__)

class ReadByFilter(SeventyFiveF.Read):
    def __init__(self, username, password, subscription_key, authentication_key, read_argument):
        super().__init__(username, password, subscription_key, authentication_key)
        logging.debug("Entering ReadByFilter.constructor()")
        self.read_argument = read_argument

    def get_body(self):
        """
        Formats the body text for a ReadyByFilter query. Whitespace at the end of any line will cause errors.
        Example:

        ver:"3.0"
        filter
        "system and equip and siteRef==@12345678-1234-1234-1234-123456789012"

        :return: Properly formatted string
        """
        logger.debug("Entering ReadByFilter.get_body()")
        # NOTE:  The "id" filter does not use quotes around the argument, the "filter" filter does
        body_text =  f"ver:\"3.0\"\nfilter\n\"{self.read_argument}\""
        logger.debug(f"Body text:\n{body_text}")
        return body_text