
import logging
import pathlib

import click
import yaml

from cisco_support_api.utilities.cli_debug import debug_option
from cisco_support_api.utilities.configuration import (configuration_directory,
                                               configuration_path,
                                               default_configuration)
logger = logging.getLogger(__name__)

config_cli = click.Group('config')


@config_cli.command()
@debug_option
def edit():
    if not configuration_path.is_file():
        if not configuration_directory.is_dir():
            configuration_directory.mkdir(parents=True)
        configuration_path.touch()
        text = yaml.dump(default_configuration, default_flow_style=False)
        configuration_path.write_text(text)
        logger.debug(f'Configuration file created in {configuration_path}')
    click.edit(filename=str(configuration_path))
