# coding:utf-8

import logging, click
import build_page

FORMAT = '%(asctime)-7s [%(name)-6s] [%(levelname)-5s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%H:%M:%S")

log = logging.getLogger("main")



@click.group()
def cli():
    pass

@cli.command()
@click.option('-c', '--config', default="config.yaml", help='config.yaml', type=click.Path(exists=True))
def build(config):
    build_page.build(config)


if __name__ == '__main__':
    cli()