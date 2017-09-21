
import datetime
import contextlib
import logging

import click

from cisco_support_api.cli.messages import messages
from cisco_support_api.utilities.cli_debug import debug_option

logger = logging.getLogger(__name__)

eox_cli = click.Group('eox')


@eox_cli.command('list')
@click.pass_context
@click.option('-v', '--verbose', is_flag=True, default=False)
@debug_option
def list_(ctx, verbose):
    """List EOX from the past week"""
    items = ctx.obj.eox.list()
    if not items:
        logger.info(messages.no_results)
    now = datetime.datetime.now()
    for item in sorted(items, key=lambda x: x.last_day_of_support or now):
        item.verbose = verbose
        logger.info(item)

@eox_cli.command()
@click.pass_context
@click.argument('product')
@click.option('-v', '--verbose', is_flag=True, default=False)
@debug_option
def by_product(ctx, product, verbose):
    """List EOX by product id"""
    items = ctx.obj.eox.by_product(product)
    if not items:
        logger.info(messages.no_results)
    now = datetime.datetime.now()
    for item in sorted(items, key=lambda x: x.last_day_of_support or now):
        item.verbose = verbose
        logger.info(item)

@eox_cli.command()
@click.pass_context
@click.argument('serial')
@click.option('-v', '--verbose', is_flag=True, default=False)
@debug_option
def by_serial(ctx, serial, verbose):
    """List EOX by serial"""
    items = ctx.obj.eox.by_serial(serial)
    if not items:
        logger.info(messages.no_results)
    now = datetime.datetime.now()
    for item in sorted(items, key=lambda x: x.last_day_of_support or now):
        item.verbose = verbose
        logger.info(item)

