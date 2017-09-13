import click


CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
)

commands = click.Group('cisco_api', context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@commands.command()
@click.pass_context
def main(ctx):
    """Console script for cisco_api"""
    click.echo("Replace this message by putting your code into "
               "cisco_api.cli.main")

