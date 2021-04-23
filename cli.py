# Custom CLI tool using Click

import click
from webScraper import webScraper

url = "https://ca.linkedin.com/jobs/amazon-data-scientist-jobs?position=1&pageNum=0"

@click.command()
@click.argument('url')
@click.argument('ele')
def web_scrap(url, ele):
    """Program that scraps the give URL"""
    click.echo("Welcome to my web scraper!")
    if not url or not ele:
        click.echo("URL and/or element to scrap for is empty.")
        return
    webScraper(url, ele)


if __name__ == '__main__':
    web_scrap()