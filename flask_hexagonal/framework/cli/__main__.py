import click

from flask_hexagonal.application.cli import templates
from flask_hexagonal.infrastructure.database.repositories.templates import ListDBTemplateRepository
from flask_hexagonal.infrastructure.memory.repositories.templates import ListMemoryTemplateRepository


@click.group()
def cli():
    pass


@cli.command()
@click.option('--source', type=click.Choice(['database', 'memory'], case_sensitive=False), help='')
def list_templates(source):
    repositories = {
        'database': ListDBTemplateRepository,
        'memory': ListMemoryTemplateRepository,
    }
    repo = repositories[source]
    result = templates.cmd_list_templates(repo())
    template_list = result.data or []
    click.echo([t.dict() for t in template_list])


if __name__ == '__main__':
    cli()