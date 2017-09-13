
import datetime

ATTRIBUTES = [
    # 'product',
    'announced',
    'failure_analysis',
    'software_maintenance',
    'security_vulnerability',
    'service_contract_renewal',
    'service_contract_attachment',
    'last_day_of_support',
    'product_bulletin_url',
    'bulletin_number',
    'product_description',
    'updated',
]


class EoxRecord:
    def __init__(self):
        self.product = None
        self.announced = None
        self.failure_analysis = None
        self.software_maintenance = None
        self.security_vulnerability = None
        self.service_contract_renewal = None
        self.service_contract_attachment = None
        self.last_day_of_support = None
        self.product_bulletin_url = None
        self.bulletin_number = None
        self.product_description = None
        self.updated = None
        self.verbose = False

    def __str__(self):
        value = self.last_day_of_support
        output = f'{self.product}'
        if self.verbose:
            for attribute in ATTRIBUTES:
                value = getattr(self, attribute)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%Y-%m-%d')
                if value:
                    output += f'\n\t{attribute} = {value}'
        else:
            value = self.last_day_of_support
            value = value.strftime('%Y-%m-%d') if value else 'n/a'
            output = f'{output} {value}'
        return output

    def __repr__(self):
        value = self.last_day_of_support
        value = value.strftime('%Y-%m-%d') if value else 'n/a'
        return f'<{self.product} {value}>'
