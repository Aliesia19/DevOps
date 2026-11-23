import click


@click.group()
def cli():
    """Утиліта для роботи з іменами."""


@cli.command()
@click.option("--name", required=True, help="Ім'я для перевірки.")
def say(name):
    """Виводить ім'я, якщо воно не починається з P."""
    if name.lower().startswith("p"):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()