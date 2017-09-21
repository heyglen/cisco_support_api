

class InvalidProduct(Exception):
    error_id = 'SSA_ERR_026'


class GeneralException(Exception):
    error_id = 'SSA_GENERIC_ERR'


class InvalidStartDate(Exception):
    error_id = [
        'SSA_ERR_001',
        'SSA_ERR_016',
    ]


class SoftwareReleaseTooLong(Exception):
    error_id = 'SSA_ERR_003'


class TooManySerialNumbers(Exception):
    error_id = 'SSA_ERR_007'


class TooManyProductIds(Exception):
    error_id = 'SSA_ERR_009'


class InvalidResponseEncoding(Exception):
    error_id = 'SSA_ERR_010'


class Unavailable(Exception):
    error_id = [
        'SSA_ERR_011',
        'SSA_ERR_012',
        'SSA_ERR_014',
    ]


class ServiceProblem(Exception):
    error_id = 'SSA_ERR_013'


class ProductIdNotFound(Exception):
    error_id = 'SSA_ERR_015'


class SerialToProductIdServiceDown(Exception):
    error_id = 'SSA_ERR_018'


class ProductBulletinDoesNotExist(Exception):
    error_id = 'SSA_ERR_022'


class SerialDoesNotExist(Exception):
    error_id = 'SSA_ERR_023'


class SoftwareDoesNotExist(Exception):
    error_id = 'SSA_ERR_024'


class ProductIdDoesNotExist(Exception):
    error_id = 'SSA_ERR_026'


class InvalidPageIndex(Exception):
    error_id = 'SSA_ERR_028'


class ProductBulletinNotFound(Exception):
    error_id = 'SSA_ERR_030'


class RequestNotUtf8Compliant(Exception):
    error_id = 'SSA_ERR_031'


class InvalidProductIdWildcard(Exception):
    error_id = 'SSA_ERR_032'


class AaaServiceUnavailable(Exception):
    error_id = 'SSA_ERR_033'


class AccessDenied(Exception):
    error_id = [
        'SSA_ERR_034',
        'SSA_ERR_036',
    ]


class CepmServiceUnavailable(Exception):
    error_id = 'SSA_ERR_037'