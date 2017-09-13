
import datetime

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

    def __str__(self):
        value = self.last_day_of_support
        value = value.strftime('%Y-%m-%d') if value else 'n/a'
        return f'{self.product} {value}'

    def __repr__(self):
        value = self.last_day_of_support
        value = value.strftime('%Y-%m-%d') if value else 'n/a'
        return f'<{self.product} {value}>'
