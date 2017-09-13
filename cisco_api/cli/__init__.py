import click

from cisco_api.cisco_api import CiscoApi
from cisco_api.cli.eox import eox_cli
from cisco_api.cli.config import config_cli


CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
    obj=CiscoApi(),
)

commands = click.Group('cisco_api', context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
commands.add_command(eox_cli)
commands.add_command(config_cli)
