# -*- coding: utf-8 -*-

import functools
import logging
import sys

import click
import colorlog


FORMATTER = colorlog.ColoredFormatter(
    "%(white)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

LOG_TEXT = "%(log_color)s%(levelname)-2s%(reset)s %(name)-3s %(white)s%(message)s"

VERBOSE_FORMATTER = colorlog.ColoredFormatter(
    LOG_TEXT,
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)


def debug_option(fn):
    debug_handler = logging.StreamHandler(sys.stdout)
    debug_handler.setLevel(logging.WARNING)
    debug_handler.setFormatter(VERBOSE_FORMATTER)

    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(FORMATTER)

    module_logger = logging.getLogger(__name__.split('.')[0])
    module_logger.handlers = list()
    module_logger.addHandler(info_handler)

    cli_logger = logging.getLogger(fn.__module__)

    @click.option('-d', '--debug', is_flag=True, default=False)
    def debug_decorator(*args, **kwargs):
        debug_flag = kwargs.pop('debug')
        if debug_flag:
            for log in (module_logger, ):
                log.handlers = list()
                debug_handler.setLevel(logging.DEBUG)
                log.addHandler(debug_handler)
                log.setLevel(logging.DEBUG)

        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if debug_flag:
                cli_logger.error(str(e), exc_info=True)
                raise
            raise click.ClickException(str(e))
    return functools.update_wrapper(debug_decorator, fn)
