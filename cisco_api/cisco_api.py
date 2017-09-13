
from cisco_api.eox import Eox

from cisco_api.utilities.log_setup import log_setup
from cisco_api.utilities.configuration import configuration


logger = log_setup('cisco_api')
logger.setLevel(configuration.log.level)


class CiscoApi:

    def __init__(self):
        self.eox = Eox()