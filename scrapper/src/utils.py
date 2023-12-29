from bs4 import BeautifulSoup
import requests

def get_content(link: str, parser='html.parser', **kwargs)->BeautifulSoup:
    response = requests.get(link, **kwargs)
    html_content = response.content
    return BeautifulSoup(html_content, parser)