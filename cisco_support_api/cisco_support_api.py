
from cisco_support_api.eox import Eox

from cisco_support_api.utilities.log_setup import log_setup
from cisco_support_api.utilities.configuration import configuration


logger = log_setup('cisco_support_api')
logger.setLevel(configuration.log.level)


class CiscoSupportApi:

    def __init__(self):
        self.eox = Eox()
