#!/usr/bin/env python3

import click
import importlib.util
import sys
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)


def load_client_module(protocol):
    """Dynamically load the client module for the given protocol."""
    base_dir = Path(__file__).parent
    module_path = base_dir / f"{protocol}_client.py"

    if not module_path.exists():
        click.echo(f"❌ Error: {protocol}_client.py not found at {module_path}")
        sys.exit(1)

    try:
        spec = importlib.util.spec_from_file_location(f"{protocol}_client", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        click.echo(f"❌ Failed to load {protocol}_client: {e}")
        sys.exit(1)


@click.group()
@click.version_option()
def cli():
    """Agent CLI Chat Client — Interact with chat agents using multiple protocols."""
    pass


@cli.command()
@click.option('--host', '-h', default=None, help='Host/IP of the ACP agent')
@click.option('--port', '-p', default=None, type=int, help='Port to connect to')
@click.option('--token', '-t', default=None, help='Authentication token')
@click.option('--debug', is_flag=True, help='Enable debug logging')
def acp(host, port, token, debug):
    """Run ACP protocol client."""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
    click.echo("🚀 Launching ACP client...")
    client_module = load_client_module("acp")
    import asyncio
    asyncio.run(client_module.main(host=host, port=port, token=token))


@cli.command()
@click.option('--host', '-h', default=None, help='Host/IP of the A2A agent')
@click.option('--port', '-p', default=None, type=int, help='Port to connect to')
@click.option('--token', '-t', default=None, help='Authentication token')
@click.option('--debug', is_flag=True, help='Enable debug logging')
def a2a(host, port, token, debug):
    """Run A2A protocol client."""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
    click.echo("🚀 Launching A2A client...")
    client_module = load_client_module("a2a")
    client_module.main(host=host, port=port, token=token)


if __name__ == '__main__':
    cli()
