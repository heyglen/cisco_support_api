
import click

from cisco_support_api.cisco_support_api import CiscoSupportApi
from cisco_support_api.cli.eox import eox_cli
from cisco_support_api.cli.config import config_cli
from cisco_support_api.utilities.dot_dict import DotDict


CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
    obj=DotDict({
        'api': CiscoSupportApi()
    }),
)

commands = click.Group('cisco_support_api',
                       context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
commands.add_command(eox_cli)
commands.add_command(config_cli)
