from scrapper.src.base_classes import Scrapper
from scrapper.src.utils import get_content

class USCrapper(Scrapper):

    def __init__(self):
        self.url = 'https://search-study-uk.britishcouncil.org/course/search-results.html?onlineFlag=Y&OnCampusNowFlag=Y&OnCampusLaterFlag=Y'
        self.last_id = None

    def get_data(self):
        self.html = get_content(self.url)