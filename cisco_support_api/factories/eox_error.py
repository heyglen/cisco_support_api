
from cisco_support_api.utilities.exceptions import (InvalidProduct,
                                            GeneralException,
                                            InvalidStartDate,
                                            SoftwareReleaseTooLong,
                                            TooManySerialNumbers,
                                            TooManyProductIds,
                                            InvalidResponseEncoding,
                                            Unavailable,
                                            ServiceProblem,
                                            ProductIdNotFound,
                                            SerialToProductIdServiceDown,
                                            ProductBulletinDoesNotExist,
                                            SerialDoesNotExist,
                                            SoftwareDoesNotExist,
                                            ProductIdDoesNotExist,
                                            InvalidPageIndex,
                                            ProductBulletinNotFound,
                                            RequestNotUtf8Compliant,
                                            InvalidProductIdWildcard,
                                            AaaServiceUnavailable,
                                            AccessDenied,
                                            CepmServiceUnavailable)

EOX_EXCEPTIONS = [
    InvalidProduct,
    GeneralException,
    InvalidStartDate,
    SoftwareReleaseTooLong,
    TooManySerialNumbers,
    TooManyProductIds,
    InvalidResponseEncoding,
    Unavailable,
    ServiceProblem,
    ProductIdNotFound,
    SerialToProductIdServiceDown,
    ProductBulletinDoesNotExist,
    SerialDoesNotExist,
    SoftwareDoesNotExist,
    ProductIdDoesNotExist,
    InvalidPageIndex,
    ProductBulletinNotFound,
    RequestNotUtf8Compliant,
    InvalidProductIdWildcard,
    AaaServiceUnavailable,
    AccessDenied,
    CepmServiceUnavailable,
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
                error_ids = eox_exception.error_id
                if not isinstance(eox_exception.error_id, list):
                    error_ids = [eox_exception.error_id]
                if error_id in error_ids:
                    raise eox_exception(description)
