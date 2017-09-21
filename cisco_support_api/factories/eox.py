
import logging
import datetime

from cisco_support_api.records.eox import EoxRecord
from cisco_support_api.factories.eox_error import EoxErrorFactory
from cisco_support_api.factories.eox_migration import EoxMigrationFactory


logger = logging.getLogger(__name__)

deafult_clean = lambda x: x.strip() if isinstance(x, str) else None


attribute_map = {
    'EOLProductID': 'product',
    'EOXExternalAnnouncementDate': 'announced',
    'EndOfRoutineFailureAnalysisDate': 'failure_analysis',
    'EndOfSWMaintenanceReleases': 'software_maintenance',
    'EndOfSecurityVulSupportDate': 'security_vulnerability',
    'EndOfServiceContractRenewal': 'service_contract_renewal',
    'EndOfSvcAttachDate': 'service_contract_attachment',
    'LastDateOfSupport': 'last_day_of_support',
    'LinkToProductBulletinURL': 'product_bulletin_url',
    'ProductBulletinNumber': 'bulletin_number',
    'ProductIDDescription': 'product_description',
    'UpdatedTimeStamp': 'updated',
}


date_format_map = {
    'YYYY': '%Y',
    'MM': '%m',
    'DD': '%d',
}


def parse_date_record(record):
    date_format = record['dateFormat']
    for key, value in date_format_map.items():
        date_format = date_format.replace(key, value)
    value = record['value'].strip() or None
    if value:
        value = datetime.datetime.strptime(value, date_format)
    return value


attribute_type_map = {
    'EOXMigrationDetails': EoxMigrationFactory.build,
    'EOXExternalAnnouncementDate': parse_date_record,
    'EndOfRoutineFailureAnalysisDate': parse_date_record,
    'EndOfSWMaintenanceReleases': parse_date_record,
    'EndOfSecurityVulSupportDate': parse_date_record,
    'EndOfServiceContractRenewal': parse_date_record,
    'EndOfSvcAttachDate': parse_date_record,
    'LastDateOfSupport': parse_date_record,
    'UpdatedTimeStamp': parse_date_record,
}


class EoxFactory:

    @classmethod
    def build(cls, response):
        for record in response.EOXRecord:
            EoxErrorFactory.build(response)
            eox = EoxRecord()
            for key, attribute in attribute_map.items():
                value = record[key]
                if key in attribute_type_map:
                    value = attribute_type_map[key](value)
                else:
                    value = deafult_clean(value)
                setattr(eox, attribute, value)
            yield eox
