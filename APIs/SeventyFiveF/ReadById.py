import APIs.SeventyFiveF.Read as SeventyFiveF
import logging

logger = logging.getLogger(__name__)

class Read_By_Id(SeventyFiveF.Read):
    def __init__(self, username, password, subscription_key, authentication_key):
        super().__init__(username, password, subscription_key, authentication_key)
        logging.debug("Entering ReadById.constructor()")

    def get_body(self, read_argument):
        """
        Formats the body text for a ReadyById query. Whitespace at the end of any line will cause errors.
        Example:

        ver:"3.0"
        id
        @12345678-1234-1234-1234-123456789012
        @12345678-1234-1234-1234-123456789012

        :return: Properly formatted string
        """
        logger.debug("Entering ReadById.get_body()")
        # NOTE:  ReadById does not use quotes around the argument, ReadyByFilter and ReadByFilterPaged do.
        read_argument = ["@" + s for s in read_argument]                # Each ID must begin with a "@"
        ids = "\n".join(read_argument)                                  # Each ID must be on a separate line
        body_text = f"ver:\"3.0\"\nid\n{ids}"                           # HULK SMASH! them together
        logger.debug(f"Body text:\n{body_text}")
        return body_text