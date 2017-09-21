
import datetime
import logging

import click

from cisco_support_api.cli.messages import messages
from cisco_support_api.utilities.cli_debug import debug_option
from cisco_support_api.cli.aio_loop_decorator import aio_loop

logger = logging.getLogger(__name__)

eox_cli = click.Group('eox')


@eox_cli.command('list')
@click.pass_context
@click.option('-v', '--verbose', is_flag=True, default=False)
@aio_loop
@debug_option
def list_(ctx, verbose, loop):
    """List EOX from the past week"""
    items = loop.run_until_complete(ctx.obj.api.eox.list())
    if not items:
        logger.info(messages.no_results)
    # now = datetime.datetime.now()
    # for item in sorted(items, key=lambda x: x.last_day_of_support or now):
    for item in items:
        item.verbose = verbose
        logger.info(item)


@eox_cli.command()
@click.pass_context
@click.argument('product')
@click.option('-v', '--verbose', is_flag=True, default=False)
@aio_loop
@debug_option
def by_product(ctx, product, verbose, loop):
    """List EOX by product id"""
    items = loop.run_until_complete(
        ctx.obj.api.eox.by_product(product)
    )
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
@aio_loop
@debug_option
def by_serial(ctx, serial, verbose, loop):
    """List EOX by serial"""
    items = loop.run_until_complete(
        ctx.obj.api.eox.by_serial(serial)
    )
    if not items:
        logger.info(messages.no_results)
    now = datetime.datetime.now()
    for item in sorted(items, key=lambda x: x.last_day_of_support or now):
        item.verbose = verbose
        logger.info(item)
