import os
import click
import pathlib

def create_module(path: pathlib.Path):
    path.mkdir(exist_ok=True)
    path.joinpath('__init__.py').touch(exist_ok=True)
    return path

@click.command()
@click.argument('modules')
def command(modules: str):
    modules = modules.replace('\\', '/')
    modules_arr = modules.split('/')[-1].split(',')
    path_to = pathlib.Path(os.getcwd()).joinpath(
        '/'.join(modules.split('/')[:-1])
    )
    path_to.mkdir(parents=True, exist_ok=True)
    result = [create_module(path_to.joinpath(i)) for i in modules_arr]
    click.echo(
        f'Added new modules at paths:\n' + '\n'.join(map(str,result)) 
        )

command()