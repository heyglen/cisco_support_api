
from cisco_api.utilities.exceptions import InvalidProduct

EOX_EXCEPTIONS = [
    InvalidProduct,
]

class EoxErrorFactory:

    @classmethod
    def build(cls, response):
        if 'EOXRecord' in response:
            record = response.EOXRecord[0]
            if 'EOXError' not in record:
                return
            description = record['EOXError']['ErrorDescription']
            error_id = record['EOXError']['ErrorID']
            for eox_exception in EOX_EXCEPTIONS:
                if error_id == eox_exception.error_id:
                    raise eox_exception(description)