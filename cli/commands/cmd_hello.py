import subprocess

import click


@click.command()
@click.argument('name', default="Zach")
def cli(name):
    """
    Output name parameter.
    :param name: Name string
    :return: Subprocess call result
    """
    cmd = 'echo hello {0}'.format(name)
    return subprocess.call(cmd, shell=True)