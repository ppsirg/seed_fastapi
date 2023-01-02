"""
add_module: add domain module
add_endpoint: add endpoint given json scheme
build: compile poetry to requirements.txt, build docker
"""
import click

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
@click.option('--file')
def entity(name, file):
    print(name, file)

@main.command()
@click.argument('schema')
def auth(schema):
    # TODO: JWT, OAuth2
    print(schema)

@main.command()
@click.argument('schema')
def database(schema):
    # TODO: textplain, mongo, peewee (sqlite, postgresql, mariadb)
    print(schema)

@main.command()
def build():
    print("build in container")


if __name__ == '__main__':
    main()
