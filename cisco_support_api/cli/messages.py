# -*- coding: utf-8 -*-

import click

from cisco_support_api.utilities.dot_dict import DotDict


messages = DotDict({
    'done': click.style('Done', fg='green', bold=True),
    'not_found': click.style('Not found', fg='yellow', bold=True),
    'no_results': click.style('No results', fg='white', bold=True),
})
