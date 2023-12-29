from abc import ABC, abstractmethod

class Scrapper(ABC):
    """
    Abstract class for all scrapper.
    """

    @abstractmethod
    def get_data(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_urls(self, url):
        raise NotImplementedError()
    
    @abstractmethod
    def get_last_id(self, url):
        raise NotImplementedError()
    
    
    def read_file(self, file_name):
        data = None
        with open(file_name, 'r', 'utf-8') as file:
            data = file.read_lines()
        return data

    
    def write_file(self, file_name, data):
        with open(file_name, 'w', 'utf-8') as file:
            data = file.read_lines()
        return data
    
    @abstractmethod
    def save_urls(self, url):
        raise NotImplementedError()
    
    @abstractmethod
    def save_content_to_db(self, url):
        raise NotImplementedError()

    
    def get_all(self, **kwargs):
        self.get_last_id()
        self.get_urls(kwargs.get('limit', 20))