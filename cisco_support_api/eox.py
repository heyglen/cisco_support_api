# https://developer.cisco.com/site/support-apis/docs/#eox

import logging
import datetime

from cisco_support_api.factories.eox import EoxFactory
from cisco_support_api.base_api import BaseApi
from cisco_support_api.utilities.configuration import configuration
from cisco_support_api.utilities.dot_dict import DotDict

logger = logging.getLogger(__name__)


EOX_TYPES = DotDict({
    'announce': 'EO_EXT_ANNOUNCE_DATE',
    'sale': 'EO_SALES_DATE',
    'failure_analysis': 'EO_FAIL_ANALYSIS_DATE',
    'service_attachment': 'EO_SVC_ATTACH_DATE',
    'software_maintenance': 'EO_SW_MAINTENANCE_DATE',
    'security_vulnerability': 'EO_SECURITY_VUL_SUPPORT_DATE',
    'contract_renewal': 'EO_CONTRACT_RENEW_DATE',
    'last_support': 'EO_LAST_SUPPORT_DATE',
    'update_timestamp': 'UPDATE_TIMESTAMP (default)',
})


class Eox(BaseApi):
    """
        https://developer.cisco.com/site/support-apis/docs/#eox/SWReleaseStringType
    """
    _username = configuration.eox.username
    _password = configuration.eox.password

    _base_url = 'https://api.cisco.com/supporttools/eox/rest/5'
    _request_type = {
        'date': 'EOXByDates',
        'product': 'EOXByProductID',
        'serial': 'EOXBySerialNumber',
        'software': 'EOXBySWReleaseString',
    }
    _base_params = {
        'responseencoding': 'json',
    }
    # https://developer.cisco.com/site/support-apis/docs/#eox/SWReleaseStringType
    _os_types = [
        'ACNS',
        'ACSW',
        'ALTIGAOS',
        'ASA',
        'ASYNCOS',
        'CATOS',
        'CDS-IS',
        'CDS-TV',
        'CDS-VN',
        'CDS-VQE',
        'CTS',
        'ECDS',
        'FWSM-OS',
        'GSS',
        'IOS',
        'IOS XR',
        'IOS-XE',
        'IPS',
        'NAM',
        'NX-OS',
        'ONS',
        'PIXOS',
        'SAN-OS',
        'STAR OS',
        'TC',
        'TE',
        'UCS NX-OS',
        'VCS',
        'VDS-IS',
        'WAAS',
        'WANSW BPX/IGX/IPX',
        'WEBNS',
        'WLC',
        'WLSE-OS',
        'XC',
    ]

    def _url_page_index(self, request_type):
        base_url = self._base_url
        request_type = self._request_type[request_type]
        base_url = f'{base_url}/{request_type}'
        for page_index in range(1, 15):
            yield f'{base_url}/{page_index}'

    def _date_urls(self, start_date, end_date):
        for page_index_url in self._url_page_index('date'):
            url = f'{page_index_url}/{start_date}/{end_date}'
            url = f'{url}'
            yield url

    def _product_urls(self, product_id):
        for page_index_url in self._url_page_index('product'):
            url = f'{page_index_url}/{product_id}'
            url = f'{url}'
            yield url

    def _serial_urls(self, serial):
        for page_index_url in self._url_page_index('serial'):
            url = f'{page_index_url}/{serial}'
            url = f'{url}'
            yield url

    def _get_records(self, response):
        for record in EoxFactory.build(response):
            yield record

    def _new_page(self, response):
        current_page = response.PaginationResponseRecord.PageIndex
        last_page = response.PaginationResponseRecord.LastIndex
        return current_page != last_page

    async def by_date(self, start_date, end_date):
        records = list()
        for unvalidated_date in [start_date, end_date]:
            datetime.datetime.strptime(unvalidated_date, '%Y-%m-%d')
        for date_url in self._date_urls(start_date, end_date):
            responses = await self._get(
                date_url,
                # params={
                #     'eoxAttrib': EOX_TYPES.sale
                # },
            )
            for eox in self._get_records(responses):
                records.append(eox)
            if not self._new_page(responses):
                break
        return records

    async def by_product(self, product_id):
        records = list()
        for product_url in self._product_urls(product_id):
            responses = await self._get(
                product_url,
                # params={
                #     'eoxAttrib': EOX_TYPES.sale
                # },
            )

            for eox in self._get_records(responses):
                records.append(eox)

            if not self._new_page(responses):
                break
        return records

    async def by_serial(self, serial):
        records = list()
        for serial_url in self._serial_urls(serial):
            responses = await self._get(
                serial_url,
                # params={
                #     'eoxAttrib': EOX_TYPES.sale
                # },
            )

            for eox in self._get_records(responses):
                records.append(eox)

            if not self._new_page(responses):
                break
        return records

    async def list(self):
        now = datetime.datetime.now()
        last_week = now - datetime.timedelta(weeks=1)

        start_date = last_week.strftime('%Y-%m-%d')
        end_date = now.strftime('%Y-%m-%d')
        records = list()
        async for eox in self.by_date(start_date, end_date):
            records.append(eox)
        return records
