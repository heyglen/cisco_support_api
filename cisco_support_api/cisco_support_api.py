
from cisco_support_api.eox.eox import Eox
from cisco_support_api.eox.async_eox import AsyncEox

from cisco_support_api.utilities.log_setup import log_setup
from cisco_support_api.utilities.configuration import configuration


logger = log_setup('cisco_support_api')
logger.setLevel(configuration.log.level)


class CiscoSupportApi:

    def __init__(self, async=False):
        if async:
            self.eox = AsyncEox()
        else:
            self.eox = Eox()