import click

from flask_hexagonal.application.cli import templates
from flask_hexagonal.application.cli.interfaces.entities import CmdResponse
from flask_hexagonal.infrastructure.database.repositories.templates import (
    ListDBTemplateRepository,
)
from flask_hexagonal.infrastructure.memory.repositories.templates import (
    ListMemoryTemplateRepository,
)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option(
    "--source", type=click.Choice(["database", "memory"], case_sensitive=False)
)
def list_templates(source: str) -> None:
    repositories = {
        "database": ListDBTemplateRepository,
        "memory": ListMemoryTemplateRepository,
    }
    repo = repositories[source]
    result: CmdResponse = templates.cmd_list_templates(repo())
    click.echo(result.data or {})


if __name__ == "__main__":
    cli()
