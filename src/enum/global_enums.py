from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected, check the file "FailedPages.txt"'
    WRONG_URL = 'The link does not match the address bar, check the file "FailedUrls.txt"'
    HEADER_IS_MISSING = 'The "header" element is not on the page'
    FOOTER_IS_MISSING = 'The "footer" element is not on the page'
